from tkinter import *

is_typing = False
count_timer = None


def started_typing(event):
    global is_typing
    global count_timer
    # I need to check this on first call of this function as it
    # appears to get called even before a key is physically pressed.
    if is_typing:
        hint_text.config(text="")
        if count_timer:
            window.after_cancel(count_timer)
        count_timer = window.after(5000, will_disappear)
    else:
        is_typing = True


def will_disappear():
    global count_timer
    hint_text.config(text="Still there??")
    if count_timer:
        window.after_cancel(count_timer)
    count_timer = window.after(5000, timed_out)


def timed_out():
    global is_typing
    hint_text.config(text="Sorry, it's gone.\n\nMight as well start again...")
    input_text.delete('1.0', END)
    is_typing = False


# ------- SET UP UI ------- #
window = Tk()
window.title("Panic")
window.config(padx=20, pady=20)
window.minsize(width=410, height=400)
window.bind("<Key>", started_typing)

hint_text = Label(text="Start typing when you're ready...")
hint_text.grid(row=0, column=0)

input_text = Text(window, height=25, width=50, font=('times', 20), wrap=WORD)
input_text.grid(row=1, column=0, pady=20)
input_text.focus()


window.mainloop()
