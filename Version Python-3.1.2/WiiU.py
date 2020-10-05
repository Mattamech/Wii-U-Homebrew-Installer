import os
import shutil

Download_Location = input("Enter folder here:")
os.chdir(Download_Location)
print(os.getcwd())
input("If the folder above is not correct you will have to restart. Press enter to continue.")

wiiu_downloader = open('wiiu_downloader.bat','w')
wiiu_downloader.write('curl http://wiiubru.com/appstore/zips/homebrew_launcher.zip --output homebrew_launcher.zip\ncurl https://wiiubru.com/appstore/zips/appstore.zip --output appstore.zip\ncurl https://wiiubru.com/appstore/zips/mocha_fshax.zip --output mocha.zip\ncurl https://wiiubru.com/appstore/zips/haxchi.zip --output haxchi.zip\ncurl https://wiiubru.com/appstore/zips/cbhc.zip --output cbhc.zip\ncurl http://stahlworks.com/dev/unzip.exe --output unzip.exe')
wiiu_downloader.close()

input("Double Check that downloader.bat is now in the folder you specifyed. Press enter to continue.")

os.system('cmd /c downloader.bat')
os.system('cmd /c unzip *zip')
os.system('cmd /c del /f *.zip')
os.system('cmd /c del /f *.install')
os.system('cmd /c del /f *.png')
os.system('cmd /c del /f *.json')
os.system('cmd /c del /f *.exe')
os.system('cmd /c del /f *.bat')

os.mkdir('copy_to_sd')
shutil.copytree('cbhc', 'copy_to_sd\cbhc')
shutil.copytree('haxchi', 'copy_to_sd\haxchi')
shutil.copytree('wiiu', 'copy_to_sd\wiiu')

Save_Location = input("Enter Drive letter (ex G:) here:")
wiiu_copier = open('wiiu_copier.bat','w')
wiiu_copier.write('Xcopy /E /I copy_to_sd ')
wiiu_copier.write(Save_Location)
wiiu_copier.close()
os.system('cmd /c wiiu_copier.bat')
os.system('cmd /c RD /S /Q cbhc')
os.system('cmd /c RD /S /Q haxchi')
os.system('cmd /c RD /S /Q wiiu')
os.system('cmd /c del /f *.bat')

input("If you followed the directions correctly the files should be in the root of the sd card. Press enter to exit.")
exit()