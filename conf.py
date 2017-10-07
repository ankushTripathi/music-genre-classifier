import os

root_dir = os.getcwd();
raw_data_dir = os.path.join(os.getcwd(),"genres")
dataset_dir = os.path.join(root_dir,"dataset")
genres = [name for name in os.listdir(raw_data_dir) if os.path.isdir(os.path.join(raw_data_dir,name))]
os.environ["PATH"] += os.pathsep + "C:\Program Files (x86)\sox-14-4-2\sox.exe"