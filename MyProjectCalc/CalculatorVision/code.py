from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("315x510")
window.resizable(False,False)
window.config(bg="dark blue")
window.iconbitmap("calculator.ico")

entry = Entry(window,width= 200  , font = ("Arial", 40,))
entry.pack(anchor= "w" , padx=10, pady = 15)

frame = Frame(window)
frame.pack(anchor="w", padx=10,pady=1)


btn_clear = Button(frame,
                   text = "CLEAR",
                   font = ("Comic Sans MS",15),
                   width = 10,
                   height = 2,
                   bg = "gray")

btn_clear.pack(side="left", padx = 0)

# backspace_img = PhotoImage(file = "backspace.png")
# backspace_img = backspace_img.zoom(3, 1)
btn_backspace = Button(frame,
                       # image = backspace_img,
                       text = "BACK",
                       font = ("Comic Sans MS",15),
                       width = 10,
                       height = 2,
                       bg = "pink")

btn_backspace.pack(side = "left", padx=0)

btn_div = Button(frame,
                 text = ":",
                 font = ("Comic Sans MS",15),
                 width = 5,
                 height = 2 ,
                 bg = "pink")

btn_div.pack(side = "left", padx = 0)

frame2 = Frame(window)
frame2.pack(anchor = "w", padx=10)

btn_7 = Button(frame2,
               text = "7",
               font = ("Comic Sans MS",15),
               width = 5,
               height = 2,
               bg = "pink")

btn_7.pack(side = "left", padx=0)

btn_8 = Button(frame2,
               text = "8",
               font = ("Comic Sans MS",15),
               width = 5,
               height = 2,
               bg = "pink")

btn_8.pack(side = "left", padx=0)

btn_9 = Button(frame2,
               text = "9",
               font = ("Comic Sans MS",15),
               width = 5,
               height = 2,
               bg = "pink")

btn_9.pack(side = "left", padx=0)

btn_x = Button(frame2,
               text = "x",
               font = ("Comic Sans MS",15),
               width = 5,
               height = 2,
               bg = "pink")

btn_x.pack(side = "left", padx=0)


frame3 = Frame(window)
frame3.pack(anchor = "w", padx = 10)

btn_4 = Button(frame3,
               text = "4",
               font = ("Comic Sans MS",15),
               width = 5,
               height = 2,
               bg = "pink")

btn_4.pack(side = "left", padx = 0)


btn_5 = Button(frame3,
               text = "5",
               font = ("Comic Sans MS",15),
               width = 5,
               height = 2,
               bg = "pink")

btn_5.pack(side = "left" , padx = 0)


btn_6 = Button(frame3,
               text = "6",
               font = ("Comic Sans MS",15),
               width = 5,
               height = 2,
               bg = "pink")

btn_6.pack(side = "left", padx=0)

btn_minus = Button(frame3,
                   text = "-",
                   font = ("Comic Sans MS",15),
                   width = 5,
                   height = 2,
                   bg = "pink")

btn_minus.pack(side = "left", padx=0)


frame4 = Frame(window)
frame4.pack(anchor = "w", padx= 10)


btn_1 = Button(frame4,
               text = "1",
               font = ("Comic Sans MS",15),
               width = 5,
               height = 2,
               bg = "pink")

btn_1.pack(side = "left", padx=0)


btn_2 = Button(frame4,
               text = "2",
               font = ("Comic Sans MS",15),
               width = 5,
               height = 2,
               bg = "pink")

btn_2.pack(side = "left", padx=0)

btn_3 = Button(frame4,
               text = "3",
               font = ("Comic Sans MS",15),
               width = 5,
               height = 2,
               bg = "pink")

btn_3.pack(side = "left", padx=0)


btn_plus = Button(frame4,
               text = "+",
               font = ("Comic Sans MS",15),
               width = 5,
               height = 2,
               bg = "pink")

btn_plus.pack(side = "left", padx=0)


frame5 = Frame(window)
frame5.pack(anchor = "w", padx=10)



btn_plus_minus = Button(frame5,
               text = "+/-",
               font = ("Comic Sans MS",15),
               width = 5,
               height = 2,
               bg = "pink")

btn_plus_minus.pack(side = "left", padx=0)



btn_0 = Button(frame5,
               text = "0",
               font = ("Comic Sans MS",15),
               width = 5,
               height = 2,
               bg = "pink")

btn_0.pack(side = "left", padx=0)


btn_point = Button(frame5,
               text = ".",
               font = ("Comic Sans MS",15),
               width = 5,
               height = 2,
               bg = "pink")

btn_point.pack(side = "left", padx=0)


btn_equal = Button(frame5,
               text = "=",
               font = ("Comic Sans MS",15),
               width = 5,
               height = 2,
               bg = "grey")

btn_equal.pack(side = "left", padx=0)


# text1 = Label(window,
#               text = "Standart",
#               font = ("Arial", 20,"bold"),
#               fg = "white",
#               bg = "dark blue")
#
# text1.pack(anchor= "w" ,padx=20,pady=20)


window.mainloop()