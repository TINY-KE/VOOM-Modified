+ 在tum上运行
	+ Data Preprocessing:

	python find_tum_corresponds.py
	python generate_rgbd_association.py
	python generate_detection_files.py

	+ origin version: 

	./rgbd_tum_with_ellipse ../Vocabulary/ORBvoc.txt ../Cameras/TUM2.yaml /media/robotlab/0DD416590DD41659/DATASET/TUM/TUM/rgbd_dataset_freiburg2_desk  ../Data/fr2_desk/fr2_desk.txt ../Data/fr2_desk/detections_yolov8x_seg_tum_rgbd_fr2_desk_with_ellipse.json  points fr2

	+ my version:

	./rgbd_tum_with_ellipse ../Vocabulary/ORBvoc.txt ../Cameras/TUM2.yaml /media/robotlab/0DD416590DD41659/DATASET/TUM/TUM/rgbd_dataset_freiburg2_desk  ../PythonScripts/support_files/rgbd_dataset_freiburg2_desk_associated.txt ../PythonScripts/support_files/rgbd_dataset_freiburg2_desk_detections_yolov8x_seg_with_ellipse.json  points fr2
	
+ 在icl2上运行

	./rgbd_tum_with_ellipse ../Vocabulary/ORBvoc.txt ../Cameras/ICL_NUIM_home_2.yaml /home/robotlab/dataset/ICL-NUIM/living_room_traj2n_frei_png  ../PythonScripts/support_files/living_room_traj2n_frei_png_associated.txt ../PythonScripts/support_files/living_room_traj2n_frei_png_detections_yolov8x_seg_with_ellipse.json  points iclhome2

+ 在icl0上运行

	./rgbd_tum_with_ellipse ../Vocabulary/ORBvoc.txt ../Cameras/ICL_NUIM_home_2.yaml /home/robotlab/dataset/ICL-NUIM/living_room_traj0_frei_png  ../PythonScripts/support_files/living_room_traj0_frei_png_associated.txt ../PythonScripts/support_files/living_room_traj0_frei_png_detections_yolov8x_seg_with_ellipse.json  points iclhome0

+ 在icl1上运行

	./rgbd_tum_with_ellipse ../Vocabulary/ORBvoc.txt ../Cameras/ICL_NUIM_home_2.yaml /home/robotlab/dataset/ICL-NUIM/living_room_traj1_frei_png  ../PythonScripts/support_files/living_room_traj1_frei_png_associated.txt ../PythonScripts/support_files/living_room_traj1_frei_png_detections_yolov8x_seg_with_ellipse.json  points iclhome1

+ 在replica0上运行

	./rgbd_tum_with_ellipse ../Vocabulary/ORBvoc.txt ../Cameras/replica_hotel0.yaml /home/robotlab/dataset/Replica-Dataset-results/hotel_0_640  ../PythonScripts/support_files/hotel_0_640_associated.txt ../PythonScripts/support_files/hotel_0_640_detections_yolov8x_seg_with_ellipse.json  points replicahotel0

+ 在replica1上运行

	./rgbd_tum_with_ellipse ../Vocabulary/ORBvoc.txt ../Cameras/replica_hotel0.yaml /home/robotlab/dataset/Replica-Dataset-results/hotel_0_640  ../PythonScripts/support_files/hotel_0_640_associated.txt ../PythonScripts/support_files/hotel_0_640_detections_yolov8x_seg_with_ellipse.json  points replicahotel0

+ 在replica2上运行

	./rgbd_tum_with_ellipse ../Vocabulary/ORBvoc.txt ../Cameras/replica_hotel0.yaml /home/robotlab/dataset/Replica-Dataset-results/hotel_0_640  ../PythonScripts/support_files/hotel_0_640_associated.txt ../PythonScripts/support_files/hotel_0_640_detections_yolov8x_seg_with_ellipse.json  points replicahotel0

+ 在gazebo0上运行

	./rgbd_tum_with_ellipse ../Vocabulary/ORBvoc.txt ../Cameras/self_allobject_ground_10.yaml /home/robotlab/dataset/MySimDataset/gazebo_dataset_10  ../PythonScripts/support_files/gazebo_dataset_10_associated.txt ../PythonScripts/support_files/gazebo_dataset_10_detections_yolov8x_seg_with_ellipse.json  points gazebo0

+ 在gazebo1上运行

	./rgbd_tum_with_ellipse ../Vocabulary/ORBvoc.txt ../Cameras/self_allobject_ground_10.yaml /home/robotlab/dataset/MySimDataset/gazebo_dataset_10  ../PythonScripts/support_files/gazebo_dataset_10_associated.txt ../PythonScripts/support_files/gazebo_dataset_10_detections_yolov8x_seg_with_ellipse.json  points gazebo0

+ 在gazebo2上运行

	./rgbd_tum_with_ellipse ../Vocabulary/ORBvoc.txt ../Cameras/self_allobject_ground_10.yaml /home/robotlab/dataset/MySimDataset/gazebo_dataset_10  ../PythonScripts/support_files/gazebo_dataset_10_associated.txt ../PythonScripts/support_files/gazebo_dataset_10_detections_yolov8x_seg_with_ellipse.json  points gazebo0