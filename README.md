# WaitExchange
This is project of mine, where you can see real-time (live) converter where you can switch this currencies: USD, BAM, EUR, RUB, AED, USDT, GRAM , STARS, JPY, GPB, CAD, AUD, CNY, INR, KZTM SGD, BRL, NOK , SEK, PLN, MXN, SAR, KZT, TRY, AZN and others will be soon (:

## ✨ FeaturesLive Exchange Rates:


Automatically fetches up-to-date fiat exchange rates via public APIs (open.er-api.com).Cryptocurrency Support: 

Integrates live pricing for popular assets like Bitcoin (BTC) and Tether (USDT) using the CoinGecko API.Custom Pegged Assets: Includes support for custom digital assets or tokens (e.g., Telegram Stars, Gram Token).

## 🚀 UsageRun the script from your terminal:python currency_converter.py

(Note: Replace currency_converter.py with whatever filename you saved the script under.)

How to use the App:From: Select your base currency from the first dropdown list.To: 

Select your target currency from the second dropdown list.
Amount: Enter the numerical amount you wish to convert.Swap (⇅): 
Click the swap button to quickly reverse the "From" and "To" selections.

Convert: Click the Convert button to view the real-time calculated result.

## 🧩 Adding Custom CurrenciesTo add new currencies or tokens, modify the CURRENCY_MAP dictionary and the fallback/fetching logic inside get_rates_in_usd():Add your currency code and description to CURRENCY_MAP:CURRENCY_MAP = {
    ...
    "YOUR_CODE": "YOUR_CODE - Currency Name",
}
Adjust the API calls or fallback rates in get_rates_in_usd() to handle the rate relative to USD ($1\text{ USD} = \text{rate}$).📄 LicenseThis project is open-source and available for personal or educational use.


# But how to do it?

It is easy python program where you can type

python main.py 

Guide to install python: https://www.python.org/downloads/
