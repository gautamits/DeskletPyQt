import tkinter as tk


LARGE_FONT=("Verdana",12)
class SeaofBTCapp(tk.Tk):  #we can put here inheritance
	def __init__(self,*args,**kwargs):  #  initialises the class as well as class is called, args is list of arguments, kwargs is cuboid of arguments passed through dictionary
		tk.Tk.__init__(self,*args,**kwargs)
		container = tk.Frame(self)     ##top container
		container.pack(side="top",fill="both",expand=True)
	
	
		container.grid_rowconfigure(0,weight=1)
		container.grid_columnconfigure(0,weight=1)
	
		self.frames={}
	
		frame = StartPage(container,self)
	
		self.frames[StartPage] = frame
	
		frame.grid(row=0, column=0, sticky="nsew")
	
		self.show_frame(StartPage)
	def show_frame(self,cont):
		frame = self.frames[cont]
		frame.tkraise()

class StartPage(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label=tk.Label(self,text="Start Page",font="LARGE_FONT")
		label.pack(pady=10,padx=10)
app=SeaofBTCapp()
app.mainloop()
		
