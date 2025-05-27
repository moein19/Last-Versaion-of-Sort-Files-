import customtkinter,shutil,os,re
from tkinter.messagebox import *
from customtkinter import filedialog
from PIL import Image
from tkinter import Menu

class SortFiles:
    def __init__(self,address):
        self.address = address

    def sort_files_by_pattern(self,pattern,file_type):
        pat = re.compile(pattern)
        valid_files = [n for n in [n for n in os.listdir(self.address) if os.path.isfile(os.path.join(self.address , n))] if pat.match(n)]
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
        self.maxsize(600,500)
        self.minsize(600,500)
        self.geometry(f"600x500")
        self.title("Sort Files++")
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.bind("<KeyPress>",func=self.validkeyword)
        customtkinter.set_appearance_mode("light")

        MenuBar = Menu(self)
        self.config(menu = MenuBar)

        ExitMenu = Menu(MenuBar,tearoff = 0,activebackground="#3399FF", activeforeground="white", fg="black",
                        bg="white")
        
        ExitMenu.add_command(label = "Exit",command=  self.go)

        SettingsMenu = Menu(MenuBar,tearoff = 0  ,activebackground="#3399FF", activeforeground="white", fg="black",
                        bg="white")

        HelpMenu = Menu(MenuBar,tearoff = 0,activebackground="#3399FF", activeforeground="white", fg="black",
                        bg="white")
        
        HelpMenu.add_command(label = "Help(English)",command = self.help_english)
        HelpMenu.add_separator()
        HelpMenu.add_command(label = "Help(Persian)",command = self.help_persian)

        SettingsMenu.add_command(label="ColorTheme",command=self.ct)
        SettingsMenu.add_separator()

        self.ch_on_off = customtkinter.BooleanVar(value = True)

        SettingsMenu.add_checkbutton(label="Active Shortcuts keywords",variable = self.ch_on_off)
        

        MenuBar.add_cascade(label = "Exit" , menu = ExitMenu)
        MenuBar.add_cascade(label = "Settings" , menu = SettingsMenu)
        MenuBar.add_cascade(label = "Help",menu = HelpMenu)

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

        self.sort_station_label = customtkinter.CTkLabel(frame1,text="SortStation")
        self.sort_station_label.grid(row=3,column=0 , pady = 5)

        self.sort_station = []
        self.combo = customtkinter.CTkComboBox(frame1,values = self.sort_station , state = "readonly")
        self.combo.grid(row = 4 , column = 0 , pady = 15)

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

This program can sort 19 different types, from Python programming types to Pack Office file types

Note : After each sort, the type of file that was sorted is added to Sort Station, and at the end you can see what type of files you have sorted.

