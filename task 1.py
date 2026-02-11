from tkinter import *
window = Tk()
window.title("Event handler")
window.geometry("100x100")
def handl_keypress(event):
    print("Key pressed: ", event.char)
window.bind("<KeyPress>", handl_keypress)
def handle_click(event):
    print("\nMouse clicked at: ", event.x, event.y)
button = Button(text = "Click me")
button.pack()
button.bind("<Button-1>", handle_click)
window.mainloop()
