
%{
# Zygosity - we can add here exact definitions for the enum
-> hillman_mouse_subject.Subject
-> hillman_mouse_subject.Allele
---
zygosity: enum("Present", "Absent", "Homozygous Negative", "Homozygous Positive", "Heterozygous")
zygosity_ts = CURRENT_TIMESTAMP: timestamp
%}

classdef Zygosity < dj.Lookup
    
end

