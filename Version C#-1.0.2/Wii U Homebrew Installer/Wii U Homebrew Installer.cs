using System.Net;
using System.Diagnostics;
using System.IO;
using System;
using System.Threading;

namespace Wii_U_Homebrew_Installer
{
    class Program
    {
        static void Main(string[] args)
        {
            if (Directory.Exists("Copy_to_SD"))
            {
                Console.WriteLine("Copy_to_SD folder dectected. Jumping to Copier code.");
                Thread.Sleep(2000);
                goto Copier;
            } else
            {
                //pass
            }
            Console.WriteLine("Downloading files.");
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
                client.DownloadFile("https://mattamech.github.io/Wii-U-Homebrew-Installer/cs/Haxchi-Installer.tar.gz", "Haxchi-Installer.tar.gz");
            using (var client = new WebClient())
                client.DownloadFile("https://mattamech.github.io/Wii-U-Homebrew-Installer/cs/Extract.bat", "Extract.bat");
            using (var client = new WebClient())
                client.DownloadFile("https://mattamech.github.io/Wii-U-Homebrew-Installer/cs/Move.bat", "Move.bat");
            using (var client = new WebClient())
                client.DownloadFile("http://stahlworks.com/dev/unzip.exe", "unzip.exe");
            Directory.CreateDirectory("Copy_to_SD");
            Environment.CurrentDirectory = Directory.GetCurrentDirectory();
            Console.WriteLine("Running .bat files.");
            Process.Start("CMD.exe", "/c start Extract.bat").WaitForExit();
            Copier:
            Environment.CurrentDirectory = Directory.GetCurrentDirectory();
            Console.WriteLine("Enter the drive you want to copy the files to:");
            string drive = Console.ReadLine();
            Process process = Process.Start("CMD.exe", "/c robocopy /E Copy_to_SD \"" + drive + "\"");
            process.WaitForExit();
            Console.WriteLine("Complete. Exiting.");
            Thread.Sleep(5000);
            Environment.Exit(0);
        }
    }
}
