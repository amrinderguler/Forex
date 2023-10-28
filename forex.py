import tkinter as tk
from tkinter import ttk, Label, Entry, Button
from forex_python.converter import CurrencyRates

# Create the main application window
window = tk.Tk()
window.title("Currency Converter")

# Create and configure the widgets
amount_label = Label(window, text="Amount:", font=('Arial', 14))
amount_label.grid(row=0, column=0, padx=10, pady=10)

amount_field = Entry(window, font=('Arial', 14), borderwidth=5, relief='ridge', justify='center')
amount_field.grid(row=0, column=1, padx=10, pady=10)

from_currency_label = Label(window, text="From Currency:", font=('Arial', 14))
from_currency_label.grid(row=1, column=0, padx=10, pady=10)

from_currency = ttk.Combobox(window, width=27)
from_currency.grid(column=1, row=1)
from_currency.current()

to_currency_label = Label(window, text="To Currency:", font=('Arial', 14))
to_currency_label.grid(row=2, column=0, padx=10, pady=10)

to_currency = ttk.Combobox(window, width=27)
to_currency.grid(column=1, row=2)
to_currency.current()

result_label = Label(window, text="", font=('Arial', 14))
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

def convert_currency():
    try:
        amount = float(amount_field.get())
    except ValueError:
        result_label.config(text="Enter a valid amount", fg="red")
        return

    from_curr = from_currency.get()
    to_curr = to_currency.get()

    c = CurrencyRates()
    converted_amount = c.convert(from_curr, to_curr, amount)
    result_label.config(text=f"Converted Amount: {converted_amount} {to_curr}", fg="green")

convert_button = Button(window, text="Convert", font=('Arial', 14), command=convert_currency)
convert_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
window.mainloop()