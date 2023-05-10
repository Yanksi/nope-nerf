from pose_utils import load_colmap_data, save_poses

dataset_dir = "data/DAVIS/train"

poses, pts3d, perm, names = load_colmap_data(dataset_dir)
save_poses(dataset_dir, poses, pts3d, perm, names)