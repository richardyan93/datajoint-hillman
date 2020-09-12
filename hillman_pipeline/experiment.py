import datajoint as dj
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import microscopy, lab, organism, setup

schema = dj.schema('hillman_experiment')


@schema
class Specimen(dj.Manual):
    definition = """
    specimen                                : varchar(64)
    ---
    -> lab.LabMember.proj(source='user')
    -> organism.Species
    -> [nullable] organism.Genotype
    -> [nullable] organism.TissueType
    -> [nullable] organism.PreparationType
    prep_time=NULL                          : datetime
    specimen_description =''                : varchar(1024)
    """

@schema
class Session(dj.Manual):
    definition = """
    session_name                            : varchar(32)
    ---
    -> lab.LabMember
    -> [nullable] lab.Project
    session_date                            : datetime
    data_directory                          : varchar(256)     # location on server
    backup_location                         : varchar(64)      # location of cold backup, eg. GOAT_BACKUP_10
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
    scan_metadata_file              :   varchar(256)   # File name of metadata
    scan_note=''                    :   varchar(1024)
    scan_start_time                 :   datetime
    scan_status                     :   enum('Successful', 'Interrupted','NULL')
    dual_color=0                    :   bool
    scan_size=0                     :   decimal(5, 1)     # GB
    nd_filter                       :   decimal(3, 2)      # O.D.
    run_condition='Unknown'         :   enum('Successful','Test','Unknown','Failed Run')
    scan_length_vol                 :   int unsigned    # Number of volumes recorded
    scan_length_sec                 :   decimal(8, 2)   # second
    scanner_type=''                 :   enum('HR', '', 'Single Frame', 'Stage Scan')
    vps                             :   decimal(5, 2)
    ai_sampling_rate                :   int unsigned
    daq_data_filename               :   varchar(256)    # DAQ AI file name
    -> [nullable] organism.Organ
    -> setup.Scapeconfig
    -> [nullable] setup.StimSetup
    -> [nullable] setup.BehavioralSetup
    filter_config                   :   varchar(1024)
    """

    class DevStage(dj.Part):
        definition = """
        -> master
        ---
        dev_stage                       :   enum('larva', 'adult','embryo','others')
        age=0                           :   decimal(7, 2)            # age in the unit of age_unit
        age_unit='Unknown'              :   enum('hours', 'days', 'months', 'years', 'instar','Unknown')
        """

    class CaliFactor(dj.Part):
        definition = """
        -> master
        ---
        calibration_x                   :   decimal(5, 3)  # (um/pixel)
        calibration_y                   :   decimal(4, 3)  # (um/pixel)
        calibration_z                   :   decimal(4, 3)  # (um/pixel)
        """

    class GalvoParam(dj.Part):
        definition = """
        -> master
        ---
        scan_fov_um                 :   decimal(7, 2)
        scan_fov_pixel              :   int unsigned    # Number of galvo steps,including flyback
        scan_angle=0                :   decimal(7, 3)
        galvo_offset=0              :   decimal(4, 1)   # um
        saw_tooth=0                 :   bool
        """

    class CameraParam(dj.Part):
        definition = """
        -> master
        camera_id                           :   tinyint
        ---
        camera_fps                          :   decimal(9, 2)
        camera_series_length                :   int unsigned         # Total frames recorded, including background
        camera_height                       :   smallint unsigned    # pixel
        camera_width                        :   smallint unsigned    # pixel
        -> microscopy.Camera
        -> microscopy.TubeLens
        tubelens_actual_focal_length=null   :   decimal(5, 2)  # (mm)
        """

    class LaserParam(dj.Part):
        definition = """
        -> master
        -> setup.Scapeconfig.Laser
        ---
        laser_purpose=''                    : varchar(32)
        laser_output_power                  : decimal(5, 1)      # (mW)
        laser_specimen_actualpower=0        : decimal(7, 3)      # (mW)
        """

    class TunableLaserParam(dj.Part):
        definition = """
        -> master
        -> setup.Scapeconfig.Laser
        ---
        laser_wavelengh             : decimal(5, 1)      # (nm)
        laser_reprate               : decimal(7, 1)      # (kHz)
        """

    class AiChannel(dj.Part):
        definition = """
        -> master
        channel_index               : smallint   # Physical DAQ analog input ID
        ---
        channel_purpose='hardware'  : enum('stimulus', 'hardware', 'other')
        channel_description=''      : varchar(1024)
        """

    class MiscFiles(dj.Part):
        definition = """
        -> master
        filename                    :   varchar(256)
        ---
        file_description=''         :   varchar(1024)
        """

    class MiscParam(dj.Part):
        definition = """
        -> master
        param_name              : varchar(32)
        ---
        param_value             : varchar(64)
        param_description=''    : varchar(256)
        """

    class BehaviorCamera(dj.Part):
        definition = """
        -> master
        -> setup.BehavioralSetup.Camera
        ---
        behavior_recording_filename     :   varchar(256)
        camera_fps                      :   decimal(7, 2)
        camera_series_length            :   int unsigned         # Total frames recorded, including background
        camera_height                   :   smallint unsigned    # pixel
        camera_width                    :   smallint unsigned    # pixel
        tubelens_focal_length           :   decimal(5, 2)        # (mm)
        tubelens_na=null                :   decimal(3,1)
        behavior_description=''         :   varchar(1024)
        """
