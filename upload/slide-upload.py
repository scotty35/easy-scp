import os
import subprocess
from time import sleep
															#written by someone who has never used python (sorry about the mess)
#these variables are mostly not used later in the program even tho these locations are
#path from the image folder
path=r'C:\Users\SSEL-SOC-01\Desktop\upload'
#ip address of the pi
ip='153.90.120.213'
#path to pi's image folder
pith=r"/home/pi/Desktop/slideshow/images"

subprocess.run('cls', shell=True)

sleep(0.5)
print("\n\nPlace the images you wish to upload in the upload folder on the Desktop")
input("and push enter when done\n\n")

for filename in os.listdir(path):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        print(filename)
        print("connecting to pi...")
        subprocess.run(r"scp C:\Users\SSEL-SOC-01\Desktop\upload\%s pi@153.90.120.213:/home/pi/Desktop/slideshow/images" % filename)
        os.system(r"move /y C:\Users\SSEL-SOC-01\Desktop\upload\%s C:\Users\SSEL-SOC-01\Desktop\upload\uploaded" % filename)

    else:
        continue

input("press enter to exit program")
