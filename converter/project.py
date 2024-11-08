import tkinter as tk
import ttkbootstrap as ttk
###
cont ={
    "km":int("0"),
    "m":int("1"),
    "cm":int("2")
}
n1 = ""
def engine():
    numm = num.get()
    num1 = first_string.get()
    num2 =second_string.get()
    las = last_intt.get()
    if cont.get(num1) > cont.get(num2):
        calco = las / 1000
        num.set(str(calco))
        if cont.get(num1) - cont.get(num2) == 2:
            calco = las / 100000
            num.set(str(calco))
    elif cont.get(num1) < cont.get(num2):
        calco =  las * 1000
        num.set(str(calco))
        
##
root = ttk.Window(themename='darkly')
root.title('Converter')
root.geometry('400x200')
##
fon ='cilibri 25 bold'
##
main_label= ttk.Label(master= root,text='Converter',font = fon,foreground='blue')
main_label.pack()
##
main_frame = ttk.Frame(master = root)
main_frame.pack()
##
first_string= tk.StringVar()
first_entry= ttk.Entry(master = main_frame,foreground='green',textvariable=first_string,width=15)
first_entry.pack(side='left',padx=5)
##
lablee = ttk.Label(master = main_frame,text = 'To',font=fon)
lablee.pack(side='left',padx=5)
##
second_string=tk.StringVar()
second_entry=ttk.Entry(master=main_frame,foreground='green',textvariable=second_string,width=15)
second_entry.pack(padx=5,side='right')
##
last_intt = tk.IntVar()
last = ttk.Entry(master = root , foreground='blue',textvariable=last_intt)
last.pack()

##
con = ttk.Button(master =root ,text='Convay' , command=engine,style='info.TButton')
con.pack(pady=5)
###
num = tk.StringVar()
num_lable = ttk.Label(master=root,text='none',font=fon , textvariable=num)
num_lable.pack(pady=5)
##
root.mainloop()