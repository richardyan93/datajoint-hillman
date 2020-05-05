import datajoint as dj

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


@schema
class StimulusType(dj.Lookup):
    pass
    # TODO: to think about the structure of stimulus type


@schema
class Session(dj.Manual):
    definition = """
    -> Specimen
    session_start_time      : datetime
    ---
    data_directory          : varchar(1024)
    -> Organ
    """

    class DevStage(dj.Part):
        definition = """
        -> master
        ---
        dev_stage   :  enum('larva', 'adult')
        age         :  float                 # age in the unit of age_unit
        age_unit    :  enum('hours', 'days', 'months', 'years', 'instar')
        dev_stage_note='': varchar(255)
        """


@schema
class LaserSetting(dj.Lookup):
    definition = """
    laser_purpose               :   varchar(256)
    ---
    laser_output_power          :   float   # what's the best way to have multiple laser output power here?
    nd_filter                   :   varchar(32)     #should we use enum here?
    laser_power_actual_mw       :   float
    """


@schema
class ScanParameter(dj.Manual):
    definitoin = """
    -> Session
    -> microscopy.ScapeConfig
    scan_idx                        :   int
    ---
    scan_note                       :   varchar(1024)
    scan_start_time                 :   datetime
    scan_status                     :   enum("Successful", "Interrupted")
    dual_color                      :   bool
    stim_status                     :   yes
    scan_size_gb                    :   float
    """
​
    class CameraParam(dj.Part):
        definition = """
        -> master
        ---
        camera_fps                  :   float
        camera_series_length        :   int
        camera_roi_x                :   int
        camera_roi_y                :   int
        """

    class CaliFactor(dj.Part):
        definition = """
        ->master
        ---
        cali_k                      :   float
        cali_x                      :   float
        cali_y                      :   float
        cali_z                      :   float
        """
    class ScanParam(dj.Part):
        definition = """
        -> master
        ---
        vps                         :   float
        scan_fov_um                 :   float
        scan_fov_pixel              :   float
        scan_length_vol             :   int
        scan_length_s               :   float
        scanner_type                :   enum("HR", "LR", "Single Frame", "Stage Scan")
        """
    class LaserParam(dj.Part):
        definition = """
        -> master
        laser_num_in_use            :   smallint
        ---
        -> LaserSetting
        """
    class FilterParam(dj.Part):
        definition = """
        -> master
        filter_num_in_use           :   smallint
        ---
        -> FilterType
        """
    class OtherParam(dj.Part):
        definition = """
        -> master
        ---
        saw_tooth                   :   bool
        scan_angle                  :   float
        galvo_offset                :   float
        ai_channel                  :   smallint
        ai_sampling_rate            :   int
        scan_waveform               :   longblob
        """
