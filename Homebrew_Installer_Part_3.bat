unzip *zip
pause
del /f *.zip
del /f *.json
del /f *.install
cd C:\homebrew
curl https://raw.githubusercontent.com/Mattamech/Wii-U-Homebrew-Installer/master/Homebrew_Installer_Part_4.bat --output Homebrew_Installer_Part_4.bat
start C:\homebrew\Homebrew_Installer_Part_4.bat
exit
