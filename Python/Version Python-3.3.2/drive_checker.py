def getdrives() -> list:
    import string
    from ctypes import windll
    drives = [] # From https://stackoverflow.com/a/827398
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            if letter.endswith(':') == False:
                letter = letter+':'
            drives.append(letter)
        bitmask >>= 1
    return drives

def checkdrives(drives:list) -> list:
    import os
    current_drive = os.path.splitdrive(os.getcwd())
    current_drive = current_drive[0]
    drives.remove(current_drive)
    entry = int(0)
    drives_removed = int(0)
    while entry < len(drives):
        try:
            os.chdir(drives[entry])
            os.chdir(current_drive)
        except:
            print(drives[entry],'is a bad drive. Removing from your list.')
            bad_drive = drives[entry]
            drives.remove(bad_drive)
            drives_removed += 1
            entry = entry - 1
        entry += 1
    print(drives_removed,"drive(s) were removed due to being bad.")
    drives.append(current_drive)
    drives.sort()
    return drives

def drivecheck(drive:str) -> bool:
    import os
    try:
        og_drive = os.path.splitdrive(os.getcwd())
        og_drive = og_drive[0]
        os.chdir(drive)
        os.chdir(og_drive)
        return True
    except:
        return False

def drive_folder_check(drive:str, folder:str) -> bool:
    import os
    os.chdir(drive)
    if os.path.isdir(folder) == True:
        return True
    else:
        return False