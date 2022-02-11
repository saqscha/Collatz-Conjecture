import tkinter as tk


root = tk.Tk()
root.configure(bg='#E9EDC9')
root.title("Collatz Conjecture")
root.geometry('300x450')
x1 = '0'


def enter(e):
    output.config(state='normal')
    x = input_window.get()
    x1 = int(x)
    output.delete(1.0, tk.END)
    output.insert(tk.END, '➡')
    output.insert(tk.END, x1)
    output.insert(tk.END, '\n' + '➡')
    while x1 > 1:
        

    
        if x1 % 2:  # ungerade
            x1 = x1 * 3 + 1
            input_window.delete(0, tk.END)
            output.insert(tk.END, x1)
            output.insert(tk.END, '\n' + '➡')

            
        else:
            x1 = x1 / 2
            input_window.delete(0, tk.END)
            output.insert(tk.END, x1)
            output.insert(tk.END, '\n' + '➡')


    output.config(state='disable')
            

#Frame für den oberen Teil
frame_top = tk.Frame(master=root, bg='#E9EDC9')
frame_top.pack(side='top', padx=5, pady=5)

#Input-Fenster
input_window = tk.Entry(
    master=frame_top, borderwidth='0', highlightbackground='#E9EDC9')
input_window.configure(bg='#CCD5AE')
input_window.pack(side='left', padx=5, pady=5)
input_window.bind('<Return>', enter)

#Enter-Button
enter = tk.Button(master=frame_top, text="ENTER",
                    highlightbackground='#E9EDC9', command=enter)
enter.pack(side='right')

#Ausgabe-Fenster
output = tk.Text(root, bg='#E9EDC9')
output.config(state='disable', highlightbackground='#E9EDC9',
              font=("Helvetica", 14))

output.pack(side='bottom', padx=5, pady=5)





root.mainloop()



