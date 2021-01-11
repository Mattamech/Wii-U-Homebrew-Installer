#Made by Lord-Giganticus and Mattamech. Please do not repost this without crediting us! :)
import os
import shutil
Version = 3.3.1

class error: # error code is from https://gist.github.com/Lord-Giganticus/db95058abbd54b198061902a4f6b6d7c
  def problem(x:int, y:int):
    if y == 0:
      print("There was a input error on line",str(x)+'.')
    elif y != 0 and y > 0:
      print('There was a error somewhere between line',str(x),'and line',str(y)+'.')
    elif y != 0 and y < 0:
      print('y is less than 0! It is set to',str(y),'and x is set to',str(x)+'. Please inform the author that this has occured!')
    input('Press enter to exit.')
    exit()
class main:
    def WiiU():
        try:
            Download_Location = input("Enter folder here:")
            os.chdir(Download_Location)
            print(os.getcwd())
            input("If the folder above is not correct you will have to restart. Press enter to continue.")

            wiiu_downloader = open('wiiu_downloader.bat','w')
            wiiu_downloader.write('curl http://wiiubru.com/appstore/zips/homebrew_launcher.zip --output homebrew_launcher.zip\n')
            wiiu_downloader.write('curl https://wiiubru.com/appstore/zips/appstore.zip --output appstore.zip\n')
            wiiu_downloader.write('curl https://wiiubru.com/appstore/zips/mocha_fshax.zip --output mocha.zip\n')
            wiiu_downloader.write('curl https://wiiubru.com/appstore/zips/haxchi.zip --output haxchi.zip\n')
            wiiu_downloader.write('curl https://wiiubru.com/appstore/zips/cbhc.zip --output cbhc.zip\n')
            wiiu_downloader.write('curl http://stahlworks.com/dev/unzip.exe --output unzip.exe')
            wiiu_downloader.close()

            input("Double Check that wiiu_downloader.bat is now in the folder you specifyed. Press enter to continue.")

            os.system('cmd /c wiiu_downloader.bat')
            os.system('cmd /c unzip *zip')
            os.system('cmd /c del /f *.zip')
            os.system('cmd /c del /f *.install')
            os.system('cmd /c del /f *.png')
            os.system('cmd /c del /f *.json')
            os.system('cmd /c del /f *.exe')
            os.system('cmd /c del /f *.bat')

            if os.path.isdir('copy_to_sd') == True:
                os.chdir('copy_to_sd')
                os.system('cmd /c RD /S /Q cbhc')
                os.system('cmd /c RD /S /Q haxchi')
                os.system('cmd /c RD /S /Q wiiu')
                os.chdir(Download_Location)
                shutil.copytree('cbhc', 'copy_to_sd\cbhc')
                shutil.copytree('haxchi', 'copy_to_sd\haxchi')
                shutil.copytree('wiiu', 'copy_to_sd\wiiu')
            else:
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
        except:
            error.problem(19, 68)
    def Copier():
        try:
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
        except:
            error.problem(73, 88)
    def Complete():
        try:
            input("Complete. Press enter to exit.")
            exit()
        except:
            error.problem(93, 95)

Choice = int(input('Enter a number corresponding to which program you wish to run.\n[1]WiiU.py\n[2]Copier.py\n'))
if Choice == 1:
    main.WiiU()
    main.Complete()
elif Choice == 2:
    main.Copier()
    main.Complete()
else:
    error.problem(99, 0)