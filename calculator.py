import tkinter as tk
main_window = tk.Tk()
main_window.title("Basic Calculator")
main_window.geometry("312x324")


#Global variable
expression = ""
input_text = tk.StringVar()

#create 3 functions
#function to handle number/operation button click
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# function to clear the input field
def btn_clear():
    global expression
    expression = ""
    input_text.set("")

#function to evaluate the expression
def btn_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = ""
    except:
        input_text.set("Error")
        expression = ""

#Creating frames to organize the widgets
#top frame
input_frame = tk.Frame(main_window, width = 312, height = 50, bd = 0, highlightbackground="black",
                     highlightcolor="black", highlightthickness=1)
#pact the frame using pack ()
input_frame.pack(side= 'top')

#entry to widget to be placed in this frame
input_field = tk.Entry(input_frame, font = ("Arial", 18, 'bold'),
                       textvariable = input_text, width=50, bg= "#eee", bd=0, justify="right")

input_field.pack(ipady=10)

#buttons frame
btns_frame = tk.Frame(main_window, width=312, height=50, bd=0, bg="grey")
btns_frame.pack()



btn_clearing = tk.Button(btns_frame, text="Clear", fg="black", width=32, height=3,
                         bd=0, bg="#eee", cursor="hand2", command=btn_clear)

btn_clearing.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

btn_div = tk.Button(btns_frame, text="/", fg="black", width=10, height=3,
                    bd=0, bg="#eee", cursor="hand2",
                    command=lambda: btn_click("/"))
btn_div.grid(row=0, column=3, padx=1, pady=1)

btn_7 = tk.Button(btns_frame, text="7", fg="black", width=10, height=3,
                  bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(7))
btn_7.grid(row=1, column=0, padx=1, pady=1)

btn_8 = tk.Button(btns_frame, text="8", fg="black", width=10, height=3,
                  bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(8))
btn_8.grid(row=1, column=1, padx=1, pady=1)

btn_9 = tk.Button(btns_frame, text="9", fg="black", width=10, height=3,
                  bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(9))
btn_9.grid(row=1, column=2, padx=1, pady=1)

btn_mul = tk.Button(btns_frame, text="*", fg="black", width=10, height=3,
                    bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("*"))
btn_mul.grid(row=1, column=3, padx=1, pady=1)

btn_4 = tk.Button(btns_frame, text="4", fg="black", width=10, height=3,
                  bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(4))
btn_4.grid(row=2, column=0, padx=1, pady=1)

btn_5 = tk.Button(btns_frame, text="5", fg="black", width=10, height=3,
                  bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(5))
btn_5.grid(row=2, column=1, padx=1, pady=1)

btn_6 = tk.Button(btns_frame, text="6", fg="black", width=10, height=3,
                  bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(6))
btn_6.grid(row=2, column=2, padx=1, pady=1)

btn_sub = tk.Button(btns_frame, text="-", fg="black", width=10, height=3,
                    bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("-"))
btn_sub.grid(row=2, column=3, padx=1, pady=1)


btn_1 = tk.Button(btns_frame, text="1", fg="black", width=10, height=3,
                  bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(1))
btn_1.grid(row=3, column=0, padx=1, pady=1)

btn_2 = tk.Button(btns_frame, text="2", fg="black", width=10, height=3,
                  bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(2))
btn_2.grid(row=3, column=1, padx=1, pady=1)

btn_3 = tk.Button(btns_frame, text="3", fg="black", width=10, height=3,
                  bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(3))
btn_3.grid(row=3, column=2, padx=1, pady=1)

btn_add = tk.Button(btns_frame, text="+", fg="black", width=10, height=3,
                    bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("+"))
btn_add.grid(row=3, column=3, padx=1, pady=1)


btn_0 = tk.Button(btns_frame, text="0", fg="black", width=21, height=3,
                  bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(0))
btn_0.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

btn_dot = tk.Button(btns_frame, text=".", fg="black", width=10, height=3,
                    bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("."))
btn_dot.grid(row=4, column=2, padx=1, pady=1)

btn_eq = tk.Button(btns_frame, text="=", fg="black", width=10, height=3,
                   bd=0, bg="#eee", cursor="hand2", command=btn_equal)
btn_eq.grid(row=4, column=3, padx=1, pady=1)





main_window.mainloop()
