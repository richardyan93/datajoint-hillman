import datajoint as dj

schema = dj.schema('hillman_microscope')


@schema
class ScapeSystem(dj.Lookup):
    definition = """
    scape_name             :   varchar(32)
    ---
    scape_description=''   :   varchar(2047)
    """
    contents = [dict(scape_name='scape3')]


@schema
class Laser(dj.Manual):
    definition = """
    laser                       : varchar(32)            # unique nickname of laser
    ---
    laser_brand                 : varchar(256)
    laser_model                 : varchar(256)
    laser_serial_number         : varchar(128)
    unique index (laser_serial_number)
    laser_wavelength            : smallint unsigned      # (nm)
    laser_max_power             : decimal(7, 1)          # (mW)
    """

@schema
class Objective(dj.Manual):
    definition = """
    objective                   : varchar(32)    # unique nickname of objective
    ---
    objective_mag               : decimal(4, 1)  #
    objective_na                : decimal(3, 2)
    objective_imm               : enum('air', 'water', 'oil, 'silicone oil', 'clearing media')
    objective_manufacturer      : enum('Nikon', 'Olympus', 'Leica', 'Zeiss', 'Edmund', 'Mitutoyo')
    objective_part_number       : varchar(64)
    """


@schema
class ScapeConfig(dj.Manual):
    definition = """
    -> ScapeSystem
    scape_config_number      : varchar(16)   # e.g. 3.1.2
    ---
    scape_config_date        : date
    sys_description=''       : varchar(256)
    laser_coupling           : enum("Dichroic", "Mirror")
    """

    class Laser(dj.Part):
        definition = """
        -> master
        laser_id            : tinyint
        ---
        -> Laser
        """

    class Objective(dj.Part):
        definition = """
        -> master
        objective_id            : tinyint
        ---
        -> Objective
        """



@schema
class Camera_Config(dj.Lookup):
    definition = """
    ->SCAPE_Config
    ---
    camera_num=1                : smallint
    camera1                     : enum("Andor Zyla 4.2", "Andor Zyla 4.2 PLUS", "Andor Zyla 4.2 PLUS V2", "HiCam FLUO")
    camera2                     : enum("NULL", "Andor Zyla 4.2", "Andor Zyla 4.2 PLUS", "Andor Zyla 4.2 PLUS V2", "HiCam FLUO")
    camera_wf                   : varchar(1024)
    """

#error when using [nullable]
@schema
class TubeLens_Type(dj.Manual):
    definition = """
    tubelens_desciption         : varchar(256)
    ---
    focal_length_mm             : varchar(256)
    zoom                        : bool
    """
​
@schema
class TubeLens_Config(dj.Lookup):
    definition = """
    ->SCAPE_Config
    ---
    ->TubeLens_Type
    """
​
@schema
class LaserType(dj.Manual):
    definition = """
    laser_desciption            : varchar(256)
    ---
    laser_brand                 : varchar(256)
    laser_model                 : varchar(256)
    laser_wavelength            : varchar(8)
    laser_power_mw              : varchar(256)
    """
​
@schema
class LaserConfig(dj.Lookup):
    definition = """
    ->SCAPE_Config
    ---
    laser_num                   : varchar(256)
    ->Laser_Type
    """
​
@schema
class Filter_Type(dj.Manual):
    definition = """
    filter_desciption            : varchar(64)
    ---
    filter_brand                 : varchar(64)
    filter_model_number          : varchar(64)
    filter_center_wavelength     : smallint
    filter_bandwidth             : smallint
    """
​
@schema
class Channel(dj.Manual):
    definition = """
    -> SCAPE_Config
    channel_name:  varchar(16)
    """
​
@schema
class Filter_Config(dj.Lookup):
    definition = """
    ->SCAPE_Config
    ---
    filter_num                  : smallint
    """
​
    class PrimaryFilter(dj.Part):
        definition = """
        -> master
        primary_filter_description  : varchar(256)
        ---
        ->Filter_Type
        """
​
    class EmissionFilter(dj.Part):
        definition = """
        -> master
        -> Channel
        emission_filter_description  : varchar(256)
        ---
        ->Filter_Type
        """
