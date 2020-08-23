import datajoint as dj
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import microscopy

schema = dj.schema('hillman_peripheralSetup')

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
