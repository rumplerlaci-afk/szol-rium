# Szolárium időpontfoglaló 

Hallgató: Rumpler László QTP1EH (RL)

## Rövid leírás
Egyszerű szolárium időpontfoglaló. A felületen bal oldalt a szabad időpontok láthatók, alul a foglalás gombbal rögzíthetőek. Jobb oldalon külön mezőben adható meg a vezetéknév és keresztnév. Az alap idősávok: 13:00-13:15, 13:20-13:35, 13:40-13:55. Foglaláskor CSV fájlba kerül a név, dátum és idősáv.

## Feladatok teljesítése 
- Tanult modul: `csv`, `datetime`, `os`, `tkinter`
- Bemutatandó modul (3 függvény példa): `os` és `csv` alap műveletek bemutatása a README-ben
- Saját modul: `rl_solar_utils.py`
- Saját osztály: `RLSolarApp`
- Saját függvények (monogrammal): `RL_default_slots`, `RL_format_name`, `RL_save_csv`
- Grafikai modul: Tkinter
- Eseménykezelés: Enterrel foglalás, Listbox kiválasztás, gombnyomás
- Indítás: `main.py`, ablaknév: `app`

## Indítás
- `python main.py` 
- A foglalások a `data/foglalasok.csv` fájlba kerülnek.
