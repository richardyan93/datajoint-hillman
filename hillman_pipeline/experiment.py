import datajoint as dj
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import microscopy, lab

schema = dj.schema('hillman_experiment')


@schema
class Species(dj.Lookup):
    definition = """
    species        :  varchar(32)
    """
    contents = zip(['mouse', 'C elegans', 'rat', 'fly','zebrafish','human','weird stuff','Tardigrade'])


@schema
class Genotype(dj.Lookup):
    definition = """
    -> Species
    genotype_nickname           : varchar(32)
    ---
    genotype_fullname           : varchar(255)
    zygosity='Unknown'          : enum('Homo', 'Hetero', 'Positive', 'Negative', 'Unknown')
    genotype_description=''     : varchar(1024)
    source=''                   : varchar(32)
    """


@schema
class TissueType(dj.Lookup):
    # Fixed,expanded,cleared,fresh
    definition = """
    tissue_type                 : varchar(32)
    ---
    tissue_type_description=''  : varchar(1024)
    """


@schema
class Specimen(dj.Manual):
    definition = """
    specimen        : varchar(64)
    ---
    -> lab.LabMember.proj(source='user')
    -> Species
    -> [nullable] Genotype
    specimen_description =''    :varchar(1024)
    pathology=''        :varchar(255)
    """

    class Tissue(dj.Part):
        # Check with Kripa
        definition = """
        -> master
        ---
        -> TissueType
        tissue_description='': varchar(1024)
        """


@schema
class PreparationType(dj.Lookup):
    # In-vivo, ex-vivo, sliced
    definition = """
    prep_type    : varchar(32)
    ---
    prep_type_description='' : varchar(1024)
    """


@schema
class Preparation(dj.Manual):
    definition = """
    -> Specimen
    prep_time       : datetime
    ---
    -> PreparationType
    prep_note=''    : varchar(1024)
    """


@schema
class Organ(dj.Lookup):
    definition = """
    organ                   : varchar(32)
    ---
    organ_discription=''    : varchar(255)
    """
    contents = [['brain', ''], ['whole body', '']]


@schema
class BehavioralSetup(dj.Manual):
    definition = """
    behavior_setup                       : varchar(32)    # unique nickname of a behavior set up
    ---
    behavior_setup_date                  : date
    behavior_setup_description=''        : varchar(1024)
    """

    class Camera(dj.Part):
        definition = """
        -> master
        camera_id               :  tinyint unsigned
        ---
        -> microscopy.Camera
        -> microscopy.Filter
        camera_description=''   : varchar(1024)
        """


@schema
class StimSetup(dj.Manual):
    definition = """
    stim_setup                  : varchar(32)     # unique nickname of a stim set up
    ---
    stim_description            : varchar(1024)
    """


@schema
class Session(dj.Manual):
    definition = """
    session_name            : varchar(32)
    ---
    -> lab.LabMember
    -> microscopy.ScapeConfig
    -> [nullable]lab.Project
    session_date            : datetime
    data_directory          : varchar(256)     # location on server
    backup_location         : varchar(64)      # location of cold backup, eg. GOAT_BACKUP_10
    """

    class Specimen(dj.Part):
        definition = """
        -> master
        -> Specimen
        """


@schema
class Scan(dj.Manual):
    definition = """
    -> Session.Specimen
    scan_name                       :   varchar(64)
    ---
    -> [nullable] Organ
    scan_metadata_file              :   varchar(256)   # File name of metadata
    scan_note=''                    :   varchar(1024)
    scan_start_time                 :   datetime
    scan_status                     :   enum('Successful', 'Interrupted','NULL')
    dual_color=0                    :   bool
    scan_size=null                  :   decimal(5, 1)     # GB
    -> [nullable] StimSetup
    excitation_NA=nullable          :  enum('HighNA','MediumNA','LowNA')
    nd_filter                       :  decimal(3, 2)      # O.D.
    run_condition=''                :  enum('Awesome','SADDD','IcanGraduate!','Test','')
    """

    class DevStage(dj.Part):
        definition = """
        -> master
        ---
        dev_stage   :  enum('larva', 'adult','embryo','others')
        age         :  decimal(7, 2)            # age in the unit of age_unit
        age_unit    :  enum('hours', 'days', 'months', 'years', 'instar')
        dev_stage_note='': varchar(255)
        """

    class CaliFactor(dj.Part):
        definition = """
        -> master
        ---
        calibration_x                :   decimal(5, 3)  # (um/pixel)
        calibration_y                :   decimal(4, 3)  # (um/pixel)
        calibration_z                :   decimal(4, 3)  # (um/pixel)
        """

    class ScanParam(dj.Part):
        definition = """
        -> master
        ---
        vps                         :   decimal(5, 2)
        scan_fov_um                 :   decimal(7, 2)
        scan_fov_pixel              :   int unsigned    # Number of galvo steps,including flyback
        scan_length_vol             :   int unsigned    # Number of volumes recorded
        scan_length_s               :   decimal(8, 2)   # second
        scanner_type=''             :   enum('HR', '', 'Single Frame', 'Stage Scan')
        """

    class CameraParam(dj.Part):
        definition = """
        -> master
        -> microscopy.ScapeConfig.Camera
        ---
        camera_fps                  :   decimal(9, 2)
        camera_series_length        :   int unsigned         # Total frames recorded, including background
        camera_height               :   smallint unsigned    # pixel
        camera_width                :   smallint unsigned    # pixel
        -> microscopy.TubeLens
        tubelens_actual_focal_length=null  :   decimal(5, 2)  # (mm)
        """

    class FilterParam(dj.Part):
        definition = """
        -> master
        filter_index                :   smallint
        ---
        -> microscopy.Filter
        position=''                 :   varchar(64)   # Position of the filter, e.g. Red channel, dual channel dichroic, etc.
        """

    class LaserParam(dj.Part):
        definition = """
        -> master
        -> microscopy.ScapeConfig.Laser
        ---
        laser_purpose=''            : varchar(32)
        laser_output_power          : decimal(5, 1)      # (mW)
        laser_specimen_actualpower=''       : decimal(7, 3)   # (mW)
        laser_actual_wavelengh=null : decimal(5, 1)      # (nm)
        """
        #Laser_reprate=null
        
    class AiChannel(dj.Part):
        definition = """
        -> master
        channel_index               : smallint   # Physical DAQ analog input ID
        ---
        channel_purpose='hardware'  : enum('stimulus', 'hardware', 'other')
        channel_description=''      : varchar(1024)
        """

    class MiscParam(dj.Part):
        definition = """
        -> master
        ---
        saw_tooth=0                 :   bool
        scan_angle=NULL             :   decimal(7, 3)
        galvo_offset=0              :   decimal(4, 1)   # um
        ai_sampling_rate            :   int unsigned
        daq_data_filename           :   varchar(256)    # DAQ AI file name
        """

    class MiscFiles(dj.Part):
        definition = """
        -> master
        filename                    : varchar(256)
        ---
        file_description=''         : varchar(1024)
        """

    class BehaviorCamera(dj.Part):
        definition = """
        -> master
        -> BehavioralSetup.Camera
        ---
        behavior_recording_filename     : varchar(256)
        camera_fps                  :   decimal(7, 2)
        camera_series_length        :   int unsigned         # Total frames recorded, including background
        camera_height               :   smallint unsigned    # pixel
        camera_width                :   smallint unsigned    # pixel
        tubelens_focal_length       :   decimal(5, 2)        # (mm)
        tubelens_na=null            :   decimal(3,1)
        behavior_description=''     :   varchar(1024)
        """
