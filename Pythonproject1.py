#import system module
import arcpy

#set workspace environment
arcpy.env.workspace = r"C:\Users\Student\Downloads\sample_data1"

#Local variables
output = arcpy.GetParameterAsText(0)
out_coor_system = arcpy.GetParameterAsText(1)
output1 = arcpy.GetParameterAsText(2)


fclist = arcpy.ListFeatureClasses()
print fclist

#Create file geodatabase
arcpy.CreateFileGDB_management(arcpy.env.workspace,output)

#Set projection and clip shapefiles
for fc in fclist:
    l=fc.replace(".shp","_np.shp")
    arcpy.Project_management(fc,l,out_coor_system)
    b=l.replace("_np.shp","_clipnp")
    arcpy.Clip_analysis(fc,output1,"C:\\Users\\Student\\Downloads\\sample_data1\\" +output +".gdb\\"+b)
                        
