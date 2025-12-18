import numpy as np
import json
import matplotlib.pyplot as plt
import os

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

filenames = json.load(open('support_files/' + data_name + '.json'))
rgbs = filenames['rgb']
depths = filenames['depth']

# ---- 修复：按数值排序 ----
def key_func(path):
    base = os.path.basename(path)
    num = os.path.splitext(base)[0]
    # return int(num)
    return float(num)

rgbs = sorted(rgbs, key=key_func)
depths = sorted(depths, key=key_func)

# ---- 写入 associated 文件 ----
out_path = 'support_files/' + data_name + '_associated.txt'
with open(out_path, 'w') as f:
    for rgb, depth in zip(rgbs, depths):
        filename_rgb = os.path.basename(rgb)
        time_rgb = filename_rgb[:-4]

        filename_depth = os.path.basename(depth)
        time_depth = filename_depth[:-4]

        line = f"{time_rgb} rgb/{filename_rgb} {time_depth} depth/{filename_depth}\n"
        f.write(line)











# filenames = json.load(open('support_files/' + data_name + '.json'))
# rgbs = filenames['rgb']
# depths = filenames['depth']
# f = open('support_files/' + data_name + '_associated.txt','a')
# for rgb, depth in zip(rgbs, depths):
#     _, filename_rgb = os.path.split(rgb)
#     time_rgb = filename_rgb[:-4]
#     filename_rgb = 'rgb/' + filename_rgb
#     _, filename_depth = os.path.split(depth)
#     time_depth = filename_depth[:-4]
#     filename_depth = 'depth/' + filename_depth
#     line = time_rgb + ' ' + filename_rgb + ' ' + time_depth + ' ' + filename_depth + '\n'
#     f.write(line)
# '''for i in range(1508):
#     time = (i+1)/3.0
#     line = str(time) + ' rgb/' + str(i+1) + '.png ' + str(time) + ' depth/' + str(i+1) + '.png' + '\n'
#     f.write(line)'''
# f.close()