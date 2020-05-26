import datajoint as dj
import microscopy

schema = dj.schema('hillman_experiment')


@schema
class Lab(dj.Lookup):
    definition = """
    lab                     : varchar(32)    # e.g. Randylab, Hillmanlab
    ---
    lab_description=''      : varchar(255)
    """


@schema
class LabMember(dj.Lookup):
    definition = """
    user        : varchar(32)
    ---
    -> Lab
    """


@schema
class Project(dj.Lookup):
    definition = """
    project                     : varchar(32)
    ---
    -> LabMember
    project_description=''      : varchar(1024)
    """


@schema
class Species(dj.Lookup):
    definition = """
    species        :  varchar(32)
    """


@schema
class Genotype(dj.Lookup):
    definition = """
    -> Species
    genotype_nickname           : varchar(32)
    ---
    genotype_fullname           : varchar(255)
    zygosity='Unknown'          : enum('Homo', 'Hetero', 'Positive', 'Negative', 'Unknown')
    genotype_description=''     : varchar(255)
    """


@schema
class TissueType(dj.Lookup):
    definition = """
    tissue_type                 : varchar(32)
    ---
    tissue_type_description=''  : varchar(1024)
    """


@schema
class Specimen(dj.Manual):
    definition = """
    specimen        : varchar(32)
    ---
    -> LabMember.proj(source='user')
    -> Species
    -> [nullable] Genotype
    """

    class Tissue(dj.Part):
        definition = """
        -> master
        ---
        -> TissueType
        tissue_description='': varchar(1024)
        """


@schema
class PreparationType(dj.Lookup):
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


#@schema
#class StimulusType(dj.Lookup):
#    pass
    # TODO: to think about the structure of stimulus type
    # stimulus_directory      :varchar(1024)
    # stimulus_description   ：varchar(1024)


@schema
class Session(dj.Manual):
    definition = """
    -> Specimen
    session_start_time      : datetime
    ---
    data_directory          : varchar(1024)     # location on server
    backup_location         : varchar(128)      # location of cold backup, eg. GOAT_BACKUP_10
    -> Organ
    """

    class DevStage(dj.Part):
        definition = """
        -> master
        ---
        dev_stage   :  enum('larva', 'adult')
        age         :  decimal(7, 2)            # age in the unit of age_unit
        age_unit    :  enum('hours', 'days', 'months', 'years', 'instar')
        dev_stage_note='': varchar(255)
        """


@schema
class Scan(dj.Manual):
    definition = """
    -> Session
    scan_index                      :   smallint
    ---
    -> microscopy.ScapeConfig
    scan_filename                   :   varchar(1024)
    scan_note                       :   varchar(1024)
    scan_start_time                 :   datetime
    scan_status                     :   enum('Successful', 'Interrupted','NULL')
    dual_color                      :   bool
    stim_status                     :   bool
    stim_description                :   varchar(1024)
    scan_size_gb                    :   decimal(5, 1)
    """

    class CameraParam(dj.Part):
        definition = """
        -> master
        -> microscopty.ScapeConfig.Camera
        ---
        camera_fps                  :   decimal(7, 2)
        camera_series_length        :   int unsigned         # Total frames recorded, including background
        camera_height               :   smallint unsigned    # pixel
        camera_width                :   smallint unsigned    # pixel
        -> microscopy.TubeLens
        tubelens_actual_focal_length=null  :   decimal(5, 2)  # (mm)
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
        scan_fov_pixel              :   int unsigned    # Number of galvo steps
        scan_length_vol             :   int unsigned    # Number of volumes recorded
        scan_length_s               :   decimal(8, 2)   # second
        scanner_type                :   enum("HR", "LR", "Single Frame", "Stage Scan")
        """

    class LaserParam(dj.Part):
        definition = """
        -> master
        -> microscopy.ScapeConfig.Laser
        ---
        laser_purpose               : varchar(32)
        laser_output_power          : decimal(5, 1)      # (mW)
        nd_filter                   : decimal(3, 2)
        laser_power_actual_mw       : decimal(5, 1)
        laser_actual_wavelengh=null : decimal(5, 1)      # (nm)
        """

    class FilterParam(dj.Part):
        definition = """
        -> master
        filter_index                :   smallint
        ---
        -> microscopy.Filter
        """

    class AiChannel(dj.Part):
        definition = """
        -> master
        channel_index               : smallint   # Physical DAQ analog input ID
        ---
        channel_purpose='hardware'  : enum('stimulus', 'hardware', 'other')
        channel_description=''      : varchar(1024)
        """

    class OtherParam(dj.Part):
        definition = """
        -> master
        ---
        saw_tooth=0                 :   bool
        scan_angle                  :   decimal(7, 3)
        galvo_offset                :   decimal(4, 1)   # um
        ai_sampling_rate            :   int unsigned
        scan_waveform               :   longblob
        """


@schema
class BehavioralCamera(dj.Lookup):
    definition = """
    behavioral_camera    : varchar(32)    # unique nickname of a behavioral camera
    ---
    behavioral_camera_part_no=''     : varchar(64)
    behavioral_camera_manufacturer   : enum('FLIR', 'BASLER', 'ALLIED VISION')
    """


@schema
class BehavioralSetup(dj.Manual):
    definition = """
    behavior_setup              : varchar(32)    # name of a set up
    behavior_setup_date         : date
    """

    class Camera(dj.Part):
        definition = """
        -> master
        camera_id               :  tinyint unsigned
        ----
        -> BehavioralCamera
        """

        class Filter(dj.Part):
            definition = """
            -> master.Camera
            ---
            -> microscopy.Filter
            """


@schema
class BehavioralRecording(dj.Manual):
    definition = """
    -> Scan
    behavior_recording_index        : tinyint unsigned
    ---
    behavior_recording_filename     : varchar(1024)
    # light_source                    : enum('')
    -> BehavioralSetup
    """

    class CameraParam(dj.Part):
        definition = """
        -> master
        -> BehavioralSetup.Camera
        ---
        camera_fps                  :   decimal(7, 2)
        camera_series_length        :   int unsigned         # Total frames recorded, including background
        camera_height               :   smallint unsigned    # pixel
        camera_width                :   smallint unsigned    # pixel
        tubelens_focal_length=null  :   decimal(5, 2)  # (mm)
        tubelens_na=null            :   decimal(3,1)
        """