shortcuts : 
1.little q is shortcut for exit the program
2.little b is shortcut for execute browse button 
3.capital D is shortcut for Delete(Drop) Address
4.little l is shortcut for change theme to light
5.little d is shortcut for change theme to dark

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

        self.data2 = r"""

خواسته‌اید تا به حال آیا که کنید سازماندهی خودکار صورت به را پوشه‌ای یک فایل‌های؟
شماست برای برنامه‌ای SortFiles++

برنامه از استفاده نحوه:
می‌کنید انتخاب Browse دکمه یا دستی صورت به را است حاوی فایل‌ها که سیستمی در مورد نظر پوشه آدرس ابتدا

کنید کلیک گزینه آن روی و کنید انتخاب فایل نوع به مربوط منوی از را کرده‌اید انتخاب که‌ای پوشه در را می‌خواهید که را فایلی سپس

:مثال
کنیم مرتب را Desktop در موجود Word فایل‌های تمام می‌خواهیم

دهید دستی صورت به را Desktop آدرس کامل می‌توانید، یعنی باشد این شکل به باید:
C:\Users{UserName}\Desktop

نویسد می‌آدرس انتخاب بخش در اول روش معادل چیزی و است خودکار کاملاً اساساً که کنید کلیک SelectFolder گزینه روی و روید برو خود در مورد نظر پوشه به Browse دکمه با می‌توانید یا

C:\Users{UserName}\Desktop

دهد انجام را کار این به‌صورت برنامه بلکه، کنید نمی‌پیست را آدرس خودتان شما دوم، روش در است این نکته

کردیم وارد برنامه به را Desktop آدرس و آمدیم دوم روش از ما هم اول روش هم، اینجا تا حال به

هستند آفیس مجموعه زیرمجموعه Word فایل‌های تمام و نرم‌افزار این زیرا کنیم انتخاب را آن مربوط گزینه آفیس منوی از باید کنیم مرتب را ورد فایل‌های که می‌خواهیم که حالا

:برنامه رفتار

دهید قرار در آن پوشه تمام را txt فایل‌های و می‌کند ایجاد txt فایل‌های پوشه مثلاً می‌کند ایجاد را File That Type نام به‌ای پوشه، کرده‌اید وارد را آدرسی که در آن در مورد نظر فایل گزینه و آدرس دادن از بعد

می‌شوند جایگذاری به‌اصطلاح، شوند منتقل txt فایل‌های پوشه آن به‌ها فایل تمام، باشید کرده‌اید استفاده آن در قبلاً برنامه این از یا باشید داشته آدرس آن در تصادفی‌ای پوشه اگر

:مهم بسیار نکته
********** دارید را کرده‌اید وارد را آدرسی که در پوشه‌ای در Data.txt نام به فایلی یک شما **********
می‌شود وارد آن را آدرس که پوشه‌ای در جایگزین فایلی و می‌کند حذف txt files پوشه در را Data.txt فایل یعنی، کند رفتار با شما ویندوز رفتار مشابه برنامه این دارد txt فایل‌های پوشه در نام همین با فایلی همچنین و

کند مرتب‌سازی را آفیس فایل‌های انواع تا پایتون برنامه‌نویسی‌های انواع از، مختلف نوع ۱۹ می‌تواند برنامه این

کرده‌اید مرتب را فایل‌هایی نوع چه که ببینید می‌توانید پایان در و شود اضافه  Sort Station به است شده مرتب که فایلی نوع هر بار هر از بعد

:میانبرها
است برنامه از خروج برای q little .۱
است مرور دکمه اجرای برای میانبر b little .۲
است آدرس رها کردن (حذف) برای میانبر D capital .۳
است تیره به تم تغییر برای میانبر d little .۴
است روشن به تم تغییر برای میانبر l little .۵

کنند کار میانبرها، باشند روشن فعال میانبرهای کلیدی کلمات گزینه اگر: توجه

:برنامه مشخصات

++SortFiles :برنامه نام
پوشه یک در فایل‌ها سازماندهی :برنامه عملکرد
حسین‌زاده معین محمد :برنامه‌نویس
است شده ایجاد ماه ۷ :ایجاد زمان مدت
:پایتون برنامه‌نویسی زبان
شمسی هجری ۱۴۰۴ معادل میلادی ۲۰۲۵ سال ساخت
moein191013895@gmail.com :برنامه‌نویس ایمیل    

دارد را آنها سازی مرتب توانایی برنامه که هایی فایل 

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
        frame2.grid(row=1, column=0, sticky="nsew")

        ProgrammingTypes = customtkinter.CTkLabel(frame2,text="Programming Types")
        ProgrammingTypes.grid(row = 0 , column = 0,padx = 10 , pady = 10)
        programming_types = ["sort c","sort html","sort python"]
        self.programming_types_language = customtkinter.CTkComboBox(frame2,values=programming_types,width=175,command=self.pro,state="readonly")
        self.programming_types_language.grid(row = 0 , column = 1,padx = 10 , pady = 10)

        OfficePackTypes = customtkinter.CTkLabel(frame2,text="Office Pack Types")
        OfficePackTypes.grid(row = 1 , column = 0,padx = 10 , pady = 10)
        office_pack_types = ["sort access", "sort excel","sort pdf","sort Power Point","sort word"]
        self.office_types_language = customtkinter.CTkComboBox(frame2, values=office_pack_types, width=175,command=self.office_pack,state="readonly")
        self.office_types_language.grid(row = 1 , column = 1,padx = 10 , pady = 10)

        Recreational_Types = customtkinter.CTkLabel(frame2,text="Recreational Types")
        Recreational_Types.grid(row = 2 , column = 0,padx = 10 , pady = 10)
        recreational_types = ["sort music","sort photo","sort video"]
        self.recreational_types = customtkinter.CTkComboBox(frame2, values=recreational_types, width=175,command=self.recreational_pack,state="readonly")
        self.recreational_types.grid(row = 2 , column = 1,padx = 10 , pady = 10)

        Compressed_Types = customtkinter.CTkLabel(frame2,text="Compressed Types")
        Compressed_Types.grid(row = 3 , column = 0,padx = 10 , pady = 10)
        compressed_types = ["sort rar","sort zip"]
        self.compressed_types = customtkinter.CTkComboBox(frame2, values=compressed_types, width=175,command=self.commress_types,state="readonly")
        self.compressed_types.grid(row = 3 , column = 1,padx = 10 , pady = 10)

        Specialized_Types = customtkinter.CTkLabel(frame2,text="Specialized Types")
        Specialized_Types.grid(row = 4 , column = 0,padx = 10 , pady = 10)
        specialized_files = ["sort android","sort csv","sort exe","sort json","sort pickle","sort txt"]
        self.specialized_files_types = customtkinter.CTkComboBox(frame2, values=specialized_files, width=175,command=self.specialized,state="readonly")
        self.specialized_files_types.grid(row = 4 , column = 1,padx = 10 , pady = 10)

    def ct(self):
        ct = customtkinter.CTk()

        ct.geometry("200x150")
        ct.minsize(200,150)
        ct.maxsize(200,150)
        ct.title("Theme")
        customtkinter.set_appearance_mode("light")

        label = customtkinter.CTkLabel(ct,  text = "Color Theme" , font=customtkinter.CTkFont(size = 20))
        label.pack(pady = 10)

        color_themes = ["dark","light","system"]
        combo = customtkinter.CTkComboBox(ct,values= color_themes , state="readonly" , command = lambda ch : customtkinter.set_appearance_mode(ch))
        combo.pack(pady = 5)
        ct.mainloop()

    def help_english(self):
        help = customtkinter.CTk()

        help.geometry("950x400")
        help.minsize(950,400)
        help.maxsize(950,400)
        help._set_appearance_mode("light")
        help.title("Help(english)")

        help_text_box = customtkinter.CTkTextbox(help,width=940,height=390,wrap="word",state="disabled")
        
        help_text_box.configure(state="normal")
        help_text_box.delete(0.0,"end")
        help_text_box.insert(0.0,self.data)
        help_text_box.configure(state="disabled")

        help_text_box.pack()

        help.mainloop()

    def help_persian(self):
        help = customtkinter.CTk()

        help.geometry("950x400")
        help.minsize(950,400)
        help.maxsize(950,400)
        help._set_appearance_mode("light")
        help.title("Help(english)")

        help_text_box = customtkinter.CTkTextbox(help,width=940,height=390,wrap="word",state="disabled")
        
        help_text_box.configure(state="normal")
        help_text_box.delete(0.0,"end")
        help_text_box.insert(0.0,self.data2)
        help_text_box.tag_add("rtl","1.0","end")

        help_text_box.tag_config("rtl", justify="right", lmargin1=10, lmargin2=10, rmargin=10)

        help_text_box.configure(state="disabled")

        help_text_box.pack()

        help.mainloop()

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
            self.sort_station.append("sort html")
            self.combo.configure(values=set(self.sort_station))
            showinfo("OK","all html files moved to html files directory")

        elif choice == "sort python":
            SortFiles(self.entry.get()).sort_files("python")
            self.sort_station.append("sort python")
            self.combo.configure(values=set(self.sort_station))
            showinfo("OK", "all python files moved to python files directory")

    def recreational_pack(self,ch):
        if ch == "sort music":
            SortFiles(self.entry.get()).sort_files("music")
            self.sort_station.append("sort music")
            self.combo.configure(values=set(self.sort_station))
            showinfo("OK", "all music files moved to music files directory")

        elif ch == "sort photo":
            SortFiles(self.entry.get()).sort_files("photo")
            self.sort_station.append("sort photo")
            self.combo.configure(values=set(self.sort_station))
            showinfo("OK", "all photo files moved to photo files directory")

        elif ch == "sort video":
            SortFiles(self.entry.get()).sort_files("video")
            self.sort_station.append("sort video")
            self.combo.configure(values=set(self.sort_station))
            showinfo("OK", "all video files moved to video files directory")

    def commress_types(self,ch):
        if ch == "sort rar":
            SortFiles(self.entry.get()).sort_files("rar")
            self.sort_station.append("sort rar")
            self.combo.configure(values=set(self.sort_station))
            showinfo("OK", "all rar files moved to rar files directory")
        elif ch == "sort zip":
            SortFiles(self.entry.get()).sort_files("zip")
            self.sort_station.append("sort zip")
            self.combo.configure(values=set(self.sort_station))
            showinfo("OK", "all zip files moved to zip files directory")

    def office_pack(self,ch):
        if ch == "sort access":
            SortFiles(self.entry.get()).sort_files("access")
            self.sort_station.append("sort access")
            self.combo.configure(values=set(self.sort_station))
            showinfo("OK", "all access files moved to access files directory")

        elif ch == "sort excel":
            SortFiles(self.entry.get()).sort_files("excel")
            self.sort_station.append("sort excel")
            self.combo.configure(values=set(self.sort_station))
            showinfo("OK", "all excel files moved to excel files directory")

        elif ch == "sort pdf":
            SortFiles(self.entry.get()).sort_files("pdf")
            self.sort_station.append("sort pdf")
            self.combo.configure(values=set(self.sort_station))
            showinfo("OK", "all pdf files moved to pdf files directory")

        elif ch == "sort Power Point":
            SortFiles(self.entry.get()).sort_files("powerPoint")
            self.sort_station.append("sort powerPoint")
            self.combo.configure(values=set(self.sort_station))
            showinfo("OK", "all Power Point files moved to Power Point files directory")

        elif ch == "sort word":
            SortFiles(self.entry.get()).sort_files("word")
            self.sort_station.append("sort word")
            self.combo.configure(values=set(self.sort_station))
            showinfo("OK", "all word files moved to word files directory")

    def drop_address(self):
        self.entry.delete(0,"end")

    def askopendir(self):
        self.entry.delete(0, "end")
        self.entry.insert(0,filedialog.askdirectory())
        
    def validkeyword(self,ch):
        if self.ch_on_off.get() == True:
            if ch.char == "l":
                customtkinter.set_appearance_mode("light")
            elif ch.char == "d":
                customtkinter.set_appearance_mode("dark")
            elif ch.char == "q":
                self.destroy()
            elif ch.char == "D":
                self.entry.delete(0,"end")
            elif ch.char == "b":
                self.askopendir()

    def go(self):
        self.destroy()

class Start(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.maxsize(500,500)
        self.minsize(500,500)
        customtkinter.set_appearance_mode("light")
        self.title("Start")

        self.bind("<KeyPress>",func = self.validkeywords)

        MenuBar = Menu(self)
        self.config(menu = MenuBar)

        ExitMenu = Menu(MenuBar,tearoff = 0,activebackground="#3399FF", activeforeground="white", fg="black",
                        bg="white")
        
        ExitMenu.add_command(label = "Exit" , command = self.go)

        MenuBar.add_cascade(label = "Exit" , menu = ExitMenu)

        self.logo = customtkinter.CTkLabel(self,text="",fg_color="transparent",image = customtkinter.CTkImage(Image.open("logo.ico"),size=(250,250)),height=250,width=250)
        self.logo.pack(pady = 15)

        self.start_btn = customtkinter.CTkButton(self,text="Start",text_color="white",hover_color="#0000FF",fg_color="DarkBlue",width=150,height=50,command = self.start)
        self.start_btn.pack(pady = 15)

    def start(self):
        self.destroy()
        if __name__ == "__main__":
            window = Window()
            window.mainloop()

    def go(self):
        self.destroy()

    def validkeywords(self,ch):
        if ch.keysym == "q":
            self.destroy()
        elif ch.keysym == "d":
            customtkinter.set_appearance_mode("dark")
        elif ch.keysym == "l":
            customtkinter.set_appearance_mode("light")

if __name__ == "__main__":
    start = Start()
    start.mainloop()