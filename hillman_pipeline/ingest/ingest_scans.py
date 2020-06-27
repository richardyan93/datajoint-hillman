import datajoint as dj
import h5py
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import experiment, microscopy
import re
import datetime
import numpy as np

# helper functions
def dataset_to_string(dataset):
    return ''.join([chr(x) for x in np.hstack(dataset[()])])


def dataset_to_scalar(dataset, decimal=2):
    return round(dataset[()][0][0], decimal)

# User input section
session_dir = 'D:\\Neuropal20200528'
source = 'richardyan'
species = 'worm'

# insert ScapeConfig (fake)
scape_config = dict(
    scape_name='scape3',
    scape_config_number='3.1.2',
    scape_config_date=datetime.date(2019, 5, 1),
    laser_coupling='Dichroic',
    scape_magnification=40.,
    calibration_galvo=10.2)

microscopy.ScapeConfig.insert1(
    scape_config, skip_duplicates=True)

datapath = os.path.abspath(os.path.dirname(__file__))

h5py.get_config().default_file_mode = 'r'
#f = h5py.File(os.path.join(datapath, '../../', 'example_data/neuropal20200522/worm1_fast_run1_info.mat'))


# get session date with regular expression YYYYMMDD
date = re.search('[0-9]{8}', session_dir)
if not date:
    exit()

date_str = date.group(0)
session_date = datetime.datetime.strptime(date_str, '%Y%m%d').date()

# only detect the _info.mat files
filenames = [filename for filename in os.listdir(session_dir)
                if '_info.mat' in filename]

# insert into the table experiment.Session
session_pk = os.path.split(session_dir)[-1]
experiment.Session.insert1(
    dict(session_name=session_pk,
         session_date=session_date,
         data_directory=session_dir,
         backup_location='unknown'),
    skip_duplicates=True)

# insert into the table experiment.Scan and its part tables
for i_scan, filename in enumerate(filenames):
    
    # get the specimen name
    specimen = re.search(r'^([A-Za-z0-9]*)_', filenames[i_scan]).groups()[0]+'_'+session_pk
    
    # insert into the table experiment.Specimen
    experiment.Specimen.insert1(
    dict(specimen=specimen,
         source=source,
         species=species),
    skip_duplicates=True)  # usually turn on this arg if insert manually
    
    experiment.Session.Specimen.insert1(
    dict(session_name=session_pk, specimen=specimen),
    skip_duplicates=True)

    # load file
    f = h5py.File(os.path.join(session_dir, filename))['info']
    status = dataset_to_string(f['scanStatus'])

    scan_pk = dict(
        session_name=session_pk,specimen=specimen,
        scan_name=dataset_to_string(f['scanName']))

    # insert into the experiment.Scan table
    experiment.Scan.insert1(
        dict(**scan_pk,
             **scape_config,
             scan_filename=filename, # to be replaced by the real tiff name
             scan_note=dataset_to_string(f['experiment_notes']),
             scan_start_time=datetime.datetime.strptime(
                 dataset_to_string(f['scanStartTimeApprox']),
                 '%d-%b-%Y %H:%M:%S'),
             scan_status='Successful' if status=='scan complete!' else 'Interrupted',
             ),
        ignore_extra_fields=True,
        skip_duplicates=True)

    # insert into the part table CaliFactor
    calfactor = f['GUIcalFactors']
    experiment.Scan.CaliFactor.insert1(
        dict(**scan_pk,
             calibration_xk=dataset_to_scalar(calfactor['xK_umPerVolt'], 3),
             calibration_x=dataset_to_scalar(calfactor['x_umPerPix'], 3),
             calibration_y=dataset_to_scalar(calfactor['y_umPerPix'], 3),
             calibration_z=dataset_to_scalar(calfactor['z_umPerPix'], 3)),
        skip_duplicates=True)
