# Dancerail_Import

A tool written in Python to import custom charts made with DRMaker to DanceRail (Android only)

# Dependencies

* Python 3.5 or above
* JDK 8 or above

## If you're going to just download the .py files, you will also need these inside the folder:

* [apktool](https://ibotpeaches.github.io/Apktool/)
* [uber-apk-signer](https://github.com/patrickfav/uber-apk-signer)

### This tool is currently only available for Windows. I will add support for other platforms in the future.

# How to use

You will first need to make your chart with DRMaker. You can download that [here](http://www.mediafire.com/file/q5okdo6l3n2s0oo/DRMaker%28lrc4.2%29.zip "DRMaker (Mediafire)").

Yes, this IS the official download link.

_Usage: dancerail_import.py apk_file_
  
# Overview

The tool will ask you for the following:

* Song Title
* Song filename (this is both the chartfile created by DRMaker and the ogg file. **do not add the extension.**)
* Song artist
* BPM
* Duration (seconds)
* Preview time (so for example, if you want the song to start previewing at 10 seconds, you write 10)
* Difficulty number (Easy)
* Difficulty number (Normal)
* Difficulty number (Hard)
* Difficulty number (Ultra)
* Difficulty number (Master)

# TO-DO LIST

* Add multi-platform support
* Optimize for better using (I've _got_ to remove the requirement to specifiy all difficulties)
* Add jacket support
