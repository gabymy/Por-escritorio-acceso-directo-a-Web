import tkinter as tk
import webbrowser


window=tk.Tk()
window.geometry("300x200")
window.title("Ingreso Directo a Redes")

def linkedin(event):
    webbrowser.open_new(' aca pones la url'  )

def twitter(event):
    webbrowser.open_new(' aca pones la url ' )



label1=tk.Label(text="Mi Red Social")
label1.grid(column=0,row=0)
label1 = tk.Label(text = "Mi red Social", font=("Times new roman",20))

button1=tk.Button(window,text="Linkedin",bg="orange")
button1.grid(column=1,row=1)
button2=tk.Button(window,text="Twitter",bg="pink")
button2.grid(column=3,row=1)

button1.bind("<Button-1>",linkedin)
button2.bind("<Button-1>",twitter)

window.mainloop()




