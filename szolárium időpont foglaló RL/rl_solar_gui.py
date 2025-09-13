import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
from rl_solar_utils import RL_default_slots, RL_format_name, RL_save_csv

class RLSolarApp(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master, padding=10)
        self.master = master
        self.pack(fill="both", expand=True)
        self._build_ui()
        self._bind_events()
        self._refresh_slots()

    def _build_ui(self):
        root = self
        left = ttk.Frame(root); left.pack(side="left", fill="both", expand=True, padx=(0,10))
        right = ttk.Frame(root, width=260); right.pack(side="left", fill="y")
        left_top = ttk.LabelFrame(left, text="Szabad időpontok"); left_top.pack(fill="x")
        self.date_var = tk.StringVar(value=str(date.today()))
        ttk.Label(left_top, textvariable=self.date_var).pack(anchor="w", padx=10, pady=6)
        left_mid = ttk.LabelFrame(left, text="Idősávok"); left_mid.pack(fill="both", expand=True, pady=(8,0))
        self.slot_list = tk.Listbox(left_mid, height=8, activestyle="dotbox")
        self.slot_list.pack(fill="both", expand=True, padx=6, pady=6)
        sb = ttk.Scrollbar(left_mid, orient="vertical", command=self.slot_list.yview); sb.pack(side="right", fill="y")
        self.slot_list.config(yscrollcommand=sb.set)
        self.book_btn = ttk.Button(left, text="Időpont foglalása", command=self._book); self.book_btn.pack(anchor="w", pady=(8,0))
        right_box = ttk.LabelFrame(right, text="Ügyfél adatok"); right_box.pack(fill="x")
        ttk.Label(right_box, text="Vezetéknév:").pack(anchor="w", padx=8, pady=(8,0))
        self.last_var = tk.StringVar()
        ttk.Entry(right_box, textvariable=self.last_var).pack(fill="x", padx=8, pady=2)
        ttk.Label(right_box, text="Keresztnév:").pack(anchor="w", padx=8, pady=(8,0))
        self.first_var = tk.StringVar()
        ttk.Entry(right_box, textvariable=self.first_var).pack(fill="x", padx=8, pady=2)
        self.status = tk.StringVar(value="")
        ttk.Label(root, textvariable=self.status, anchor="w").pack(fill="x", pady=(8,0))

    def _bind_events(self):
        self.master.bind("<Return>", lambda e: self._book())

    def _refresh_slots(self):
        self.slot_list.delete(0,"end")
        for s in RL_default_slots():
            self.slot_list.insert("end", s)

    def _book(self):
        sel = self.slot_list.curselection()
        if not sel:
            messagebox.showerror("Hiba","Válassz időpontot.")
            return
        slot = self.slot_list.get(sel[0])
        nev = RL_format_name(self.last_var.get(), self.first_var.get())
        if not nev or " " not in nev:
            messagebox.showerror("Hiba","Add meg a vezeték- és keresztnevet.")
            return
        self.slot_list.delete(sel[0])
        path = "data/foglalasok.csv"
        RL_save_csv(path, [self.date_var.get(), nev, slot])
        self.status.set(f"Foglalva: {nev} • {slot}")
