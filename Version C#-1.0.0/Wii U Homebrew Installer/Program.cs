using Microsoft.VisualBasic;
using System.Net;
using System.Diagnostics;
using System.IO;
using System;

namespace Wii_U_Homebrew_Installer
{
    class Program
    {
        static void Main(string[] args)
        {
            using (var client = new WebClient())
                client.DownloadFile("http://wiiubru.com/appstore/zips/homebrew_launcher.zip", "homebrew_launcher.zip");
            using (var client = new WebClient())
                client.DownloadFile("https://wiiubru.com/appstore/zips/appstore.zip", "appstore.zip");
            using (var client = new WebClient())
                client.DownloadFile("https://www.wiiubru.com/appstore/zips/mocha.zip", "mocha.zip");
            using (var client = new WebClient())
                client.DownloadFile("https://wiiubru.com/appstore/zips/haxchi.zip", "haxchi.zip");
            using (var client = new WebClient())
                client.DownloadFile("https://wiiubru.com/appstore/zips/cbhc.zip", "cbhc.zip");
            using (var client = new WebClient())
                client.DownloadFile("https://mattamech.github.io/Wii-U-Homebrew-Installer/cs/Haxchi-Installer.zip", "Haxchi-Installer.zip");
            using (var client = new WebClient())
                client.DownloadFile("https://mattamech.github.io/Wii-U-Homebrew-Installer/cs/Extract.bat", "Extract.bat");
            using (var client = new WebClient())
                client.DownloadFile("https://mattamech.github.io/Wii-U-Homebrew-Installer/cs/Move.bat", "Move.bat");
            using (var client = new WebClient())
                client.DownloadFile("http://stahlworks.com/dev/unzip.exe", "unzip.exe");
            FileSystem.MkDir("Copy_to_SD");
            Environment.CurrentDirectory = Directory.GetCurrentDirectory();
            Process.Start("CMD.exe","echo hi & exit");
        }
    }
}
