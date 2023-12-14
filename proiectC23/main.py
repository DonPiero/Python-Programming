import math
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from playsound import playsound
import time


class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Temporizator")

        self.s = StringVar(root, value='0')
        self.m = StringVar(root, value='0')
        self.h = StringVar(root, value='0')

        self.hours_label = tk.Label(root, text="Ore:")
        self.hours_label.grid(row=0, column=0, padx=10, pady=10)

        self.hours_entry = tk.Entry(root, textvariable=self.h)
        self.hours_entry.grid(row=0, column=1, padx=10, pady=10)

        self.minutes_label = tk.Label(root, text="Minute:")
        self.minutes_label.grid(row=1, column=0, padx=10, pady=10)

        self.minutes_entry = tk.Entry(root, textvariable=self.m)
        self.minutes_entry.grid(row=1, column=1, padx=10, pady=10)

        self.seconds_label = tk.Label(root, text="Secunde:")
        self.seconds_label.grid(row=2, column=0, padx=10, pady=10)

        self.seconds_entry = tk.Entry(root, textvariable=self.s)
        self.seconds_entry.grid(row=2, column=1, padx=10, pady=10)

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.grid(row=3, column=0, columnspan=2, pady=10)

    def start_timer(self):
        try:
            hours = int(self.hours_entry.get())
            minutes = int(self.minutes_entry.get())
            seconds = int(self.seconds_entry.get())
        except ValueError:
            messagebox.showerror("Eroare", "Introduceti valori valide pentru ore, minute si secunde.")
            return

        total_seconds = hours * 3600 + minutes * 60 + seconds

        if total_seconds <= 0:
            messagebox.showerror("Eroare", "Introduceti o durata de timp mai mare decÃ¢t zero.")
            return

        self.start_button.config(state=tk.DISABLED)

        self.run_timer(total_seconds)

    def run_timer(self, total_seconds):
        while total_seconds > 0:
            time.sleep(1)
            total_seconds -= 1
            self.s.set(total_seconds % 60)
            self.m.set(math.floor(total_seconds / 60 % 60))
            self.h.set(math.floor(total_seconds / 3600))
            root.update()

        self.show_notification()

    def show_notification(self):
        playsound('buzzer.mp3', block=FALSE)
        messagebox.showinfo("Notificare", "Timpul s-a scurs!")
        self.start_button.config(state=tk.NORMAL)


if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
