import open3d as o3d
pcd=o3d.io.read_point_cloud('../allply/newbase/mvsnet004_l3.ply')
o3d.visualization.draw_geometries([pcd])