import tkinter as tk


root = tk.Tk()
root.configure(bg='#E9EDC9')
root.title("Collatz Conjecture")
root.geometry('300x450')



def enter_bind():
    enter()

def enter():
    x = int(input_window.get())
    x1 = x
    output_ungerade.config(state='normal')
    output_gerade.config(state='normal')

    output_ungerade.delete(1.0, tk.END)
    output_gerade.delete(1.0, tk.END)
    
    if x1 % 2:  # ungerade
        output_ungerade.insert(tk.END, '➡')
        output_ungerade.insert(tk.END, x1)
        output_ungerade.insert(tk.END, '\n')

    else:
        output_gerade.insert(tk.END, '➡')
        output_gerade.insert(tk.END, x1)
        output_gerade.insert(tk.END, '\n')


    while x1 > 1:
        

    
        if x1 % 2:  # ungerade
            x1 = x1 * 3 + 1
            input_window.delete(0, tk.END)
            output_ungerade.insert(tk.END, x1)
            output_ungerade.insert(tk.END, '\n' + '➡')
            output_gerade.insert(tk.END, '➡')

            
        else:
            x1 = x1 / 2
            input_window.delete(0, tk.END)
            output_gerade.insert(tk.END, x1)
            output_gerade.insert(tk.END, '\n' + '➡')
            output_ungerade.insert(tk.END, '➡')

    output_gerade.config(state='disable')
    output_ungerade.config(state='disable')
            

#Frame für den oberen Teil
frame_top = tk.Frame(master=root, bg='#E9EDC9')
frame_top.pack(side='top', padx=5, pady=5)

#Input-Fenster
input_window = tk.Entry(
    master=frame_top, borderwidth='0', highlightbackground='#E9EDC9')
input_window.configure(bg='#CCD5AE')
input_window.pack(side='left', padx=5, pady=5)




#Enter-Button
enter = tk.Button(master=frame_top, text="ENTER",
                    highlightbackground='#E9EDC9', command=enter)
enter.pack(side='right')

#frame
frame = tk.Frame(root)
frame.pack(side='bottom')

#Ausgabe-Fenster_gerade
output_gerade = tk.Text(master=frame, bg='#E9EDC9')
output_gerade.config(state='disable', highlightbackground='#E9EDC9',
              font=("Helvetica", 14), width='15')

output_gerade.pack(side='left', padx=5, pady=5,)

#Ausgabe-Fenster_ungerade
output_ungerade = tk.Text(master=frame, bg='#E9EDC9')
output_ungerade.config(state='disable', highlightbackground='#E9EDC9',
              font=("Helvetica", 14), width='15')

output_ungerade.pack(side='right', padx=5, pady=5)


root.bind('<Return>', enter_bind)
root.mainloop()



