import tkinter as tk
from rl_solar_gui import RLSolarApp

def main():
    root = tk.Tk()
    root.title("Szolárium – Időpontfoglaló")
    app = RLSolarApp(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()
