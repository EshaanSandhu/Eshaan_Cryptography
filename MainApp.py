from tkinter import*
import os
from tkinter import ttk
from tkinter import filedialog,messagebox
import tkinter as tk
from PIL import Image,ImageTk
from Encryption import*
from Decryption import*
import shutil
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidKey

class Main_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Steganography")

        #title
        title_label = Label(self.root,text="SECURE DATA HIDING IN IMAGES USING STEGANOGRAPHY",font=("times new roman",20,"bold"),bg="PaleTurquoise1",fg="black")
        title_label.place(x=0,y=0,width=1650,height=50)
        
        #Background
        img_bg=Image.open(r"background_image_3.jpg")
        img_bg=img_bg.resize((1792,1024))
        self.photo_image_bg = ImageTk.PhotoImage(img_bg)
        second_label=Label(self.root,image=self.photo_image_bg)
        second_label.place(x=0,y=50,width=1600,height=800)

        #Encryption
        title_label = Label(self.root,text="ENCRYPTION",font=("times new roman",15,"bold"),bg="PaleTurquoise1",fg="black")
        title_label.place(x=250,y=100,width=300,height=50)

        #Decryption
        title_label = Label(self.root,text="DECRYPTION",font=("times new roman",15,"bold"),bg="PaleTurquoise1",fg="black")
        title_label.place(x=950,y=100,width=300,height=50)

        #Warning
        title_label = Label(self.root,text="IT APPLIES WITH .PNG EXTENSION ONLY AS OTHER EXTENSIONS CHANGE THE INTENSITY VALUES OF PIXELS AFTER THEY ARE SAVED",font=("times new roman",12,"bold"),bg="PaleTurquoise1",fg="black")
        title_label.place(x=250,y=750,width=1200,height=50)

        #Input Value
        title_label = Label(self.root,text="Enter Message",font=("times new roman",15,"bold"),bg="PaleTurquoise1",fg="black")
        title_label.place(x=200,y=250,width=200,height=50)

        #Input Text
        title_label = Label(self.root,text="Enter Message",font=("times new roman",15,"bold"),bg="PaleTurquoise1",fg="black")
        title_label.place(x=450,y=250,width=200,height=50)

        #Text Input Encryption
        input_text_value = Text(title_label,height=30,width=200,font=("times new roman",15),bg="PaleTurquoise1",fg="black")
        input_text_value.pack()

        #Input Password
        title_label = Label(self.root,text="Enter Password",font=("times new roman",15,"bold"),bg="PaleTurquoise1",fg="black")
        title_label.place(x=200,y=350,width=200,height=50)

        #Input Text
        title_label = Label(self.root,text="Enter Value",font=("times new roman",15,"bold"),bg="PaleTurquoise1",fg="black")
        title_label.place(x=450,y=350,width=200,height=50)

        #Text Input Encryption
        input_text_password = Text(title_label,height=30,width=200,font=("times new roman",15),bg="PaleTurquoise1",fg="black")
        input_text_password.pack()

        def upload_image():
            try:
                file_path = filename = filedialog.askopenfilename(initialdir = "/",
                                            title = "Select a Image",
                                            filetypes = (("Image files",
                                                            "*.png*"),
                                                        ("All files",
                                                            "*.*")))
                if file_path:
                    try:
                        image = Image.open(file_path)
                        image.thumbnail((400, 400))
                        photo = ImageTk.PhotoImage(image)
                        image_label.config(image=photo)
                        image_label.image = photo
                        save_image(file_path)
                        messagebox.showinfo("Success", "Image uploaded successfully!")
                    except Exception as e:
                        messagebox.showerror("Error", f"Could not open or process image: {e}")
                else:
                        print("No file selected") 
            except Exception as e:
                messagebox.showinfo("Success!", "Image Already in the directory")
    
        def save_image(file_path):
            global filename
            save_dir = os.path.dirname(os.path.abspath(__file__))
            filename = os.path.basename(file_path)
            try:
                shutil.copy(file_path, os.path.join(save_dir, filename))
                print("Image saved to:", os.path.join(save_dir, filename))
            except Exception as e:
                messagebox.showinfo("Success!", "Image Already in the directory")

        #Upload Button
        upload_button = Button(second_label,text="UPLOAD IMAGE",cursor="hand2",command=upload_image,font=("times new roman",15,"bold"),bg="PaleTurquoise1",fg="black")
        upload_button.place(x=320,y=370,height=50,width=200)

        #Image Label
        image_label = tk.Label(second_label)
        image_label.place(x=320,y=450,height=200,width=200)

        #Hashing Password
        def hash_password(password):
            salt = os.urandom(16)
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
                backend=default_backend()
            )
            return salt, kdf.derive(password.encode('utf-8'))
        
        def save_password_data(salt, hashed_password,msg_len,filename):
            with open(filename, 'wb') as f:
                f.write(salt + hashed_password + msg_len.to_bytes(4, 'big'))

        #Encryption Function
        def Encrypting():
            pass_asinp = input_text_password.get(1.0, "end-1c")
            message_words = input_text_value.get(1.0, "end-1c")
            message_length = len(message_words)
            password_length = len(pass_asinp)
            if message_length < 0 and password_length < 0 :
                messagebox.showinfo("WARNING!","Message and Password Length Must be Greater than 0 Characters and Select An Image")
            else:
                only_filename, _ = os.path.splitext(filename)
                salt_hashed,kdf_hashed = hash_password(pass_asinp)
                save_password_data(salt_hashed,kdf_hashed,message_length,filename='encrypted_'+only_filename+'_password_data.dat')
                Encryption_Func(filename,message_words)
                messagebox.showinfo("SUCCESS!","Encryption Successful")

        # #Encryption
        b1_1 = Button(second_label,text="ENCRYPT",cursor="hand2",command=Encrypting,font=("times new roman",15,"bold"),bg="PaleTurquoise1",fg="black")
        b1_1.place(x=600,y=550,height=40,width=150)

        #Decryption
         #Input Password
        title_label = Label(self.root,text="Enter Password",font=("times new roman",15,"bold"),bg="PaleTurquoise1",fg="black")
        title_label.place(x=850,y=250,width=200,height=50)

        #Input Text
        title_label = Label(self.root,text="Enter Message",font=("times new roman",15,"bold"),bg="PaleTurquoise1",fg="black")
        title_label.place(x=1100,y=250,width=200,height=50)

        #Text Input Decryption
        input_text_password_dec = Text(title_label,height=30,width=200,font=("times new roman",15),bg="PaleTurquoise1",fg="black")
        input_text_password_dec.pack()

        #Button and Image

        def upload_image_dec():
            global filename_de
            try:
                filepathde = filename_de = filedialog.askopenfilename(initialdir = "/",
                                            title = "Select the Encrypted Image",
                                            filetypes = (("Image files",
                                                            "*.png*"),
                                                        ("All files",
                                                            "*.*")))
                if filepathde:
                    try:
                        image = Image.open(filepathde)
                        image.thumbnail((400, 400))
                        photo = ImageTk.PhotoImage(image)
                        image_label_de.config(image=photo)
                        image_label_de.image = photo
                        messagebox.showinfo("Success", "Image uploaded successfully!")
                    except Exception as e:
                        messagebox.showinfo("Success!", "Image Already in the directory")
                else:
                        print("No file selected") 
            except Exception as e:
                messagebox.showerror("Error", f"A general error occurred: {e}")
        #Upload Button
        upload_button_de = Button(second_label,text="UPLOAD IMAGE",cursor="hand2",command=upload_image_dec,font=("times new roman",15,"bold"),bg="PaleTurquoise1",fg="black")
        upload_button_de.place(x=1000,y=300,height=50,width=200)

        #Image Label
        image_label_de = tk.Label(second_label)
        image_label_de.place(x=1000,y=380,height=200,width=200)

        def load_password_data(filename):
            with open(filename, 'rb') as f:
                data = f.read()
            salt = data[:16]
            hashed_password = data[16:48]
            msg_len = int.from_bytes(data[48:], 'big')
            return salt, hashed_password, msg_len

        def verify_password(salt, hashed_password, password):
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
                backend=default_backend()
            )
            try:
                kdf.verify(password.encode('utf-8'), hashed_password)
                return True
            except InvalidKey:
                print(password.encode('utf-8'))
                return False

        #Decryption Function
        def Decrypting():
            if len(input_text_password_dec.get(1.0, "end-1c")) > 0:
                only_filename_dec, _ = os.path.splitext(filename_de)
                salt_verify,hashed_verify,msg_len = load_password_data(filename=only_filename_dec+'_password_data.dat')
                if(verify_password(salt_verify,hashed_verify,input_text_password_dec.get(1.0, "end-1c")) == True):
                    Message_Dec = Decryption_Func(os.path.basename(filename_de),msg_len)
                    messagebox.showinfo("MESSAGE",Message_Dec)
                else:
                    messagebox.showinfo("WARNING!","Wrong Password")
            else:
                messagebox.showinfo("WARNING!","Password Length Must be Greater than 0 Characters")

        # #Encryption
        b1_2 = Button(second_label,text="DECRYPT",cursor="hand2",command=Decrypting,font=("times new roman",15,"bold"),bg="PaleTurquoise1",fg="black")
        b1_2.place(x=1030,y=620,height=40,width=150)

if __name__ =="__main__":
    root = Tk()
    obj = Main_App(root)
    root.mainloop()