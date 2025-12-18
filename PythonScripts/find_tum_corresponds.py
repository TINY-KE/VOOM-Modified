import numpy as np
import json
import os
import glob
import yaml
from yaml.loader import SafeLoader

# data_name = "rgbd_dataset_freiburg2_desk"
# data_path = "/media/robotlab/0DD416590DD41659/DATASET/TUM/TUM" + '/' + data_name

# data_name = "living_room_traj2n_frei_png"
# data_path = "/home/robotlab/dataset/ICL-NUIM" + '/' + data_name

# # configs/replica_hotel0.yaml  \
# # /home/robotlab/dataset/Replica-Dataset-results/hotel_0_640 
# data_name = "hotel_0_640"
# data_path = "/home/robotlab/dataset/Replica-Dataset-results/" + '/' + data_name

# configs/self_allobject_ground_10.yaml  \
# /home/robotlab/dataset/MySimDataset/gazebo_dataset_10 \
data_name = "gazebo_dataset_10"
data_path = "/home/robotlab/dataset/MySimDataset" + '/' + data_name

# Open the file and load the file
rgb_files = sorted(filter(os.path.isfile, glob.glob(
    data_path + '/rgb/' + '*.png')))
rgb_filenames = []
for file in rgb_files:
    head, filename = os.path.split(file)
    filename = filename[:-4]
    rgb_filenames.append(float(filename))
print('r',len(rgb_filenames))

depth_files = sorted(filter(os.path.isfile, glob.glob(
    data_path + '/depth/' + '*.png')))
depth_filenames = []
for file in depth_files:
    head, filename = os.path.split(file)
    filename = filename[:-4]
    depth_filenames.append(float(filename))
print('d',len(depth_filenames))

corres_depth = []
j = 0
for i in range(len(rgb_filenames)):
    rgb_time = rgb_filenames[i]
    delta_time_min = 10
    while j < len(depth_filenames) and abs(rgb_time - depth_filenames[j]) < delta_time_min:
        delta_time_min = abs(rgb_time - depth_filenames[j])
        j = j+1
    j = j - 1
    print(rgb_time, depth_filenames[j])
    corres_depth.append(depth_files[j])

# gt = np.loadtxt(data_path + '/groundtruth.txt', delimiter=' ')
# timestamp_gt = list(np.array(gt)[:, 0])
# #print(len(timestamp_gt))
# corres_gt = []
# j = 0
# for i in range(len(rgb_filenames)):
#     rgb_time = rgb_filenames[i]
#     delta_time_min = 100
#     while j < len(timestamp_gt) and abs(rgb_time - timestamp_gt[j]) < delta_time_min:
#         delta_time_min = abs(rgb_time - timestamp_gt[j])
#         j = j+1
#     #j = j - 1
#     #print(rgb_time, timestamp_gt[j - 1])
#     corres_gt.append(list(gt[j - 1]))

# dict_all = {"rgb": rgb_files, "depth": depth_files, "gt": corres_gt}
dict_all = {"rgb": rgb_files, "depth": depth_files}
with open('support_files/' + data_name + '.json', 'w') as outfile:
    json.dump(dict_all, outfile)