import os
import subprocess


def convertWMAtoMP3(directory):
    #converts wma to mp3
   
    conv_files = []  # list to store file paths

    for root, dirs, files in os.walk(directory): #loops through all files and subdirectorys in target
        for file in files: 
            if file.endswith('.wma'): #looks for wma files
                file_path = os.path.join(root, file) #gets file path
                conv_files.append(os.path.abspath(file_path)) #adds file path to list
                file_basename, file_extension = os.path.splitext(file) #gets file name and extension
                file_name_without_extension = file_basename 
                mp3_file = root+"\\"+file_name_without_extension +".mp3" #gets new file name
                #runs the ffmpeg cmd tool . Note ffmpeg needs installing on PATH 
                subprocess.run(['ffmpeg -i ' + file_path + ' -acodec libmp3lame -qscale:a 2 ' + mp3_file])


              
          
             
    print("************Process Complete************************************")
    for item in conv_files: #loops through items in list and prints
        print(item)


def convertM4PtoMP3(directory):
    #converts mp4 to mp3
    
    conv_files = []  # list to store file paths

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.m4v'):
                file_path = os.path.join(root, file)
                conv_files.append(os.path.abspath(file_path))
                file_basename, file_extension = os.path.splitext(file)
                file_name_without_extension = file_basename
                mp3_file = root+"\\"+file_name_without_extension +".mp3"
                subprocess.call(["ffmpeg", "-i", file_path, "-vn", "-acodec libmp3lame -qscale:a", "2", mp3_file])
              
             
   
          
             
    print("************Process Complete************************************")
    for item in conv_files:
        print(item)

def deleteNonMp3(directory): #deletes any non mp3 files in directory

    conv_files = []  # list to store file paths

    for root, dirs, files in os.walk(directory):
        for file in files:
            if not file.endswith('.mp3'): # note if this is changed to .xxx it will delete other file types
                    if not file.endswith('.mp3'):
                        conv_files.append(file)
                        file_path = os.path.join(root, file)
                        os.remove(file_path)

    print("************Process Delete************************************")
    for item in conv_files:
        print(item)

    
                
            
             




convert = input("What file type do you want to convert to MP3 ? WMA or M4V? Enter wma or m4V or delete to delete non mp3")
convert = convert.upper()
directory = input("input your directory") 
if convert=="WMA":
    convertWMAtoMP3(directory)
elif convert=="M4V":
    convertM4PtoMP3(directory)
elif convert=="DELETE":
    deleteNonMp3(directory)
else:
    print("Please enter a valid format")
