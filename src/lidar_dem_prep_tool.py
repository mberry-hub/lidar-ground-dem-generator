import arcpy

arcpy.env.overwriteOutput = True
arcpy.CheckOutExtension("3D")

# Inputs
input_laz_folder = r"D:\GISData\LiDAR\Everglades\LAZ"
output_las_folder = r"D:\GISData\LiDAR\Everglades\LAS"
output_las_dataset = r"D:\GISData\LiDAR\Everglades\Everglades_LiDAR.lasd"
output_dem = r"D:\GISData\LiDAR\Everglades\Everglades_DEM.tif"

# User settings
dem_resolution = 1
ground_method = "STANDARD"   # CONSERVATIVE / STANDARD / AGGRESSIVE

# Convert LAZ to LAS
arcpy.conversion.ConvertLas(
    in_las=input_laz_folder,
    target_folder=output_las_folder,
    compression="NO_COMPRESSION"
)

# Create LAS Dataset
arcpy.management.CreateLasDataset(
    input=output_las_folder,
    out_las_dataset=output_las_dataset,
    compute_stats="COMPUTE_STATS"
)

# Classify ground
arcpy.ddd.ClassifyLasGround(
    in_las_dataset=output_las_dataset,
    method=ground_method
)

# Use only ground points
arcpy.management.MakeLasDatasetLayer(
    in_las_dataset=output_las_dataset,
    out_layer="ground_lidar",
    class_code="2"
)

# Convert ground points to DEM
arcpy.conversion.LasDatasetToRaster(
    in_las_dataset="ground_lidar",
    out_raster=output_dem,
    value_field="ELEVATION",
    interpolation_type="BINNING AVERAGE LINEAR",
    data_type="FLOAT",
    sampling_type="CELLSIZE",
    sampling_value=dem_resolution
)

print("Ground DEM created successfully.")