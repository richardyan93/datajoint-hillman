import datajoint as dj

schema = dj.schema('hillman_lab')


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
