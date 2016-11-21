# Name: exportToShapefile.py
# Purpose: Export a geodatabase feature class to a shapefile, include domain and subtype descriptions

# Import system modules
import arcpy
from arcpy import env
import os
import sys
env.transferDomains = True

source_db = "D:/data/Geodatabase.gdb"
out_folder = "D:/data/shapefiles"


def listFcsInGDB():
    arcpy.env.workspace = source_db
    print '-- Processing ', arcpy.env.workspace
    fcs = []
    for fds in arcpy.ListDatasets('','feature') + ['']:
        for fc in arcpy.ListFeatureClasses('','',fds):
            fcs.append(os.path.join(fds, fc))
    return fcs


fcs = listFcsInGDB()
for fc in fcs:
	print "--", fc
	inFeatures = source_db + "/" + fc
	outName = fc
	arcpy.conversion.FeatureClassToFeatureClass(inFeatures, out_folder, outName)