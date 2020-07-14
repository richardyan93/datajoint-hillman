import datajoint as dj

schema = dj.schema('hillman_lab')


@schema
class Lab(dj.Lookup):
    definition = """
    lab                     : varchar(32)    # e.g. Randylab, Hillmanlab
    ---
    lab_description=''      : varchar(255)
    """
    contents = [['hillmanlab', '']]


@schema
class LabMember(dj.Lookup):
    definition = """
    user        : varchar(32)
    ---
    -> Lab
    """
    contents = [['richard yan','hillmanlab'],
                ['wenze li', 'hillmanlab'],
                ['hang yu','hillmanlab'],
                ['wenxuan liang','hillmanlab'],
                ['sam benezra','hillmanlab'],
                ['malte casper','hillmanlab'],
                ['grace lee','hillmanlab'],
                ['kripa patel','hillmanlab'],
                ['citlali campos','hillmanlab'],
                ['venkata voleti','hillmanlab'],
                ['boss','hillmanlab']]
                

@schema
class Source(dj.Lookup):
    definition = """
    source_name:    varchar(32)               # unique source id
    ---
    source_full_name='': varchar(255)  	      # name of source
    contact_details='': varchar(255)
    link_to_wedsite='':  varchar(255)
    source_description='':	varchar(255)
    source_ts = CURRENT_TIMESTAMP: timestamp
    """


@schema
class Project(dj.Lookup):
    definition = """
    project                     : varchar(32)
    ---
    -> LabMember
    project_description=''      : varchar(1024)
    """
    contents =[['NeuroPal','richard yan',''],
               ['KimaraHeart','richard yan','']]