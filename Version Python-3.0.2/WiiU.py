import wget
from shutil import copyfile
import os
import shutil

Download_Location = input("Enter folder here:")
os.chdir(Download_Location)
print(os.getcwd())
input("If the folder above is not correct you will have to restart. Press enter to continue.")

wget.download('https://mattamech.github.io/Wii-U-Homebrew-Installer/docs/downloader.bat', 'downloader.bat')

input("Double Check that downloader.bat is now in the folder you specifyed. Press enter to continue.")

os.system('cmd /c downloader.bat')
os.system('cmd /c unzip *zip')
os.system('cmd /c del /f *.zip')
os.system('cmd /c del /f *.install')
os.system('cmd /c del /f *.png')
os.system('cmd /c del /f *.json')
os.system('cmd /c del /f *.exe')
wget.download('https://mattamech.github.io/Wii-U-Homebrew-Installer/docs/copier.bat', 'copier.bat')
os.system('cmd /c del /f *.bat')

Save_Location = input("Enter a folder NOT created yet (EX: copy_to_sd) here:")
shutil.copytree(Download_Location, Save_Location)

input("If you followed the directions correctly the files should be in the root of the sd card. Press enter to exit.")
exit()