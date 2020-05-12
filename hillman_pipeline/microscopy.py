import datajoint as dj

schema = dj.schema('hillman_microscope')
#schema.drop(True)
#schema = dj.schema('hillman_microscope')


@schema
class ScapeSystem(dj.Lookup):
    # SCAPE Setup for different setup, e.g.: SCAPE3, MesoSCAPE, etc.
    definition = """
    scape_name                   :   varchar(32)
    ---
    scape_description=''         :   varchar(2047)
    system_location=''           :   varchar(256)
    person_in_charge=''          :   varchar(128)
    """
    contents = [dict(scape_name='scape3')]


@schema
class Laser(dj.Lookup):
    # Lasers inventory
    definition = """
    laser                       : varchar(32)            # unique nickname of laser
    ---
    laser_brand                 : varchar(256)
    laser_model                 : varchar(256)
    laser_serial_number         : varchar(128)
    unique index (laser_serial_number)
    laser_wavelength            : smallint unsigned      # (nm)
    laser_max_power             : decimal(7, 1)          # (mW)
    laser_tunable               : bool
    """

@schema
class Objective(dj.Lookup):
    # Objectives inventory
    definition = """
    objective                   : varchar(32)    # unique nickname of objective
    ---
    objective_mag               : decimal(4, 1)  #
    objective_na                : decimal(3, 2)
    objective_imm               : enum('air', 'water', 'oil', 'silicone oil', 'clearing media')
    objective_manufacturer      : enum('Nikon', 'Olympus', 'Leica', 'Zeiss', 'Edmund', 'Mitutoyo')
    objective_part_number       : varchar(64)
    objective_focal_length      : decimal(5, 2)  # (mm)
    objective_back_focal_plane  : decimal(5, 2)  # (mm)
    """

@schema
class Camera(dj.Lookup):
    # Camera inventory
    definition = """
    camera                      : varchar(32)    # unique nickname of camera
    ---
    camera_manufacturer         : enum('Andor', 'Lambert', 'Hamamatsu', 'Teledyne', 'Basler', 'FLIR','PCO')
    camera_model                : varchar(64)
    camera_serial_number        : varchar(128)
    unique index (camera_serial_number)
    camera_pixelsize            : decimal(4, 2)  # (um)
    is_color_camera=0           : bool
    """


@schema
class TubeLens(dj.Lookup):
    # Tubelens inventory
    definition = """
    tubelens                    : varchar(32)
    ---
    tubelens_focal_length       : decimal(5, 2)  # (mm)
    tubelens_manufacturer       : varchar(32)
    tubelens_part_number        : varchar(64)
    tubelens_zoomable           : bool
    """

@schema
class Filter(dj.Lookup):
    # Filters inventory
    definition = """
    filter                            : varchar(64)   # unique nickname of filter
    ---
    filter_manufacturer               : varchar(64)
    filter_brand                      : varchar(64)
    filter_model_number               : varchar(64)
    filter_center_wavelength          : smallint      # (nm)
    filter_bandwidth                  : smallint      # (nm)
    """

@schema
class ScapeConfig(dj.Manual):
    # Version of Optical/Hardware Setup
    definition = """
    -> ScapeSystem
    scape_config_number      : varchar(16)   # e.g. 3.1.2
    ---
    scape_config_date        : date
    sys_description=''       : varchar(256)
    laser_coupling           : enum("Dichroic", "Mirror")
    scape_magnification      : float         # Magnification ratio with respect to 70 mm tube lens
    cal_k                    : decimal(5, 2)
    """

    class Laser(dj.Part):
        # Laser in use
        definition = """
        -> master
        laser_id             : tinyint # Laser 1,2...,n. n is The number of lasers in the system
        ---
        -> Laser
        """

    class Objective(dj.Part):
        # Objective in use
        definition = """
        -> master
        objective_id         : tinyint # Objecitve 1/2/3
        ---
        -> Objective
        """

    class Camera(dj.Part):
        # Camera(s) that the SCAPE configuration may potentially employ
        definition = """
        -> master
        camera_id            : tinyint
        ---
        -> Camera
        """
