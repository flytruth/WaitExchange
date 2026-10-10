import tkinter as tk
from tkinter import ttk
import requests

CURRENCY_MAP = {
    "USD": "USD - US Dollar",
    "EUR": "EUR - Euro",
    "AED": "AED - UAE Dirham",
    "BAM": "BAM - Bosnian Convertible Mark",
    "BTC": "BTC - Bitcoin",
    "USDT": "USDT - Tether",
    "GRAM": "GRAM - Gram Token",
    "STARS": "STARS - Telegram Stars",
    "GBP": "GBP - British Pound",
    "JPY": "JPY - Japanese Yen",
    "CAD": "CAD - Canadian Dollar",
    "AUD": "AUD - Australian Dollar",
    "CHF": "CHF - Swiss Franc",
    "CNY": "CNY - Chinese Yuan",
    "INR": "INR - Indian Rupee",
    "RUB": "RUB - Russian Ruble",
    "TRY": "TRY - Turkish Lira",
    "GEL": "GEL - Georgian Lari",
    "KZT": "KZT - Kazakhstani Tenge",
    "SAR": "SAR - Saudi Riyal",
    "BRL": "BRL - Brazilian Real",
    "MXN": "MXN - Mexican Peso",
    "KRW": "KRW - South Korean Won",
    "SGD": "SGD - Singapore Dollar",
    "AZN": "AZN - Azerbaijani Manat",
    "PLN": "PLN - Polish Zloty",
    "SEK": "SEK - Swedish Krona",
    "NOK": "NOK - Norwegian Krone",
}

DISPLAY_TO_CODE = {v: k for k, v in CURRENCY_MAP.items()}


class CurrencyConverter:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Universal Currency Converter')
        self.root.geometry('360x320')
        self.root.resizable(False, False)

        # Dropdown options list
        options = list(CURRENCY_MAP.values())

        # From Currency Dropdown (ttk.Combobox for easy searching/scrolling)
        tk.Label(self.root, text="From:").pack(pady=(10, 0))
        self.from_var = tk.StringVar(self.root)
        self.from_combo = ttk.Combobox(self.root, textvariable=self.from_var, values=options, state="readonly", width=35)
        self.from_combo.set(CURRENCY_MAP["USD"])
        self.from_combo.pack(pady=2)

        # Swap Button
        self.swap_btn = tk.Button(self.root, text="⇅ Swap", command=self.swap_currencies)
        self.swap_btn.pack(pady=2)

        # To Currency Dropdown
        tk.Label(self.root, text="To:").pack(pady=(2, 0))
        self.to_var = tk.StringVar(self.root)
        self.to_combo = ttk.Combobox(self.root, textvariable=self.to_var, values=options, state="readonly", width=35)
        self.to_combo.set(CURRENCY_MAP["AZN"])
        self.to_combo.pack(pady=2)

        # Amount Entry
        tk.Label(self.root, text='Amount:').pack(pady=(8, 0))
        self.amount_entry = tk.Entry(self.root, width=20, justify="center")
        self.amount_entry.insert(0, "1")
        self.amount_entry.pack(pady=2)

        # Convert Button
        self.convert_button = tk.Button(self.root, text='Convert', command=self.convert_currency, bg="#007acc", fg="white")
        self.convert_button.pack(pady=12)

        # Result Label
        self.result_label = tk.Label(self.root, text="", font=("Arial", 11, "bold"))
        self.result_label.pack(pady=5)

        self.root.mainloop()

    def get_rates_in_usd(self):
        """Fetches live rates from open-api relative to USD, and appends custom values."""
        try:
            response = requests.get("https://open.er-api.com/v6/latest/USD", timeout=5)
            rates = response.json().get("rates", {})

           ##Fetch live crypto rates (BTC, USDT) via CoinGecko free API
            crypto_res = requests.get(
                "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,tether,the-open-network&vs_currencies=usd",
                timeout=5
            ).json()

            btc_usd = crypto_res.get("bitcoin", {}).get("usd", 65000.0)
            usdt_usd = crypto_res.get("tether", {}).get("usd", 1.0)

            rates["BTC"] = 1 / btc_usd if btc_usd else 0.000015
            rates["USDT"] = 1 / usdt_usd if usdt_usd else 1.0

           ##Add Fixed/Custom Pegged Rates relative to 1 USD
            rates["STARS"] = 50.0   # ~50 Telegram Stars = 1 USD (adjust as needed)
            rates["GRAM"] = 1000.0  # Gram token estimation

            return rates

        except Exception as e:
            return {
                "USD": 1.0, "EUR": 0.92, "AZN": 1.70, "BAM": 1.80, "RUB": 90.0,
                "GBP": 0.78, "BTC": 0.000015, "USDT": 1.0, "STARS": 50.0, "GRAM": 1000.0
            }

    def swap_currencies(self):
        from_val = self.from_combo.get()
        to_val = self.to_combo.get()
        self.from_combo.set(to_val)
        self.to_combo.set(from_val)

    def convert_currency(self):
        try:
            from_code = DISPLAY_TO_CODE[self.from_combo.get()]
            to_code = DISPLAY_TO_CODE[self.to_combo.get()]
            amount = float(self.amount_entry.get())

            rates = self.get_rates_in_usd()

            if from_code not in rates or to_code not in rates:
                self.result_label.config(text="Rate currently unavailable.")
                return

            # Convert 'Amount' to USD first, then convert to 'Target Currency'
            amount_in_usd = amount / rates[from_code]
            converted_amount = amount_in_usd * rates[to_code]

            # Format output dynamically based on decimal precision needed
            if converted_amount < 0.01:
                self.result_label.config(text=f'{amount} {from_code} = {converted_amount:.6f} {to_code}')
            else:
                self.result_label.config(text=f'{amount} {from_code} = {converted_amount:,.2f} {to_code}')

        except ValueError:
            self.result_label.config(text="Please enter a valid number.")
        except Exception as e:
            self.result_label.config(text="Conversion error occurred.")


if __name__ == "__main__":
    CurrencyConverter()
