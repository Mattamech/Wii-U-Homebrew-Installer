using System;
using System.Threading;
using System.Diagnostics;
using System.IO;

namespace Copier
{
    class Program
    {
        static void Main(string[] args)
        {
            Environment.CurrentDirectory = Directory.GetCurrentDirectory();
            Console.WriteLine("Enter the drive you want to copy the files to:");
            string drive = Console.ReadLine();
            string strCmdText;
            strCmdText = "/c cd Copy_to_SD & xcopy /E /I wiiu " + drive + " & xcopy /E /I haxchi " + drive + " & xcopy /E /I cbhc " + drive + " & exit";
            Process.Start("CMD.exe", strCmdText);
            Console.WriteLine("Complete. Exiting.");
            Thread.Sleep(5000);
            Environment.Exit(0);
        }
    }
}
