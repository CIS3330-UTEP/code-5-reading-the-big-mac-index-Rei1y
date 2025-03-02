import pandas as pd

# big_mac_file = './big-mac-full-index.csv'


df = pd.read_csv('./big-mac-full-index.csv')


def get_big_mac_price_by_year(year, country_code):
    total_price = 0
    count = 0
    for _, row in df.iterrows():
        if row['date'].startswith(str(year)) and row['iso_a3'].lower() == country_code.lower():
            total_price += row['dollar_price']
            count += 1
    if count > 0:
        # return round(total_price / count, 2)
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
    # return f"${round(total_price / count, 2)}"
    else:
        return None


def get_the_cheapest_big_mac_price_by_year(year):
    minimum_price = float('inf')
    min_country = None
    for _, row in df.iterrows():
        if row['date'].startswith(str(year)) and row['dollar_price'] < minimum_price:
            minimum_price = row['dollar_price']
            min_country = row
    if min_country is not None:
        return f"{min_country['name']}({min_country['iso_a3']}): ${round(minimum_price, 2)}"
    else:
        return None


def get_the_most_expensive_big_mac_price_by_year(year):
    maximum_price = float('-inf')
    max_country = None
    for _, row in df.iterrows():
        if row['date'].startswith(str(year)) and row['dollar_price'] > maximum_price:
            maximum_price = row['dollar_price']
            max_country = row
    if max_country is not None:
        return f"{max_country['name']}({max_country['iso_a3']}): ${round(maximum_price, 2)}"
    else:
        return None


if __name__ == "__main__":
    print(get_big_mac_price_by_year(2005, 'Usa'))  
    print(get_big_mac_price_by_country('usa'))   
    print(get_the_cheapest_big_mac_price_by_year(2005)) 
    print(get_the_most_expensive_big_mac_price_by_year(2005)) 
    #Is GitHub working?
