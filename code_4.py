import pandas as pd

df = pd.read_csv('./big-mac-full-index.csv')


def get_big_mac_price_by_year(year, country_code):
    total_price = 0
    count = 0
    for _, row in df.iterrows():
        if row['date'].startswith(str(year)) and row['iso_a3'].lower() == country_code.lower():
            total_price += row['dollar_price']
            count += 1
    if count > 0:
        return f"${round(total_price / count, 2)}"
    else:
        return None


def get_big_mac_price_by_country(country_code):
    total_price = int()
    count = int()
    for _, row in df.iterrows():
        if row['iso_a3'].lower() == country_code.lower():
            total_price += row['dollar_price']
            count += 1
    if count > 0:
        return f"${round(total_price / count, 2)}"
    else:
        return None


def get_the_cheapest_big_mac_price_by_year(year):
    minimum_price = float('inf')
    minimum_country = None
    for _, row in df.iterrows():
        if row['date'].startswith(str(year)) and row['dollar_price'] < minimum_price:
            minimum_price = row['dollar_price']
            minimum_country = row
    if minimum_country is not None:
        return f"{minimum_country['name']}({minimum_country['iso_a3']}): ${round(minimum_price, 2)}"
    else:
        return None


def get_the_most_expensive_big_mac_price_by_year(year):
    maximum_price = float('-inf')
    maximum_country = None
    for _, row in df.iterrows():
        if row['date'].startswith(str(year)) and row['dollar_price'] > maximum_price:
            maximum_price = row['dollar_price']
            maximum_country = row
    if maximum_country is not None:
        return f"{maximum_country['name']}({maximum_country['iso_a3']}): ${round(maximum_price, 2)}"
    else:
        return None


if __name__ == "__main__":
    print(get_big_mac_price_by_year(2005, 'Usa'))  
    print(get_big_mac_price_by_country('usa'))   
    print(get_the_cheapest_big_mac_price_by_year(2005)) 
    print(get_the_most_expensive_big_mac_price_by_year(2005)) 
    #Is GitHub working?
