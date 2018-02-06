import os
from shutil import copy, copy2 #Specifically to copy assets
import glob #So I can copy more than one

def addSong(filename):
    foldername = os.path.splitext(os.path.basename(filename))[0] #Gets folder name for decompiled APK
    songlist = foldername +  "/assets/songlist.drf" #Finds the songlist to modify

    song = input("Song title: ")
    songfile = input("Filename (without extension): ")
    artist = input("Song artist: ")
    bpm = str(int(input("BPM: ")))
    duration = str(int(input("Duration (in seconds): ")))
    preview = str(float(input("Preview time (in seconds): ")))
    diff_easy = str(float(input("Difficulty (Easy) (Write 0 if no chart): ")))
    diff_normal = str(float(input("Difficulty (Normal) (Write 0 if no chart): ")))        
    diff_hard = str(float(input("Difficulty (Hard) (Write 0 if no chart): ")))
    diff_ultra = str(float(input("Difficulty (Ultra) (Write 0 if no chart): ")))
    diff_master = str(float(input("Difficulty (Master) (Write 0 if no chart): ")))


    i = 10128 #Last known Song ID, I swear this isn't a magic number please don't hit me :(
    with open(songlist, "r") as s: #Reads the songlist flle
        for line in s:
            if str(i) in line: #Finds Song ID, if it exists, adds one
                i += 1
        with open(songlist, "a") as s: #Weeeeeeeeeeelcome to whatever this format is!
           s.write("\n\
<" + str(i) + ">	<" + song + ">					<" + artist + ">		<" + songfile + ">				<" + bpm + ">	<" + duration + ">	<" + preview + ">	<E:" + diff_easy + ">	<N:" + diff_normal + ">	<H:" + diff_hard + ">	<U:" + diff_ultra + ">	<M:" + diff_master + ">	<" + artist + ">					<><><><><>")

    copy("FILES/" + songfile + ".ogg", foldername + "/assets/ogg2/" + songfile + ".ogg")
    charts = glob.iglob(os.path.join('', "*.drb")) #Gets all of the chart files
    for file in charts:
        if os.path.isfile(file):
            copy2("FILES/" + file, foldername + "/assets/bitmap2/")
