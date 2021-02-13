import sys 
from ftplib import FTP
import tkinter as tk
import tkinter.filedialog
import os
import glob

class App(tk.Tk):    
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("600x400+200+200")
        self.title("Applikacioni per ngarkimin e fajllave ne FTP server")
        self.Appbutton = tk.Button(text='Choose a File to Upload', command = self.launch_file_dialog_box).pack()
        self.Appbutton_FTP = tk.Button(text='Upload File to FTP Server', command =  self.upload_file_to_FTP).pack()
    def launch_file_dialog_box(self):
        self.raw_filename = tkinter.filedialog.askopenfilename()
    def upload_file_to_FTP(self):
    ##    Konektimi me FTP host       
            session = ftp = FTP('localhost')
            ftp.login( user = 'testuser1', passwd='gashi123')
            src = (r'"C:\Users\qendr\OneDrive\Desktop\FIEK VITI 3\siguria ne internet\Uploadfiles"')
            for file in glob.glob(src +'/*'):
                splittedfile = file.split('.')
                if splittedfile[1] in ["doc","docx","xls","xlsx"]:
                 print("Uploading-"+ os.path.basename(file))
           
            ftp.set_pasv(False)
            file_name = self.raw_filename
            file = open(file_name, 'rb')
            
            ftp.storbinary('STOR %s' % os.path.basename(file_name), file, 1024)
            file.close()
            session.quit()
app = App()
app.mainloop()
