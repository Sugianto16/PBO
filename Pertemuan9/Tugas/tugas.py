import tkinter as tk
from tkinter import Label, Entry, Button, W, OptionMenu, StringVar

class AplikasiKonversiSuhu:
    def __init__(self, master):
        self.master = master
        master.title("Aplikasi Konversi Suhu")

        # Label Nama
        self.nama_label = Label(master, text="Sugianto Tegar Samudra (220511162)")
        self.nama_label.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        # Entry untuk suhu
        self.label_suhu_awal = Label(master, text="Suhu Awal:")
        self.label_suhu_awal.grid(row=1, column=0, padx=10, pady=10)
        self.entry_suhu = Entry(master)
        self.entry_suhu.grid(row=1, column=1, padx=10, pady=10)

        # Combobox untuk satuan suhu awal
        self.label_suhu_awal = Label(master, text="Satuan Awal:")
        self.label_suhu_awal.grid(row=2, column=0, padx=10, pady=10)
        self.satuan_suhu_awal = ["Celsius", "Fahrenheit", "Kelvin", "Reamur"]
        self.combo_suhu_awal = StringVar()
        self.combo_suhu_awal.set(self.satuan_suhu_awal[0])
        self.dropdown_suhu_awal = OptionMenu(master, self.combo_suhu_awal, *self.satuan_suhu_awal)
        self.dropdown_suhu_awal.grid(row=2, column=1, padx=10, pady=10)

        # Combobox untuk satuan suhu tujuan
        self.label_suhu_tujuan = Label(master, text="Satuan Tujuan:")
        self.label_suhu_tujuan.grid(row=3, column=0, padx=10, pady=10)
        self.satuan_suhu_tujuan = ["Celsius", "Fahrenheit", "Kelvin", "Reamur"]
        self.combo_suhu_tujuan = StringVar()
        self.combo_suhu_tujuan.set(self.satuan_suhu_tujuan[1])
        self.dropdown_suhu_tujuan = OptionMenu(master, self.combo_suhu_tujuan, *self.satuan_suhu_tujuan)
        self.dropdown_suhu_tujuan.grid(row=3, column=1, padx=10, pady=10)

        # Tombol Konversi
        self.tombol_konversi = Button(master, text="Konversi", command=self.konversi_suhu)
        self.tombol_konversi.grid(row=4, column=0, columnspan=2, pady=10)

        # Label hasil
        self.label_hasil = Label(master, text="Hasil Konversi:")
        self.label_hasil.grid(row=5, column=0, columnspan=2, pady=10)

        # Tombol Reset
        self.tombol_reset = Button(master, text="Reset", command=self.reset)
        self.tombol_reset.grid(row=6, column=0, columnspan=2, pady=10)

    def konversi_suhu(self):
        try:
            suhu_input = float(self.entry_suhu.get())
            satuan_awal = self.combo_suhu_awal.get()
            satuan_tujuan = self.combo_suhu_tujuan.get()

            if satuan_awal == "Celsius":
                if satuan_tujuan == "Fahrenheit":
                    suhu_output = (suhu_input * 9/5) + 32
                elif satuan_tujuan == "Kelvin":
                    suhu_output = suhu_input + 273.15
                elif satuan_tujuan == "Reamur":
                    suhu_output = suhu_input * 4/5
                else:
                    suhu_output = suhu_input
            elif satuan_awal == "Fahrenheit":
                if satuan_tujuan == "Celsius":
                    suhu_output = (suhu_input - 32) * 5/9
                elif satuan_tujuan == "Kelvin":
                    suhu_output = (suhu_input - 32) * 5/9 + 273.15
                elif satuan_tujuan == "Reamur":
                    suhu_output = (suhu_input - 32) * 4/9
                else:
                    suhu_output = suhu_input
            elif satuan_awal == "Kelvin":
                if satuan_tujuan == "Celsius":
                    suhu_output = suhu_input - 273.15
                elif satuan_tujuan == "Fahrenheit":
                    suhu_output = (suhu_input - 273.15) * 9/5 + 32
                elif satuan_tujuan == "Reamur":
                    suhu_output = (suhu_input - 273.15) * 4/5
                else:
                    suhu_output = suhu_input
            elif satuan_awal == "Reamur":
                if satuan_tujuan == "Celsius":
                    suhu_output = suhu_input * 5/4
                elif satuan_tujuan == "Fahrenheit":
                    suhu_output = suhu_input * 9/4 + 32
                elif satuan_tujuan == "Kelvin":
                    suhu_output = suhu_input * 5/4 + 273.15
                else:
                    suhu_output = suhu_input
            else:
                suhu_output = suhu_input

            self.label_hasil.config(text=f"Hasil Konversi: {suhu_output:.2f} {satuan_tujuan}")
        except ValueError:
            self.label_hasil.config(text="Masukkan suhu dengan benar!")

    def reset(self):
        self.entry_suhu.delete(0, tk.END)
        self.combo_suhu_awal.set(self.satuan_suhu_awal[0])
        self.combo_suhu_tujuan.set(self.satuan_suhu_tujuan[1])
        self.label_hasil.config(text="Hasil Konversi:")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiKonversiSuhu(root)
    root.mainloop()