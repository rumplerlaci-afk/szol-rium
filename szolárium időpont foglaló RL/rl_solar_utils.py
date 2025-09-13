import os
import csv
from datetime import datetime

def RL_default_slots():
    return ["13:00-13:15","13:20-13:35","13:40-13:55"]

def RL_format_name(vezetek, kereszt):
    v=(vezetek or "").strip().title()
    k=(kereszt or "").strip().title()
    return f"{v} {k}".strip()

def RL_save_csv(path, row):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    new = not os.path.exists(path)
    with open(path, "a", newline="", encoding="utf-8") as f:
        import csv as _c
        w = _c.writer(f, delimiter=";")
        if new:
            w.writerow(["datum","nev","idopont"])
        w.writerow(row)
