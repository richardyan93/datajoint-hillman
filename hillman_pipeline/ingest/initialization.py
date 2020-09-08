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
#data = []
#microscopy.Laser.insert(data,skip_duplicates=True)

# microscopy.Objective
data =[
    {'objective':'Olympus20x_1.0','objective_mag':20,'objective_na':1.0,
    'objective_imm':'water','objective_manufacturer':'Olympus',
    'objective_part_number':'XLUMPLFLN20XW','objective_focal_length':9,
    'objective_back_focal_plane':-48.1},
    {'objective':'Nikon40x_0.95','objective_mag':40,'objective_na':0.95,
    'objective_imm':'air','objective_manufacturer':'Nikon',
    'objective_part_number':'CFI Plan Apochromat Lambda 40XC',
    'objective_focal_length':5,'objective_back_focal_plane':99},
    {'objective':'Mitutoyo50x_0.75','objective_mag':50,'objective_na':0.75,
    'objective_imm':'air','objective_manufacturer':'Mitutoyo',
    'objective_part_number':'BD Plan Apo HR 50×',
    'objective_focal_length':5,'objective_back_focal_plane':99},
]
microscopy.Objective.insert(data,skip_duplicates=True)

# microscopy.Camera
data = [
        {'camera':'zyla4.2','camera_manufacturer':'Andor','camera_model','Zyla4.2',
        'camera_pixelsize':6.5,'is_color_camera',0},
        {'camera':'HiCAM Fluo','camera_manufacturer':'Lambert','camera_model','HiCAM Fluo',
        'camera_pixelsize':9.9,'is_color_camera',0},
]
microscopy.Camera.insert(data,skip_duplicates=True)

# microscopy.Tubelens


# micoscopy.Filter
