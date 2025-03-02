import pandas as pd

big_mac_file = './big-mac-full-index.csv'

# Load the CSV file into a DataFrame
df = pd.read_csv(big_mac_file)

# Function to get the mean Big Mac price by year and country code
def get_big_mac_price_by_year(year, country_code):
    total_price = 0
    count = 0
    for _, row in df.iterrows():
        if row['date'].startswith(str(year)) and row['iso_a3'].lower() == country_code.lower():
            total_price += row['dollar_price']
            count += 1
    if count > 0:
        return round(total_price / count, 2)
    else:
        return None

# Function to get the mean Big Mac price by country code
def get_big_mac_price_by_country(country_code):
    total_price = 0
    count = 0
    for _, row in df.iterrows():
        if row['iso_a3'].lower() == country_code.lower():
            total_price += row['dollar_price']
            count += 1
    if count > 0:
        return round(total_price / count, 2)
    else:
        return None

# Function to get the cheapest Big Mac price by year
def get_the_cheapest_big_mac_price_by_year(year):
    min_price = float('inf')
    min_country = None
    for _, row in df.iterrows():
        if row['date'].startswith(str(year)) and row['dollar_price'] < min_price:
            min_price = row['dollar_price']
            min_country = row
    if min_country is not None:
        return f"{min_country['name']}({min_country['iso_a3']}): ${round(min_price, 2)}"
    else:
        return None

# Function to get the most expensive Big Mac price by year
def get_the_most_expensive_big_mac_price_by_year(year):
    max_price = float('-inf')
    max_country = None
    for _, row in df.iterrows():
        if row['date'].startswith(str(year)) and row['dollar_price'] > max_price:
            max_price = row['dollar_price']
            max_country = row
    if max_country is not None:
        return f"{max_country['name']}({max_country['iso_a3']}): ${round(max_price, 2)}"
    else:
        return None

# Basic interface as per assignment instructions
if __name__ == "__main__":
    # Example calls for testing with different countries and years
    print(get_big_mac_price_by_year(2008, 'usa'))          # Should work for any valid year and country
    print(get_big_mac_price_by_country('chn'))              # Should work for any valid country code
    print(get_the_cheapest_big_mac_price_by_year(2008))     # Should find the cheapest for any year
    print(get_the_most_expensive_big_mac_price_by_year(2003)) # Should find the most expensive for any year
