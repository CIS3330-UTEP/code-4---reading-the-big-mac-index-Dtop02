import pandas as pd

def get_big_mac_price_by_year(year, country_code):
    df = pd.read_csv('big-mac-full-index.csv')
    fil_d = df[(df['iso_a3'].str.lower() == country_code.lower()) & (df['date'].str.startswith(str(year)))]
    rounded_price = round(fil_d['dollar_price'].mean(), 2)
    return rounded_price


def get_big_mac_price_by_country(country_code):
    df = pd.read_csv('big-mac-full-index.csv')
    fil_d = df[df['iso_a3'].str.lower() == country_code.lower()]
    mp = fil_d['dollar_price'].mean()
    rounded_price = round(mp, 2)
    return rounded_price


def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv('big-mac-full-index.csv')
    fil_d = df[df['date'].str.startswith(str(year))]
    chep_row = fil_d.loc[fil_d['dollar_price'].idxmin()]
    country_name = chep_row['name']
    country_code = chep_row['iso_a3']
    dol_pr = chep_row['dollar_price']
    return f"{country_name}({country_code}): ${dol_pr:.1f}"


def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv('big-mac-full-index.csv')
    fil_d = df[df['date'].str.startswith(str(year))]
    expen_row = fil_d.loc[fil_d['dollar_price'].idxmax()]
    country_name = expen_row['name']
    country_code = expen_row['iso_a3']
    dol_pr = expen_row['dollar_price']
    return f"{country_name}({country_code}): ${dol_pr:.1f}"



if __name__ == "__main__":
    result_a = get_big_mac_price_by_year(2009,"mex")
    print(result_a)
    result_b = get_big_mac_price_by_country ("mex")
    print(result_b)
    result_c = get_the_cheapest_big_mac_price_by_year (2008)
    print (result_c)
    result_d = get_the_most_expensive_big_mac_price_by_year (2014)
    print (result_d)