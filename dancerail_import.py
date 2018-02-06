import sys 
from subprocess import run, call
import os
from addSong import addSong
from shutil import move, rmtree

print("\n\
#=========================#\n\
#                         #\n\
#  DanceRail Song Import  #\n\
#                         #\n\
#=========================#\n\
\n\
NOTE: You must have apktool on the same folder as this file.\n\
")

try:
    filename = str(sys.argv[1]) #Read first argument, which has to be the APK file
    if ".apk" not in filename: #Check if file is an APK
        print("Error: not an APK file")
        quit()
except IndexError:
    print("Usage: dancerail_import.py <APK file>")
    quit()

isDecompiled = False

if(os.path.isdir(os.path.splitext(os.path.basename(filename))[0])): #Checks if APK directory has already been created
    print("APK already decompiled. Skipping decompilation.")
    isDecompiled = True

if isDecompiled == False:    
    try:    
        run(["java", "-jar", "apktool.jar", "d", filename], check=True) #Decompiles APK
    except Exception:
        print("\nSomething went wrong. Please check that all binaries are placed correctly.") #Whoopsie
        quit()

print("\n")
addSong(filename)
addMore = True
while addMore == True:
    choice = int(input("\nDo you want to add another song?\n1. Yes\nOther. No\n>> "))
    if choice == 1:
        print("\n")
        addSong(filename)
    else:
        addMore = False

print("\nRebuilding APK...")
os.makedirs("unsigned")

try:
    run(["java", "-jar", "apktool.jar", "b", "-o", "unsigned/mod_unsigned_" + filename, os.path.splitext(os.path.basename(filename))[0]], check=True)
except Exception:
    print("Something went wrong while recompiling the APK. Make sure you have the correct version of apktool and a compatible JDK.")
    quit()

print("Signing APK...")

try:
    os.system("java -jar sign.jar -a unsigned --out signed") #"run()" did NOT want to work with me here. It did not. I don't know why. Fuck you run().
    move("signed/mod_unsigned_" + os.path.splitext(os.path.basename(filename))[0] + "-aligned-debugSigned.apk", "signed/signed_" + filename)
    rmtree("unsigned")
    rmtree(os.path.splitext(os.path.basename(filename))[0])
    rmtree("__pycache__")
except Exception:
    print("Something went wrong while signing the APK. Make sure you have a compatible JDK. (Minimum required: JDK 8)")
    quit()

print("Finished! Your signed, modified APK is inside the \"signed\" folder.")
