import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W

def konversi_suhu():
    try:
        suhu_input = float(entry_suhu.get())
        satuan_awal = combo_suhu_awal.get()
        satuan_tujuan = combo_suhu_tujuan.get()

        if satuan_awal == "Celsius":
            if satuan_tujuan == "Fahrenheit":
                suhu_output = (suhu_input * 9/5) + 32
            elif satuan_tujuan == "Kelvin":
                suhu_output = suhu_input + 273.15
            else:
                suhu_output = suhu_input
        elif satuan_awal == "Fahrenheit":
            if satuan_tujuan == "Celsius":
                suhu_output = (suhu_input - 32) * 5/9
            elif satuan_tujuan == "Kelvin":
                suhu_output = (suhu_input - 32) * 5/9 + 273.15
            else:
                suhu_output = suhu_input
        elif satuan_awal == "Kelvin":
            if satuan_tujuan == "Celsius":
                suhu_output = suhu_input - 273.15
            elif satuan_tujuan == "Fahrenheit":
                suhu_output = (suhu_input - 273.15) * 9/5 + 32
            else:
                suhu_output = suhu_input
        else:
            suhu_output = suhu_input

        label_hasil.config(text=f"Hasil Konversi: {suhu_output:.2f} {satuan_tujuan}")
    except ValueError:
        label_hasil.config(text="Masukkan suhu dengan benar!")

# Membuat window
window = tk.Tk()
window.title("Aplikasi Konversi Suhu")

#Label Nama
Nama =tk.Label(window, text="Sugianto Tegar Samudra (220511162)")
Nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Membuat label dan entry untuk suhu awal
label_suhu_awal = tk.Label(window, text="Suhu Awal:")
label_suhu_awal.grid(row=1, column=0, padx=10, pady=10)
entry_suhu = tk.Entry(window)
entry_suhu.grid(row=1, column=1, padx=10, pady=10)

# Membuat label dan combobox untuk satuan suhu awal
label_suhu_awal = tk.Label(window, text="Satuan Awal:")
label_suhu_awal.grid(row=2, column=0, padx=10, pady=10)
satuan_suhu_awal = ["Celsius", "Fahrenheit", "Kelvin"]
combo_suhu_awal = tk.StringVar()
combo_suhu_awal.set(satuan_suhu_awal[0])
dropdown_suhu_awal = tk.OptionMenu(window, combo_suhu_awal, *satuan_suhu_awal)
dropdown_suhu_awal.grid(row=2, column=1, padx=10, pady=10)

# Membuat label dan combobox untuk satuan suhu tujuan
label_suhu_tujuan = tk.Label(window, text="Satuan Tujuan:")
label_suhu_tujuan.grid(row=3, column=0, padx=10, pady=10)
satuan_suhu_tujuan = ["Celsius", "Fahrenheit", "Kelvin"]
combo_suhu_tujuan = tk.StringVar()
combo_suhu_tujuan.set(satuan_suhu_tujuan[1])
dropdown_suhu_tujuan = tk.OptionMenu(window, combo_suhu_tujuan, *satuan_suhu_tujuan)
dropdown_suhu_tujuan.grid(row=3, column=1, padx=10, pady=10)

# Membuat tombol konversi
tombol_konversi = tk.Button(window, text="Konversi", command=konversi_suhu)
tombol_konversi.grid(row=4, column=0, columnspan=2, pady=10)

# Membuat label hasil konversi
label_hasil = tk.Label(window, text="Hasil Konversi:")
label_hasil.grid(row=5, column=0, columnspan=2, pady=10)

def reset():
    entry_suhu.delete(0, tk.END)
    combo_suhu_awal.set(satuan_suhu_awal[0])
    combo_suhu_tujuan.set(satuan_suhu_tujuan[1])
    label_hasil.config(text="Hasil Konversi:")
    
# Menambahkan tombol reset
tombol_reset = tk.Button(window, text="Reset", command=reset)
tombol_reset.grid(row=6, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
window.mainloop()