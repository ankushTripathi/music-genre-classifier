import os
import subprocess
import conf
from scipy.io import wavfile as wav
import scipy
import numpy as np

conf = reload(conf)
genres = conf.genres
root_dir = conf.root_dir
raw_data_dir = conf.raw_data_dir
dataset_dir = conf.dataset_dir

CREATE_NO_WINDOW = 0x08000000

def create_dataset_dirs():
    for genre in genres:
        if os.path.exists(os.path.join(dataset_dir,genre)):
            print("dataset already exists")
            return 0
        else:
            os.makedirs(os.path.join(dataset_dir,genre))
    return 1


def convert_files_to_wavfiles():
    for genre in genres:
        os.chdir(os.path.join(raw_data_dir,genre))
        for i in range(0,100):
            output_path = os.path.join(os.path.join(dataset_dir,genre),"%s.%05d.wav"%(genre,i))
            cmd = "sox %s.%05d.au %s"%(genre,i,output_path)
            print(cmd)
            subprocess.call(cmd,creationflags=CREATE_NO_WINDOW)
            print("executed")
        
    print("conversion complete")


def create_fft(fn):
    rate,data = wav.read(fn)
    fft_features = abs(scipy.fft(data)[:1000])
    base_fn,ext = os.path.splitext(fn)
    data_fn = base_fn+".fft"
    np.save(data_fn,fft_features)



def process():
    if(create_dataset_dirs()):
        convert_files_to_wavfiles()
        os.chdir(root_dir)
        print("dataset prepared")
        
    print("cacheing fft files")
    for genre in genres:
        os.chdir(os.path.join(raw_data_dir,genre))
        for i in range(0,100):
            base_fn = os.path.join(os.path.join(dataset_dir,genre),"%s.%05d"%(genre,i))
            fft_file = base_fn+".fft.npy"
            if(os.path.exists(fft_file)):
                print("fft features already cached")
                return
            else:
                fn = base_fn+".wav"
                create_fft(fn)
                print("%s saved!"%fft_file)
                
    print("fft files saved")