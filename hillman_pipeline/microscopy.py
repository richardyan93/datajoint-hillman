import datajoint as dj
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import lab

schema = dj.schema('hillman_microscope')


@schema
class ScapeSystem(dj.Lookup):
    # Different SCAPE setup, e.g.: SCAPE3, MesoSCAPE, etc.
    definition = """
    scape_name                   :   varchar(32)
    ---
    scape_description=''         :   varchar(1024)
    -> lab.LabMember.proj(person_in_charge='user')
    """


@schema
class Laser(dj.Lookup):
    # Lasers inventory
    definition = """
    laser                       : varchar(32)            # unique nickname of laser
    ---
    laser_brand                 : varchar(64)
    laser_part_number           : varchar(64)
    unique index (laser_part_number)
    laser_wavelength            : smallint unsigned      # (nm)
    laser_max_power             : decimal(7, 1)          # (mW)
    """

    class Tunable_laser(dj.Part):
        definition = """
        -> master
        ---
        laser_wavelength_range          : varchar(128)
        laser_reprate_range             : varchar(128)
        """


@schema
class Objective(dj.Lookup):
    # Objectives inventory
    definition = """
    objective                      : varchar(32)    # unique nickname of objective
    ---
    objective_mag                  : decimal(4, 1)  #
    objective_na                   : decimal(3, 2)
    objective_imm                  : enum('air', 'water', 'oil', 'silicone oil', 'clearing media')
    objective_manufacturer         : enum('Nikon', 'Olympus', 'Leica', 'Zeiss', 'Edmund', 'Mitutoyo')
    objective_part_number          : varchar(64)
    objective_focal_length         : decimal(5, 2)  # (mm)
    [nullable]objective_back_focal_plane     : decimal(5, 2)  # (mm)
    """


@schema
class Camera(dj.Lookup):
    # Camera inventory
    definition = """
    camera                      : varchar(32)    # unique nickname of camera
    ---
    camera_manufacturer         : enum('Andor', 'Lambert', 'Hamamatsu', 'Teledyne', 'Basler', 'FLIR','PCO', 'ALLIED VISION')
    camera_model                : varchar(64)
    camera_pixelsize            : decimal(4, 2)  # (um)
    is_color_camera=0           : bool
    """


@schema
class TubeLens(dj.Lookup):
    # Tubelens inventory
    definition = """
    tubelens                    : varchar(64)
    ---
    tubelens_focal_length       : decimal(5, 2)  # (mm)
    tubelens_manufacturer       : varchar(32)
    tubelens_part_number=''     : varchar(64)
    tubelens_zoomable=0         : bool
    """


@schema
class Filter(dj.Lookup):
    # Filters inventory
    definition = """
    filter_part_number                : varchar(32)
    ---
    filter_manufacturer               : varchar(64)
    filter_description =''            : varchar(256)
    """
