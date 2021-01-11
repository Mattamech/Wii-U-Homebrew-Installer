#Made by Lord-Giganticus and Mattamech. Please do not repost this without crediting us! :)

# Version 3.2.1

import os

Program_Location = os.getcwd()

Download_Location = input("Enter folder with downloaded files here:")
os.chdir(Download_Location)
print(os.getcwd())
input("If the folder above is not correct you will have to restart. Press enter to continue.")

if os.path.isdir('copy_to_sd') == False:
    input("copy_to_sd does not exist here! Press enter to exit and next time, enter the correct folder.")
    exit()

Save_Location = input("Enter Drive letter (ex G:) here:")
wiiu_copier = open('wiiu_copier.bat','w')
wiiu_copier.write('Xcopy /E /I copy_to_sd ')
wiiu_copier.write(Save_Location)
wiiu_copier.close()
os.system('cmd /c wiiu_copier.bat')
os.system('cmd /c del /f *.bat')

rerun = input("Do you wish to\n[1]rerun the script,\n[2]delete the copy-to-sd folder,\n[3]or just exit?\nEnter the number that matches your choice.\n")
if rerun == "1":
    os.chdir(Program_Location)
    os.system('cmd /c py Copier.py')
    exit()
elif rerun == "2":
    os.system('cmd /c RD /S /Q copy_to_sd')
    exit()
elif rerun == "3":
    exit()
else:
    input("Whoops! That wasn't supposed to happen! Press enter to exit.")
    exit()