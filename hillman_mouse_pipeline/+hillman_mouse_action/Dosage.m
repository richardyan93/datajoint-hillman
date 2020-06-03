%{
# Dosage
-> hillman_mouse_subject.Nickname
dosage_time: datetime
---
-> hillman_common_lab.Drug
dosage :                        decimal(3, 1)  # dilution
injection_site :                enum('IP', 'SC', 'IV', ’IM‘) #please add explanation
injection_amount :              decimal(4, 2)  # (mL)
dosage_ts = CURRENT_TIMESTAMP:  timestamp
%}

classdef Dosage < dj.Manuals
    
end