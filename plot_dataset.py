import os
import conf
import matplotlib.pyplot as plt

conf = reload(conf)
genres = conf.genres
root_dir = conf.root_dir
raw_data_dir = conf.dir
dataset_dir = conf.dataset_dir

plt.close('all')

sets = {
    genre : {""}
    for genre in genres
    }

for genre in genres:
    os.chdir(os.path.join(dataset_dir,genre))
    for i in range(3):
        

f, subs = plt.subplots(10,3,sharex='col',sharey='row')
