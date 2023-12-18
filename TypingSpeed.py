import tkinter as tk
from tkinter import ttk
import time

class TypingSpeedTesterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Speed Tester")
        self.master.geometry("600x400")
        self.master.configure(bg="#f0f0f0")

        self.style = ttk.Style()
        self.style.theme_use("clam")

        main_frame = ttk.Frame(self.master, style='TFrame')
        main_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

        self.sentence = (
            "The joy of coding Python. \n"
            "Unlock your creativity with programming.\n"
            "Coding is the language of the future! \n"
        )
        ttk.Label(main_frame, text="Type the following sentences one by one:", style='Header.TLabel').pack(pady=10)
        ttk.Label(main_frame, text=self.sentence, style='TLabel').pack(pady=10)

        self.text_widget = tk.Text(main_frame, wrap=tk.WORD, height=5, width=40, font=("Helvetica", 12))
        self.text_widget.pack(pady=10)

        ttk.Button(main_frame, text="Start Typing Test", command=self.start_typing_test, style='TButton').pack(pady=5)
        ttk.Button(main_frame, text="Reset", command=self.reset, style='TButton').pack(pady=5)

        self.result_label = ttk.Label(main_frame, text="", style='TLabel')
        self.result_label.pack(pady=10)

        self.timer_label = ttk.Label(main_frame, text="", font=("Helvetica", 12), style='TLabel')
        self.timer_label.pack()

        self.start_time = 0
        self.timer_running = False

    def start_typing_test(self):
        if not self.timer_running:
            self.text_widget.delete(1.0, tk.END)
            self.result_label.config(text="")
            self.start_time = time.time()
            self.timer_running = True
            self.master.after(1000, self.update_timer)

    def update_timer(self):
        elapsed_time = int(time.time() - self.start_time)
        remaining_time = max(60 - elapsed_time, 0)

        self.timer_label.config(text=f"Time left: {remaining_time} seconds")

        if remaining_time > 0 and self.timer_running:
            self.master.after(1000, self.update_timer)
        else:
            self.end_typing_test()

    def end_typing_test(self):
        self.timer_running = False

        typed_text = self.text_widget.get("1.0", tk.END)
        words_per_minute = (len(typed_text.split()) / 60) * 60

        accuracy = self.calculate_accuracy(typed_text, self.sentence)

        result_text = f"Typing Speed: {words_per_minute:.2f} words per minute\nAccuracy: {accuracy:.2f}%"
        self.result_label.config(text=result_text)

    def reset(self):
        self.timer_running = False
        self.text_widget.delete(1.0, tk.END)
        self.result_label.config(text="")
        self.timer_label.config(text="")

    def calculate_accuracy(self, typed_text, original_text):
        correct_words = sum(a == b for a, b in zip(typed_text.split(), original_text.split()))
        total_words = len(original_text.split())
        accuracy_percentage = (correct_words / total_words) * 100
        return accuracy_percentage

if __name__ == "__main__":
    root = tk.Tk()

    root.tk_setPalette(background='#f0f0f0', foreground='#000000', activeBackground='#d3e0ea', activeForeground='#000000')

    app = TypingSpeedTesterApp(root)
    root.mainloop()
