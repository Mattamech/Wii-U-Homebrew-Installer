cd C:\homebrew\sd
del /f *.exe
del /f *.bat
pause
cd C:\homebrew
curl https://raw.githubusercontent.com/Mattamech/Wii-U-Homebrew-Installer/master/Homebrew_Installer_Part_5.txt --output Homebrew_Installer_Part_5.txt
start C:\homebrew\Homebrew_Installer_Part_5.txt
exit
