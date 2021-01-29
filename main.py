from tkinter import *

typing = False


def started_typing(event):
    global typing
    # I need to check this on first call of this function as it
    # appears to get called even before a key is physically pressed.
    if typing:
        timer_text.config(text="")
        global count_timer
        if count_timer:
            window.after_cancel(count_timer)
        count_timer = window.after(5000, will_disappear)
    else:
        typing = True


def will_disappear():
    timer_text.config(text="Still there??")
    global count_timer
    if count_timer:
        window.after_cancel(count_timer)
    count_timer = window.after(5000, timed_out)


def timed_out():
    global typing
    timer_text.config(text="Sorry, it's gone.\n\nMight as well start again...")
    typed_word.delete('1.0', END)
    typing = False


# ------- SET UP UI ------- #
window = Tk()
window.title("Panic")
window.config(padx=20, pady=20)
window.minsize(width=410, height=400)

timer_text = Label(text="Start typing when you're ready...")
timer_text.grid(row=0, column=0)

typed_word = Text(window, height=25, width=50, font=('times', 20), wrap=WORD)
typed_word.grid(row=1, column=0, pady=20)
typed_word.focus()

count_timer = None
window.bind("<Key>", started_typing)

window.mainloop()
