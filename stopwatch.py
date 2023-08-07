import tkinter as tk
import time

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch App")

        self.is_running = False
        self.start_time = None
        self.elapsed_time = 0

        self.time_label = tk.Label(root, text="00:00.0", font=("Helvetica", 48))
        self.time_label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.hold_button = tk.Button(root, text="Hold", command=self.hold)
        self.hold_button.pack(side=tk.LEFT, padx=10)

        self.update_time()

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.start_time = time.time() - self.elapsed_time
            self.update_time()

    def stop(self):
        if self.is_running:
            self.is_running = False
            self.elapsed_time = time.time() - self.start_time
            self.update_time()

    def hold(self):
        self.is_running = False
        self.update_time()

    def update_time(self):
        if self.is_running:
            elapsed = time.time() - self.start_time + self.elapsed_time
        else:
            elapsed = self.elapsed_time

        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        milliseconds = int((elapsed - int(elapsed)) * 10)

        time_text = f"{minutes:02}:{seconds:02}.{milliseconds}"
        self.time_label.config(text=time_text)

        self.root.after(100, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()
