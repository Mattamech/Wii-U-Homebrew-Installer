import shutil
import os

Download_Location = input("Enter folder with copy_to_sd folder here:")
os.chdir(Download_Location)
print(os.getcwd())
input("If the folder above is not correct you will have to restart. Press enter to continue.")

Save_Location = input("Enter Drive letter (ex G:) here:")
shutil.move('copy_to_sd\cbhc', Save_Location)
shutil.move('copy_to_sd\haxchi', Save_Location)
shutil.move('copy_to_sd\wiiu', Save_Location)

input("If you followed the directions correctly the files should be in the root of the sd card. Press enter to exit.")
exit()
