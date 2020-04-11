C:
cd C:\
mkdir homebrew
cd C:\homebrew
mkdir sd
pause
cd C:\homebrew\sd
curl https://github.com/dimok789/homebrew_launcher/releases/download/v1.3/homebrew_launcher.v1.3.zip --output homebrew_launcher.zip
curl https://wiiubru.com/appstore/zips/appstore.zip --output appstore.zip
curl https://wiiubru.com/appstore/zips/mocha_fshax.zip --output mocha.zip
curl https://wiiubru.com/appstore/zips/haxchi.zip --output haxchi.zip
curl https://wiiubru.com/appstore/zips/cbhc.zip --output cbhc.zip
curl http://stahlworks.com/dev/unzip.exe --output unzip.exe
pause
unzip *zip
pause
del /f *.zip
del /f *.json
del /f *.install
cd C:\homebrew
pause
cd C:\homebrew\sd
del /f *.exe
pause
cd C:\homebrew
curl https://raw.githubusercontent.com/Mattamech/Wii-U-Homebrew-Installer/Version-2/Homebrew_Installer.txt --output Homebrew_Installer.txt
start C:\homebrew\Homebrew_Installer.txt
exit
