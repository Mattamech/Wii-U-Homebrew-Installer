import shutil
import os

Download_Location = input("Enter folder with downloaded files here:")
os.chdir(Download_Location)
print(os.getcwd())
input("If the folder above is not correct you will have to restart. Press enter to continue.")

Save_Location = input("Enter Drive letter (ex G:) here:")
wiiu_copier = open('wiiu_copier.bat','w')
wiiu_copier.write('Xcopy /E /I copy_to_sd ')
wiiu_copier.write(Save_Location)
wiiu_copier.close()
os.system('cmd /c wiiu_copier.bat')
os.system('cmd /c del /f *.bat')

input("If you followed the directions correctly the files should be in the root of the sd card. Press enter to exit.")
exit()
