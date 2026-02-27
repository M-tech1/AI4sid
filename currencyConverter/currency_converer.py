# ==============================
# Currency Converter Program
# ==============================

# 1. Store exchange rates in a dictionary
exchange_rates = {
    "USD": 0.00063,   # Example rate: 1 NGN to USD
    "EUR": 0.00058,   # Example rate: 1 NGN to EUR
    "GBP": 0.00050    # Example rate: 1 NGN to GBP
}


# 2. Create reusable conversion function
def convert_currency(amount_ngn, rate):
    return amount_ngn * rate ## Convert NGN to target currency multiplying with the  exchange rate


# 3. Main program
def main():
    print("====== NGN Currency Converter ======")

    # Collect user input
    amount = float(input("Enter amount in Nigerian Naira (NGN): "))

    print("\nConverting...\n")

    # Convert to each currency
    for currency, rate in exchange_rates.items():
        converted_amount = convert_currency(amount, rate)
        print(f"{currency}: {converted_amount:.2f}")


# 4. Run the program
if __name__ == "__main__":
    main()
