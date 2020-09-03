import datajoint as dj
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lab, microscopy, organism, peripheralsetup, experiment

# lab.Lab
data = [
  {'lab': 'Hillmanlab', 'lab_description': ''},
]

lab.Lab.insert(data)

# lab.LabMember
data = [
    {'user':'Boss','lab':'Hillmanlab'},
    {'user':'Sam_Benezra','lab':'Hillmanlab'},
    {'user':'Wenze_Li','lab':'Hillmanlab'},
    {'user':'Wenxuan_Liang','lab':'Hillmanlab'},
    {'user':'Malte_Casper','lab':'Hillmanlab'},
    {'user':'Grace_Lee','lab':'Hillmanlab'},
    {'user':'Wenze_Li','lab':'Hillmanlab'},
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
lab.LabMember.insert(data)

# lab.project
data = [
    {'project':'NeuroPal','user':'Richard_Yan'},
    {'project':'Kimara Heart','user':'Richard_Yan'},
]
lab.Project.insert(data)

# ScapeSystem
