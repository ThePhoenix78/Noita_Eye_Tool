import tkinter as tk
from tkinter import messagebox
from lumikki import codes, format_data, encode_data_trinome, to_int_list, to_numbers

res: list = [0]


def update_window():
    symbol = entry_symbol.get()
    chaine1 = entry_chaine1.get()
    chaine2 = entry_chaine2.get()
    encoding = entry_encoding.get()
    encoding = encoding.replace(" ", "-")

    try:
        base = int(entry_entier.get())
    except ValueError:
        messagebox.showerror("Error", "Enter a valid int")
        return

    try:
        offset = int(entry_offset.get())
    except ValueError:
        offset = "no"

    data: str = b""

    for code in codes:
        code = to_numbers(code, symbol)
        temp: list = encode_data_trinome(data=to_int_list(code), base=base, mode=[chaine1, chaine2])
        data += format_data(data=temp, offset=offset, encoding=encoding) + b"\n"

    text_resultat.delete(1.0, tk.END)
    text_resultat.insert(tk.END, data)
    res[0] = data

    # root.clipboard_clear()
    # root.clipboard_append(data)


def copy_to():
    root.clipboard_clear()
    root.clipboard_append(res[0])


root = tk.Tk()
root.title("Lumikki tool")

label_symbol = tk.Label(root, text="Symbol order (•↑→↓←)")
label_symbol.pack(pady=[15, 5])

entry_symbol = tk.Entry(root, justify="center")
entry_symbol.insert(0, "01234")
entry_symbol.pack(padx=50)

label_chaine1 = tk.Label(root, text="First group")
label_chaine1.pack(pady=[7, 5])

entry_chaine1 = tk.Entry(root, justify="center")
entry_chaine1.insert(0, "lrb")
entry_chaine1.pack(padx=50)

label_chaine2 = tk.Label(root, text="Second group")
label_chaine2.pack(pady=[7, 5])

entry_chaine2 = tk.Entry(root, justify="center")
entry_chaine2.insert(0, "rlt")
entry_chaine2.pack(padx=50)

label_entier = tk.Label(root, text="Base")
label_entier.pack(pady=[7, 5])

entry_entier = tk.Entry(root, justify="center")
entry_entier.insert(0, "5")
entry_entier.pack(padx=50)

label_offset = tk.Label(root, text="Offset (leave empyt to not convert into text)")
label_offset.pack(pady=[7, 5])

entry_offset = tk.Entry(root, justify="center")
entry_offset.insert(0, "32")
entry_offset.pack(padx=50, pady=[7, 5])

label_encoding = tk.Label(root, text="Encoding")
label_encoding.pack(pady=[7, 5])

entry_encoding = tk.Entry(root, justify="center")
entry_encoding.insert(0, "utf-8")
entry_encoding.pack(padx=50, pady=[0, 7])

button_concatener = tk.Button(root, text="Generate", command=update_window)
button_concatener.pack(pady=[10, 10])

text_resultat = tk.Text(root, width=145, height=12, wrap=tk.WORD)
text_resultat.pack(fill='x', padx=50, pady=10)

button_copy = tk.Button(root, text="Copy", command=copy_to)
button_copy.pack(pady=[7, 20])

# root.geometry("950x600")
root.mainloop()
