from pytube import YouTube
import os
import time
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import messagebox
from pytube.cli import on_progress
from pytube.cli import *



a = 12
os.system('cls')


root = Tk()
root.title("Python-YTD")
root.geometry('300x240')  
root.resizable(False, False)
photo = PhotoImage(file = "youtube.png")
root.iconphoto(False, photo)


tcolor = "#900C3F"
fcolor = "#D6F6F0"
root.config(bg=tcolor)
root.columnconfigure (0,weight = 1)
root.resizable (0,0)



def Download():
	#Inputs

	url = text_entry.get()

	a = types.get()
	print(a)

	path = 'E:\Python Code\Youtube Downloader\Downloads'


	print(url)
	print(a)

	#To check the Valid Link
	if len(url) < 1:
		messagebox.showerror("UI-YTD", " Please Enter a Valid URL ")
	else:


		# [1] MP3 Low Quality
		if a == "Audio LQ":


			yt = YouTube(url)


			video = yt.streams.filter(only_audio=True).first()

			out_file = video.download(output_path=path)

			# RENMAE KE LIYE HAI YE
			base, ext = os.path.splitext(out_file)
			new_file = base + '.mp3'
			os.rename(out_file, new_file)



			messagebox.showinfo("UI-YTD", "MP3 LQ Downloaded..." + path)






		# [2] MP3 High Quality
		elif a == "Audio HQ":



			yt = YouTube(url)

			video = yt.streams.filter(only_audio=True).last()



			out_file = video.download(output_path=path)


			base, ext = os.path.splitext(out_file)
			new_file = base + '.mp3'
			os.rename(out_file, new_file)


			messagebox.showinfo("UI-YTD", "MP3 HQ Downloaded at " + path)



		# Video Low Quality
		elif a == "Low Quality Video":


			b = YouTube(url,on_progress_callback=on_progress).streams.filter(progressive = True).first().download(output_path=path)

			messagebox.showinfo("UI-YTD", "Video In LQ have Downloaded at " + path)



		# Video High Quality
		elif a == "High Quality Video":



			try:
				print("Hello")
				#b = YouTube(url,on_progress_callback=on_progress).streams.filter(progressive = True).last().download(output_path=path)
				messagebox.showinfo("UI-YTD", "Video In HQ have Downloaded at " + path)
			except:
				b = YouTube(url,on_progress_callback=on_progress).streams.filter(progressive = True).first().download(output_path=path)

				messagebox.showinfo("UI-YTD", "Video is Downloaded at " + path)

		else:
			print(" >>> You have selected invalid Option :) ")



# GUI

author = Label(text = "Author : Singh Aayurshi", background=tcolor, foreground=fcolor, font=("Verdana Bold",15))
author.grid(pady=10)

label = Label(root, text="URL", background=tcolor, foreground="dark orange", font=("Trebuchet MS bold",10))
label.grid()

text_entry = Entry(root,width = 35)
text_entry.grid()


label = Label(root,background=tcolor, foreground="dark orange", font=("Trebuchet MS bold",10), text= "Select Format")
label.grid(pady=(10, 0))


options = ["Audio LQ","Audio HQ", "Low Quality Video","High Quality Video"]
types = ttk.Combobox(root, values=options, width =32)
types.current(0)
types.grid()

label = Label(root,background=tcolor, foreground="dark orange", font=("Trebuchet MS bold",10))
label.grid()

Button(root, text="DOWNLOAD",width=20,style ="PT.TButton", command= Download).grid()

#Percentage = Label(root,text="100%",background=tcolor, foreground="dark orange", font=("Trebuchet MS bold",20))
#Percentage.grid()

root.mainloop()
