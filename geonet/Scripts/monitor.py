
import glob # Unix style pathname pattern expansion
import os # Miscellaneous operating system interfaces

 
# Directory where you have the GOES-16 Files
dirname = '/home/usuario/Escritorio/BELEN/geonet/GOES_16_Samples/'
 
# Put all file names on the directory in a list
G16_images = []
for filename in sorted(glob.glob(dirname+'OR_ABI-L2-CMIPF-M3C*.nc')):
	G16_images.append(filename)


# If the log file doesn't exist yet, create one
file = open('/home/usuario/Escritorio/BELEN/geonet/Output/G16_Log.txt', 'a')
file.close()
 
# Put all file names on the log in a list
log = []
with open('/home/usuario/Escritorio/BELEN/geonet/Output/G16_Log.txt') as f:
	log = f.readlines()

# Remove the line feed
log = [x.strip() for x in log]



 
# Compare the directory list with the file list
# Loop through all files in the directory
for x in G16_images:
	if x not in log:
		os.system("/home/usuario/anaconda3/envs/goes/bin/python" + " " + "/home/usuario/Escritorio/BELEN/geonet/Scripts/Tutorial10.py" + " " + x)

        #os.system("//home//usuario//anaconda3//envs//goes//bin//python" + "\"//home//usuario//Escritorio//BELEN//geonet//Scripts//Tutorial10.py\"" + " " + "\"" + x.replace('\\','\\\\') + "\"")


# In[6]:




