# LiDAR DEM Prep Tool

ArcPy automation workflow for converting raw LAZ LiDAR tiles into ground-classified bare-earth DEMs with configurable output resolution in ArcGIS Pro.

---

## Overview

This project automates a common LiDAR preprocessing workflow used in geospatial analysis, terrain modeling, and hydrologic applications.

The script converts compressed LiDAR point cloud data (`.laz`) into standard LAS format, creates a LAS Dataset, classifies ground points, filters to ground-only returns, and generates a bare-earth Digital Elevation Model (DEM).

This workflow is useful for preparing LiDAR data for:

- hydrologic analysis
- watershed delineation
- terrain modeling
- slope analysis
- surface analysis
- GIS preprocessing workflows

---

## Workflow

```text
Raw LAZ Files
    ↓
Convert LAZ to LAS
    ↓
Create LAS Dataset (.lasd)
    ↓
Compute LAS Statistics
    ↓
Classify Ground Points
    ↓
Filter Ground Points (Class 2)
    ↓
Generate Bare-Earth DEM
```

---

## Features

- Converts compressed `.laz` LiDAR files to `.las`
- Creates ArcGIS Pro LAS Dataset (`.lasd`)
- Automatically classifies ground points
- Filters to ground-only LiDAR returns
- Generates bare-earth DEM raster
- User-configurable DEM output resolution
- Adjustable ground classification method

---

## Technologies Used

- Python
- ArcPy
- ArcGIS Pro
- 3D Analyst Extension
- LiDAR / LAS datasets

---

## Script Parameters

Edit these variables directly in the script:

```python
input_laz_folder = r"D:\GISData\LiDAR\Everglades\LAZ"
output_las_folder = r"D:\GISData\LiDAR\Everglades\LAS"
output_las_dataset = r"D:\GISData\LiDAR\Everglades\Everglades_LiDAR.lasd"
output_dem = r"D:\GISData\LiDAR\Everglades\Everglades_DEM.tif"

dem_resolution = 1
ground_method = "STANDARD"
```

---

## Ground Classification Methods

Supported options:

```python
"CONSERVATIVE"
"STANDARD"
"AGGRESSIVE"
```

### Conservative
More strict classification. Reduces false positives but may miss some ground points.

### Standard
Balanced default classification.

### Aggressive
More permissive classification. Captures more ground but may incorrectly classify some non-ground features.

---

## DEM Resolution

Output resolution is user configurable:

Examples:

```python
dem_resolution = 0.5
```

Creates:

0.5 meter DEM

```python
dem_resolution = 1
```

Creates:

1 meter DEM

```python
dem_resolution = 5
```

Creates:

5 meter DEM

Resolution units depend on the LAS dataset coordinate system.

---

## Example Use Cases

This workflow can support:

- watershed delineation
- flood modeling
- terrain analysis
- hydrologic preprocessing
- environmental GIS workflows
- DEM generation from airborne LiDAR

---

## Example ArcPy Workflow

The script uses:

```python
arcpy.conversion.ConvertLas()
arcpy.management.CreateLasDataset()
arcpy.ddd.ClassifyLasGround()
arcpy.management.MakeLasDatasetLayer()
arcpy.conversion.LasDatasetToRaster()
```

---

## Output Products

Generated outputs include:

- `.las` point cloud files
- `.lasd` LAS dataset
- ground-classified LiDAR layer
- bare-earth DEM raster

---

## Notes

Large LiDAR datasets are intentionally excluded from this repository.

Recommended data sources:

- USGS 3DEP
- OpenTopography
- NOAA Digital Coast

---

## Future Improvements

Potential enhancements:

- ArcGIS Pro script tool version
- GUI parameter inputs
- DSM generation option
- CHM generation
- automatic coordinate system validation
- batch project processing

---

## Author

Matt Berry

GIS / Geospatial Programming Portfolio Project
