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
            Console.WriteLine("Enter the drive you want to copy the files to:");
            string drive = Console.ReadLine();
            using (FileStream fs = File.Create("xcopy.bat")) //This to line 51 are from the answer in https://social.msdn.microsoft.com/Forums/vstudio/en-US/41a153ec-e9bc-4a85-a2b4-9d55dc00fef8/creating-a-batch-file-using-c-to-update-a-database-in-sql-server-2005?forum=netfxbcl
                fs.Close();
            using (StreamWriter sw = new StreamWriter("xcopy.bat"))
                sw.WriteLine("/c cd Copy_to_SD & xcopy /E /I wiiu " + drive + " & xcopy /E /I haxchi " + drive + " & xcopy /E /I cbhc " + drive + " & exit");
            Environment.CurrentDirectory = Directory.GetCurrentDirectory();
            Process process = Process.Start("CMD.exe","/c start xcopy.bat");
            process.WaitForExit();
            Console.WriteLine("Complete. Exiting.");
            Thread.Sleep(5000);
            Environment.Exit(0);
        }
    }
}
