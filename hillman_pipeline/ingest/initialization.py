import datajoint as dj
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lab, microscopy, organism, setup, experiment

# lab.Lab
data = [
    {'lab': 'Hillmanlab', 'lab_description': ''},
]
lab.Lab.insert(data,skip_duplicates=True)

# lab.LabMember
data = [
    {'user':'Boss','lab':'Hillmanlab'},
    {'user':'Sam_Benezra','lab':'Hillmanlab'},
    {'user':'Wenze_Li','lab':'Hillmanlab'},
    {'user':'Wenxuan_Liang','lab':'Hillmanlab'},
    {'user':'Malte_Casper','lab':'Hillmanlab'},
    {'user':'Grace_Lee','lab':'Hillmanlab'},
    {'user':'Elizabeth_Malan','lab':'Hillmanlab'},
    {'user':'Kripa_Patel','lab':'Hillmanlab'},
    {'user':'Nic_Thibodeaux','lab':'Hillmanlab'},
    {'user':'Weihao_Xu','lab':'Hillmanlab'},
    {'user':'Richard_Yan','lab':'Hillmanlab'},
    {'user':'Hang_Yu','lab':'Hillmanlab'},
    {'user':'Teresa_Zhao','lab':'Hillmanlab'},
    {'user':'Chinwendu_Nwokeabia','lab':'Hillmanlab'},
    {'user':'Citlali_Campos','lab':'Hillmanlab'},
    {'user':'Alexis_Yagielski','lab':'Hillmanlab'},
]
lab.LabMember.insert(data,skip_duplicates=True)

# lab.project
data = [
    {'project':'NeuroPal','user':'Richard_Yan'},
    {'project':'Kimara Heart','user':'Richard_Yan'},
]
lab.Project.insert(data,skip_duplicates=True)

# microscopy.ScapeSystem
data = [
    {'scape_name':'Super SCAPE','person_in_charge':'Wenze_Li'},
    {'scape_name':'Yan SCAPE','person_in_charge':'Richard_Yan'},
    {'scape_name':'Meso SCAPE','person_in_charge':'Grace_Lee'},
    {'scape_name':'2P SCAPE','person_in_charge':'Hang_Yu'},
]
microscopy.ScapeSystem.insert(data,skip_duplicates=True)

# microscopy.Laser
data = [
    {'laser':'OBIS405','laser_brand':'Coherent','laser_part_number':'OBIS 405 nm LX 100 mW','laser_wavelength':405,'laser_max_power':100},
    {'laser':'OBIS488','laser_brand':'Coherent','laser_part_number':'OBIS 488 nm LX 150 mW','laser_wavelength':488,'laser_max_power':150},
    {'laser':'OBIS561','laser_brand':'Coherent','laser_part_number':'OBIS 561 nm LS 150 mW','laser_wavelength':561,'laser_max_power':150},
    {'laser':'OBIS594','laser_brand':'Coherent','laser_part_number':'OBIS 594 nm LS 100 mW','laser_wavelength':594,'laser_max_power':100},
    {'laser':'OBIS637','laser_brand':'Coherent','laser_part_number':'OBIS 637 nm LX 140 mW','laser_wavelength':637,'laser_max_power':140},
]
microscopy.Laser.insert(data,skip_duplicates=True)

# microscopy.Objective
data = [
    {'objective':'Olympus20x_1.0','objective_mag':20,'objective_na':1.0,'objective_imm':'water','objective_manufacturer':'Olympus','objective_part_number':'XLUMPLFLN20XW','objective_focal_length':9,'objective_back_focal_plane':-48.1},
    {'objective':'Nikon40x_0.95','objective_mag':40,'objective_na':0.95,'objective_imm':'air','objective_manufacturer':'Nikon','objective_part_number':'CFI Plan Apochromat Lambda 40XC','objective_focal_length':5,'objective_back_focal_plane':99},
    {'objective':'Mitutoyo50x_0.75','objective_mag':50,'objective_na':0.75,'objective_imm':'air','objective_manufacturer':'Mitutoyo','objective_part_number':'BD Plan Apo HR 50×','objective_focal_length':4,'objective_back_focal_plane':99},
]
microscopy.Objective.insert(data,skip_duplicates=True)

# microscopy.Camera
data = [
    {'camera':'zyla4.2','camera_manufacturer':'Andor','camera_model':'Zyla4.2','camera_pixelsize':6.5,'is_color_camera':0},
    {'camera':'HiCAM Fluo','camera_manufacturer':'Lambert','camera_model':'HiCAM Fluo','camera_pixelsize':9.9,'is_color_camera':0},
]
microscopy.Camera.insert(data,skip_duplicates=True)

# microscopy.TubeLens
data = [
    {'tubelens':'navitar_35/1.4','tubelens_focal_length':35,'tubelens_manufacturer':'Navitar','tubelens_part_number':'MVL35M1','tubelens_zoomable':0},
    {'tubelens':'canon_50/1.8','tubelens_focal_length':50,'tubelens_manufacturer':'Canon','tubelens_part_number':'','tubelens_zoomable':0},
    {'tubelens':'Nikon_70','tubelens_focal_length':70,'tubelens_manufacturer':'Nikon','tubelens_part_number':'','tubelens_zoomable':0},
    {'tubelens':'navitar_100/2.8','tubelens_focal_length':100,'tubelens_manufacturer':'Navitar','tubelens_part_number':'MVL100M23','tubelens_zoomable':0},
]
microscopy.TubeLens.insert(data,skip_duplicates=True)

# micoscopy.Filter
data = [
    {'filter_part_number':'FF01-449/520-25','filter_manufacturer':'Semrock','filter_description':'BFP/GFP DUAL BANDPASS'},
    {'filter_part_number':'ZET594TopNotch','filter_manufacturer':'Chroma','filter_description':'594 Bandstop'},
    {'filter_part_number':'ET575lp','filter_manufacturer':'Chroma','filter_description':''},
    {'filter_part_number':'FF560-FDi01','filter_manufacturer':'Semrock','filter_description':''},
]
microscopy.Filter.insert(data,skip_duplicates=True)

# organism.Species
data = [
    {'species':'C Elegans','species_description':''},
    {'species':'Zebrafish','species_description':''},
]
organism.Species.insert(data,skip_duplicates=True)

# organism.Genotype
data = [
    {'species':'C Elegans','genotype_nickname':'OH6230','genotype_fullname':'OH6230','zygosity':'Unknown','genotype_description':'','source':'Hobert Lab'},
]
organism.Species.Genotype.insert(data,skip_duplicates=True)

# organism.TissueType
data = []
organism.TissueType.insert(data,skip_duplicates=True)

# organism.PreparationType
data = []
organism.PreparationType.insert(data,skip_duplicates=True)

# organism.Organ
data = [
    {'species':'C Elegans','organ':'whole body','organ_discription':''},
    {'species':'C Elegans','organ':'head','organ_discription':''},
    {'species':'C Elegans','organ':'tail','organ_discription':''},
    {'species':'Zebrafish','organ':'Out flow track','organ_discription':''},
]
organism.Species.Organ.insert(data,skip_duplicates=True)
