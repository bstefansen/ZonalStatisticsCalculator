
# Name: ZonalStatisticsAsTable.py

# Notes -- **** Replace "Set workspace" with your working folder file path 
# Notes -- **** Replace the "n" variables with input file names
# Notes -- **** Input the dataset that defines the zones in "inZoneData”
# Notes -- **** Input desired field value and statistics parameters
# Notes -- **** Run the program in IDLE 2.7.13


# Import arcpy module
import arcpy
from arcpy import env
from arcpy.sa import *

# Set workspace
env.workspace = r" # Set workspace file path"

# Assign variables
n = [ # List of files on which to calculate zonal statistics ]
feature = n

# Check license
arcpy.CheckOutExtension("Spatial")

# Overwrite files with same name
arcpy.env.overwriteOutput = True

# Execute ZonalStatisticsAsTable
for feature in n:
    inZoneData = # Dataset that defines the zone
    zoneField = # Field that holds the values that define each zone
    inValueRaster = feature
    outTable = "_zonal_" + feature
    outZSaT = ZonalStatisticsAsTable(inZoneData, zoneField, inValueRaster, 
                                 outTable, "NODATA", " # Input statistic you want to calculate ")
    print "_zonal_" + feature + " is complete"
    




