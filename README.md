# LiDAR DEM Prep Tool

ArcPy automation workflow for converting raw LAZ LiDAR files into ground-classified bare-earth DEMs in ArcGIS Pro.

## Overview

This project automates a LiDAR preprocessing workflow for terrain analysis. The script converts compressed LAZ files to LAS, creates a LAS dataset, classifies ground points, filters to ground-only returns, and generates a DEM with user-defined resolution.

## Workflow

```text
LAZ → LAS → LAS Dataset → Ground Classification → Ground Filter → DEM
```

## Features

- LAZ to LAS conversion
- LAS dataset creation
- automated ground classification
- configurable DEM resolution
- bare-earth DEM generation

## Requirements

- ArcGIS Pro
- ArcPy
- 3D Analyst Extension

## Technologies

- Python
- ArcPy
- ArcGIS Pro
- LiDAR

## Usage

Edit the input paths and settings in:

```python
src/lidar_dem_prep_tool.py
```

Example:

```python
dem_resolution = 1
ground_method = "STANDARD"
```

Then run the script 

## Sample Output

(Add screenshots here)

```markdown
![DEM Output]([docs/screenshots/dem_output.png](https://github.com/mberry-hub/lidar-ground-dem-generator/blob/main/docs/screenshots/hillshade.png))
```

## Future Improvements

- ArcGIS script tool version
- GUI parameters
- DSM generation
- batch processing

## Author

Matt Berry
