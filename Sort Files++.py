import customtkinter,shutil,os,re
from tkinter.messagebox import *
from customtkinter import filedialog

class SortFiles:
    def __init__(self,address):
        self.address = address

    def sort_files_by_pattern(self,pattern,file_type):
        pat = re.compile(pattern)
        valid_files = [n for n in os.listdir(self.address) if pat.match(n)]
        if len(valid_files) > 0:
            if f"{file_type} files" not in os.listdir(self.address):
                os.mkdir(self.address+os.sep+f"{file_type} files")
            for file in valid_files:
                try:
                    shutil.move(self.address+os.sep+file,self.address+os.sep+f"{file_type} files")
                except shutil.Error:
                    os.remove(self.address+os.sep+f"{file_type} files"+os.sep+file)
                    shutil.move(self.address + os.sep + file, self.address + os.sep + f"{file_type} files")

    def sort_files(self,file_type):
        file_patterns = {
            "access": r".*\.(accdb|mdb|accde|mde|ade|accft|mdw)$",
            "android": r".*\.(apk|obb|xapk|apks|aab|dex|jar|xml|cfg|db|sqlite|log|bak|bin|img|iso)$",
            "c": r".*\.c$",
            "csv": r".*\.csv$",
            "excel": r".*\.(xls|xlsx|xlsm|xlsb|xlt|xltx|xltm|csv|xml|xlam|xla)$",
            "exe": r".*\.exe$",
            "html": r".*\.(htm|html)$",
            "json": r".*\.json$",
            "music": r".*\.(mp3|wav|aac|flac|ogg|wma|m4a|alac|aiff|opus|amr|ape|dsf|dff|pcm|mid|midi|mod|xm|s3m|it|cda|ra|rm|au|voc|wv|tta|snd|caf|mpc)$",
            "pdf": r".*\.pdf$",
            "photo": r".*\.(jpg|jpeg|png|gif|bmp|tiff|tif|webp|heic|heif|avif|raw|cr2|nef|arw|orf|sr2|rw2|dng|ico|svg|eps|psd|ai|xcf)$",
            "pickle": r".*\.pickle$",
            "powerPoint": r".*\.(ppt|pptx|pps|ppsx|pot|potx|pptm|potm|ppsm)$",
            "python": r".*\.py$",
            "rar": r".*\.rar$",
            "txt": r".*\.txt$",
            "video": r".*\.(mp4|m4v|mov|avi|wmv|flv|webm|mkv|3gp|3g2|mpg|mpeg|mpe|ts|m2ts|mts|vob|rm|rmvb|asf|f4v|ogv|divx)$",
            "word": r".*\.(doc|docx|dot|dotx|docm|dotm)$",
            "zip": r".*\.zip$",
        }
        pattern = file_patterns.get(file_type)
        if pattern:
            self.sort_files_by_pattern(pattern,file_type)
