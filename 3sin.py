import time
import tkinter as tk

def to_ternary(num):
    if num == 0:
        return '0'
    ternary = ''
    while num > 0:
        num, remainder = divmod(num, 3)
        ternary = str(remainder) + ternary
    return ternary

def update_time():
    current_time = time.localtime()
    hour = to_ternary(current_time.tm_hour)
    minute = to_ternary(current_time.tm_min)
    second = to_ternary(current_time.tm_sec)
    time_label.config(text=f"現在時刻は{hour.zfill(2)}:{minute.zfill(2)}:{second.zfill(2)}です。")
    root.after(1000, update_time)

def stop_program():
    root.destroy()

root = tk.Tk()
root.title("3進法時計")


time_label = tk.Label(root, font=("Helvetica", 24))
time_label.pack(padx=20, pady=20)

stop_button = tk.Button(root, text="終了", command=stop_program)
stop_button.pack(pady=10)

update_time()
root.mainloop()