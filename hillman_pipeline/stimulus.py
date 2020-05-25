import datajoint as dj

schema = dj.schema('hillman_stimulus')


@schema
class StimulusType(dj.Manual):
    definition = """
    """

    class AirPuff(dj.Part):
        definition = """
        -> master
        """