class Window(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.maxsize(self.winfo_screenwidth(),self.winfo_screenheight())
        self.minsize(self.winfo_screenwidth(),self.winfo_screenheight())
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}+0+0")
        self.title("Sort Files++")
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.bind("<KeyPress>",func=self.validkeyword)
        customtkinter.set_appearance_mode("dark")

        #####################Frame1
        frame1 = customtkinter.CTkFrame(self)
        frame1.grid(row=0,column=0,sticky="nsew")
        frame1.grid_columnconfigure(0,weight=1)

        self.entry = customtkinter.CTkEntry(frame1,placeholder_text="Enter your directory address  : ",text_color=("black","white"),border_width=3,border_color="silver")
        self.entry.grid(row=0,column=0,pady=15,padx=25,sticky="ew")

        self.browse = customtkinter.CTkButton(frame1,text="Browse",text_color=("Black","white"),fg_color=("#BFFFFF","#008B8B"),hover_color=("#8CFFFB","#004B49"),command=self.askopendir)
        self.browse.grid(row=1,column=0,pady=15)

        self.delete_address = customtkinter.CTkButton(frame1,text="Delete Address",text_color=("Black","white"),fg_color=("#BFFFFF","#008B8B"),hover_color=("#8CFFFB","#004B49"),command=self.drop_address)
        self.delete_address.grid(row=2,column=0,pady=15)

        self.data = r"""
Have you ever wanted to automatically organize files in a folder?
SortFiles ++ is a program for you

How to use the program:
First, you select the address of the desired folder in the system that contains files, either manually or using the Browse button

Then select the file you want to sort in the folder you selected from the menu corresponding to the file type and click on that option

Example:
We want to sort all the word files on the Desktop

You can manually give the full address of the Desktop, which means it should be like this:
C:\Users\{UserName}\Desktop

Or you can use the Browse button to go to the desired folder in your system and click the SelectFolder option, which is basically completely automatic and writes something equivalent to the first method in the address selection section

C:\Users\{UserName}\Desktop

The point is that in the second method, you do not get the address yourself and paste it, but the program does this automatically

Anyway, so far, both the first method and We came from the second method and gave the Desktop address to the program. Now that we want to sort the word files, we have to select its option from the Office menu because the software and all word files are a subset of the Office suite.

Program behavior:

After giving the address and selecting the desired file option to sort it in the folder you entered the address, the program creates a folder called Type That File in the folder you entered, for example, it creates the txt files folder and automatically puts all the txt files in that folder. If you have a random folder at that address or have previously used this program at that address, all these files are transferred to that txt files folder, so to speak, they are pasted.

Very important point:
********** You have a file called, for example, Data.txt in the folder you entered the address and you also have a file with this name in the txt files folder. This program behaves similarly to Windows' behavior with you, that is, it deletes the Data.txt file in the txt files folder and The file that replaces the folder whose address you entered **********

In the Sort Station section, each sort you have done is added and you can see at the end how many sorts you have done in that folder

This program can sort 19 different types, from Python programming types to Pack Office file types

shortcuts : 
1.little q is shortcut for exit the program
2.little d is shortcut for change theme to dark
3.little l is shortcut for change theme to  light 
4.little b is shortcut for execute browse button 
5.capital D is shortcut for Delete(Drop) Address

Note : If the active shortcuts keywords option is not turned on the shortcuts will not work

Program specifications:

Program name: SortFiles ++
Program function: Organize files in a folder
Programmer: Mohammad Moein Hosseinzadeh
Duration of creation: 7 months
Programming language: Python
Year of creation: 2025 AD corresponding to 1404 Solar Hijri
Programmer email: moein91013895@gmail.com


valid types in this program:

access
android
c
csv
excel
exe
html
json
music
pdf
photo
pickle
powerpoint
python
rar
txt
video
word
zip
"""

        ###################Frame2
        frame2 = customtkinter.CTkFrame(self)
        frame2.grid(row=1, column=1, sticky="nsew")

        ProgrammingTypes = customtkinter.CTkLabel(frame2,text="Programming Types")
        ProgrammingTypes.pack(pady=5)
        programming_types = ["sort c","sort html","sort python"]
        self.programming_types_language = customtkinter.CTkComboBox(frame2,values=programming_types,width=175,command=self.pro,state="readonly")
        self.programming_types_language.pack(pady=10)

        OfficePackTypes = customtkinter.CTkLabel(frame2,text="Office Pack Types")
        OfficePackTypes.pack(pady=5)
        office_pack_types = ["sort access", "sort excel","sort pdf","sort Power Point","sort word"]
        self.office_types_language = customtkinter.CTkComboBox(frame2, values=office_pack_types, width=175,command=self.office_pack,state="readonly")
        self.office_types_language.pack(pady=10)

        Recreational_Types = customtkinter.CTkLabel(frame2,text="Recreational Types")
        Recreational_Types.pack(pady=5)
        recreational_types = ["sort music","sort photo","sort video"]
        self.recreational_types = customtkinter.CTkComboBox(frame2, values=recreational_types, width=175,command=self.recreational_pack,state="readonly")
        self.recreational_types.pack(pady=10)

        Compressed_Types = customtkinter.CTkLabel(frame2,text="Compressed Types")
        Compressed_Types.pack(pady=5)
        compressed_types = ["sort rar","sort zip"]
        self.compressed_types = customtkinter.CTkComboBox(frame2, values=compressed_types, width=175,command=self.commress_types,state="readonly")
        self.compressed_types.pack(pady=10)

        Specialized_Types = customtkinter.CTkLabel(frame2,text="Specialized Types")
        Specialized_Types.pack(pady=5)
        specialized_files = ["sort android","sort csv","sort exe","sort json","sort pickle","sort txt"]
        self.specialized_files_types = customtkinter.CTkComboBox(frame2, values=specialized_files, width=175,command=self.specialized,state="readonly")
        self.specialized_files_types.pack(pady=10)

        ###################Frame3

        frame3 = customtkinter.CTkFrame(self)
        frame3.grid(row=0, column=1, sticky="nsew")

        var = customtkinter.StringVar(value="on")
        self.switch = customtkinter.CTkSwitch(frame3,onvalue="on",offvalue="off",text="active shortcuts keywords",variable=var,text_color=("black","white"),progress_color=("#BFFFFF","#008B8B"),button_color=("black","white"),command=self.styleswitch)
        self.switch.pack(pady=5)

        ColorThemes = customtkinter.CTkLabel(frame3,text="Color Themes")
        ColorThemes.pack(pady=10)

        SortStation = customtkinter.CTkLabel(frame3,text="Sort Station")
        self.sort_station = []
        self.combo = customtkinter.CTkComboBox(frame3,values=self.sort_station,width=175,state="readonly")

        self.themes = ["dark","light","system"]
        self.color_themes = customtkinter.CTkComboBox(frame3,values=self.themes,width=175,command=self.chtheme,state="readonly")
        self.color_themes.pack(pady=10)
        SortStation.pack(pady=10)
        self.combo.pack(pady=10)

        ###################Frame4
        frame4 = customtkinter.CTkFrame(self)
        frame4.grid(row=1, column=0, sticky="nsew")

        frame4.grid_columnconfigure(0,weight=1)
        frame4.grid_rowconfigure(1,weight=1)

        self.help = customtkinter.CTkTextbox(frame4,wrap="word",state="disabled")
        self.help.grid(row=1,column=0,sticky="nsew",padx=15,pady=10)

        self.btnHelp = customtkinter.CTkButton(frame4,text="Help",text_color=("Black","white"),fg_color=("#BFFFFF","#008B8B"),hover_color=("#8CFFFB","#004B49"),command=self.writeHelp)
        self.btnHelp.grid(row=0,column=0,sticky="nsew",padx=300,pady=5)

    def specialized(self,ch):
        if ch == "sort android" :
            SortFiles(self.entry.get()).sort_files("android")
            self.sort_station.append("sort android")
            self.combo.configure(values=set(self.sort_station))
            showinfo("OK", "all android files moved to android files directory")
        elif ch == "sort csv":
            SortFiles(self.entry.get()).sort_files("csv")
            self.sort_station.append("sort csv")
            self.combo.configure(values=set(self.sort_station))
            showinfo("OK", "all csv files moved to csv files directory")
        elif ch == "sort exe":
            SortFiles(self.entry.get()).sort_files("exe")
            self.sort_station.append("sort exe")
            self.combo.configure(values=set(self.sort_station))
            showinfo("OK", "all exe files moved to exe files directory")
        elif ch == "sort json":
            SortFiles(self.entry.get()).sort_files("json")
            self.sort_station.append("sort json")
            self.combo.configure(values=set(self.sort_station))
            showinfo("OK", "all json files moved to json files directory")
        elif ch == "sort pickle":
            SortFiles(self.entry.get()).sort_files("pickle")
            self.sort_station.append("sort pickle")
            self.combo.configure(values=set(self.sort_station))
            showinfo("OK", "all pickle files moved to pickle files directory")

        elif ch == "sort txt":
            SortFiles(self.entry.get()).sort_files("txt")
            self.sort_station.append("sort txt")
            self.combo.configure(values=set(self.sort_station))
            showinfo("OK", "all txt files moved to txt files directory")

    def pro(self,choice):
        if choice == "sort c":
            SortFiles(self.entry.get()).sort_files("c")
            self.sort_station.append("sort c")
            self.combo.configure(values=set(self.sort_station))
            showinfo("OK","all c files moved to c files directory")

        elif choice == "sort html":
            SortFiles(self.entry.get()).sort_files("html")
            showinfo("OK","all html files moved to html files directory")
            self.sort_station.append("sort html")
            self.combo.configure(values=set(self.sort_station))

        elif choice == "sort python":
            SortFiles(self.entry.get()).sort_files("python")
            showinfo("OK", "all python files moved to python files directory")
            self.sort_station.append("sort python")
            self.combo.configure(values=set(self.sort_station))

    def recreational_pack(self,ch):
        if ch == "sort music":
            SortFiles(self.entry.get()).sort_files("music")
            showinfo("OK", "all music files moved to music files directory")
            self.sort_station.append("sort music")
            self.combo.configure(values=set(self.sort_station))

        elif ch == "sort photo":
            SortFiles(self.entry.get()).sort_files("photo")
            showinfo("OK", "all photo files moved to photo files directory")
            self.sort_station.append("sort photo")
            self.combo.configure(values=set(self.sort_station))

        elif ch == "sort video":
            SortFiles(self.entry.get()).sort_files("video")
            showinfo("OK", "all video files moved to video files directory")
            self.sort_station.append("sort video")
            self.combo.configure(values=set(self.sort_station))

    def styleswitch(self):
        if self.switch.get() == "off":
            self.switch.configure(text="inactive shortcuts keywords")

        elif self.switch.get() == "on":
            self.switch.configure(text="active shortcuts keywords")

    def commress_types(self,ch):
        if ch == "sort rar":
            SortFiles(self.entry.get()).sort_files("rar")
            showinfo("OK", "all rar files moved to rar files directory")
            self.sort_station.append("sort rar")
            self.combo.configure(values=set(self.sort_station))
        elif ch == "sort zip":
            SortFiles(self.entry.get()).sort_files("zip")
            showinfo("OK", "all zip files moved to zip files directory")
            self.sort_station.append("sort zip")
            self.combo.configure(values=set(self.sort_station))

    def office_pack(self,ch):
        if ch == "sort access":
            SortFiles(self.entry.get()).sort_files("access")
            showinfo("OK", "all access files moved to access files directory")
            self.sort_station.append("sort access")
            self.combo.configure(values=set(self.sort_station))

        elif ch == "sort excel":
            SortFiles(self.entry.get()).sort_files("excel")
            showinfo("OK", "all excel files moved to excel files directory")
            self.sort_station.append("sort excel")
            self.combo.configure(values=set(self.sort_station))

        elif ch == "sort pdf":
            SortFiles(self.entry.get()).sort_files("pdf")
            showinfo("OK", "all pdf files moved to pdf files directory")
            self.sort_station.append("sort pdf")
            self.combo.configure(values=set(self.sort_station))

        elif ch == "sort Power Point":
            SortFiles(self.entry.get()).sort_files("powerPoint")
            showinfo("OK", "all Power Point files moved to Power Point files directory")
            self.sort_station.append("sort power point")
            self.combo.configure(values=set(self.sort_station))

        elif ch == "sort word":
            SortFiles(self.entry.get()).sort_files("word")
            showinfo("OK", "all word files moved to word files directory")
            self.sort_station.append("sort word")
            self.combo.configure(values=set(self.sort_station))

    def chtheme(self,choice):
        customtkinter.set_appearance_mode(choice)

    def drop_address(self):
        self.entry.delete(0,"end")

    def askopendir(self):
        self.entry.delete(0, "end")
        self.entry.insert(0,filedialog.askdirectory())

    def writeHelp(self):
        if len(self.help.get(0.0,"end")) == 1:
            self.help.configure(state="normal")
            self.help.insert(0.0,self.data)
            self.help.configure(state="disabled")
        else:
            showwarning("WARNING".capitalize(),"You clicked this button once")

    def validkeyword(self,ch):
        if self.switch.get() == "on":
            if ch.char == "d":
                customtkinter.set_appearance_mode("dark")
            elif ch.char == "l":
                customtkinter.set_appearance_mode("light")
            elif ch.char == "q":
                self.destroy()
            elif ch.char == "D":
                self.entry.delete(0,"end")
            elif ch.char == "b":
                self.askopendir()

if __name__ == "__main__":
    window = Window()
    window.mainloop()
