import datajoint as dj
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

schema = dj.schema('hillman_organism')

@schema
class Species(dj.Lookup):
    definition = """
    species                     : varchar(32)
    ---
    species_description=''      : varchar(256)
    """


@schema
class Genotype(dj.Lookup):
    definition = """
    -> Species
    genotype_nickname           : varchar(32)
    ---
    genotype_fullname           : varchar(255)
    zygosity='Unknown'          : enum('Homo', 'Hetero', 'Positive', 'Negative', 'Unknown')
    genotype_description=''     : varchar(1024)
    source=''                   : varchar(32)
    """


@schema
class TissueType(dj.Lookup):
    # Fixed,expanded,cleared,fresh
    definition = """
    tissue_type                 : varchar(32)
    ---
    tissue_type_description=''  : varchar(1024)
    """


@schema
class PreparationType(dj.Lookup):
    # In-vivo, ex-vivo, sliced
    definition = """
    prep_type                   : varchar(32)
    ---
    prep_type_description=''    : varchar(1024)
    """


@schema
class Organ(dj.Lookup):
    definition = """
    organ                       : varchar(32)
    ---
    organ_discription=''        : varchar(255)
    """
