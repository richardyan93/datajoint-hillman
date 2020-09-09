import datajoint as dj
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import microscopy

schema = dj.schema('hillman_setup')


@schema
class Scapeconfig(dj.Lookup):
    # Version of Optical/Hardware Setup
    definition = """
    scape_config_number      : varchar(32)   # e.g. 3.1.2
    ---
    -> microscopy.ScapeSystem
    scape_config_date        : date
    sys_description=''       : varchar(1024)
    laser_coupling           : enum("Dichroic", "Mirror")
    scape_magnification      : float         # Magnification ratio with respect to 70 mm tube lens
    calibration_galvo        : decimal(5, 2) # um per voltage
    """

    class Laser(dj.Part):
        # Laser in use
        definition = """
        -> master
        laser_id             : tinyint # Laser 1,2...,n. n is The number of lasers in the system
        ---
        -> microscopy.Laser
        """

    class Objective(dj.Part):
        # Objective in use
        definition = """
        -> master
        objective_id         : tinyint # Objecitve 1/2/3
        ---
        -> microscopy.Objective
        """

    class Camera(dj.Part):
        # Camera(s) that the SCAPE configuration may potentially employ
        definition = """
        -> master
        camera_id            : tinyint
        ---
        -> microscopy.Camera
        """


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
        -> [nullable] microscopy.Filter
        camera_description=''   : varchar(1024)
        """


@schema
class StimSetup(dj.Manual):
    definition = """
    stim_setup                  : varchar(32)     # unique nickname of a stim set up
    ---
    stim_description            : varchar(1024)
    """
