import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES

class TranslatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Translator App")
        self.master.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        # Label
        self.label = ttk.Label(self.master, text="Enter text to translate:")
        self.label.pack(pady=10)

        # Text Entry
        self.entry = ttk.Entry(self.master, width=40)
        self.entry.pack(pady=10)

        # Language Dropdown
        self.languages = list(LANGUAGES.values())
        self.from_lang_var = tk.StringVar(value=self.languages[0])
        self.to_lang_var = tk.StringVar(value=self.languages[1])

        self.from_lang_label = ttk.Label(self.master, text="From Language:")
        self.from_lang_label.pack(pady=5)
        self.from_lang_dropdown = ttk.Combobox(self.master, textvariable=self.from_lang_var, values=self.languages)
        self.from_lang_dropdown.pack(pady=5)

        self.to_lang_label = ttk.Label(self.master, text="To Language:")
        self.to_lang_label.pack(pady=5)
        self.to_lang_dropdown = ttk.Combobox(self.master, textvariable=self.to_lang_var, values=self.languages)
        self.to_lang_dropdown.pack(pady=5)

        # Translate Button
        self.translate_button = ttk.Button(self.master, text="Translate", command=self.translate_text)
        self.translate_button.pack(pady=10)

        # Result Text
        self.result_text = tk.Text(self.master, height=6, width=40)
        self.result_text.pack(pady=10)

    def translate_text(self):
        text_to_translate = self.entry.get()
        translator = Translator()

        from_lang_code = [code for code, lang in LANGUAGES.items() if lang == self.from_lang_var.get()][0]
        to_lang_code = [code for code, lang in LANGUAGES.items() if lang == self.to_lang_var.get()][0]

        try:
            # Translate to the selected languages
            result_from_lang = translator.translate(text_to_translate, dest=from_lang_code).text
            result_to_lang = translator.translate(text_to_translate, dest=to_lang_code).text

            # Display results
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"{self.from_lang_var.get()}: {result_from_lang}\n")
            self.result_text.insert(tk.END, f"{self.to_lang_var.get()}: {result_to_lang}")

        except Exception as e:
            print(f"Error: {e}")
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Error during translation. Please try again.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()