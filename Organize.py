from cgi import print_form
from distutils import text_file
from hashlib import new
import os
from re import I
import turtle
import shutil
   
def move(location,i,text,list):
    text_path = os.path.join(location,text)
    file_loc = location + "/" + list[i]
    try: #Ingnores the error if there is already a file
        os.mkdir(text_path)
        print(text + " directory has been created")
    except OSError:
        pass
    shutil.move(file_loc,text_path)   



def main():
    print("Welcome to my auto sorter for your files")
    while 1:
        print("__________________________________________________________________________")
        print("Enter the directory you would like sorted and the program will do the rest")
        location = input()
        if(location == "exit" or location == "close" or location == "Close" or location == "Exit"):
            break   

        file_names = ["Text_Files","Programming_Files","Apps","Presentation_files","Video_Sound_Files","Image_files","Other_files"]
        

        try:
            list = os.listdir(location)
        except OSError:
            print("No such directory exists, please reveiw your entry and try again:")
            continue

        i = 0
        while i < len(list):
        #Each if is for organizing the different file types into folders
            if(list[i].endswith((".txt",".doc",".docx",".rtf"))):
                move(location,i,file_names[0],list)
                
            elif(list[i].endswith((".lnk"))):
                move(location,i,file_names[2],list)
        
            elif(list[i].endswith((".Py",".html",".css",".c",".c++","C","C++",".cpp",".cs",".java","php"))):
                move(location,i,file_names[1],list)
                
            elif(list[i].endswith((".pptx",".pub",".xlsx"))):
                move(location,i,file_names[3],list)
            
            elif(list[i].endswith((".PNG",".JPEG",".PDF",".TIFF",".GIF",".JPG",".PSD",".RAW"))):
                move(location,i,file_names[5],list) 

            elif(list[i].endswith((".MP3",".MP4",".MOV",".AVI",".WMV",".WAV",".vorbis",".AIFF",".OGG",".WMA"))):
                move(location,i,file_names[4],list)     
            #random files that i didnt include
            elif("." in list[i]):
                move(location,i,file_names[6],list)

            i = i + 1

    


if __name__ == "__main__":
    main()







