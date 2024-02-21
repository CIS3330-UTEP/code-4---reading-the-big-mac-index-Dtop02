import pandas as pd

def get_big_mac_price_by_year(year, country_code):
    df = pd.read_csv('big-mac-full-index.csv')
    query_text = f"iso_a3.str.lower() == '{country_code.lower()}' and date.str.startswith('{year}')"
    count_d = df.query(query_text)
    round_p = round(count_d['dollar_price'].mean(), 2)
    return round_p

def get_big_mac_price_by_country(country_code):
    df = pd.read_csv('big-mac-full-index.csv')
    query_text = f"iso_a3.str.lower() == '{country_code.lower()}'"
    country_p = df.query(query_text)
    mp = country_p['dollar_price'].mean()
    round_p = round(mp, 2)
    return round_p


def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv('big-mac-full-index.csv')
    query_string = f"date.str.startswith('{year}')"
    bmby = df.query(query_string)
    cheapest_row = bmby.loc[bmby['dollar_price'].idxmin()]
    cntr_n = cheapest_row['name']
    cntr_c = cheapest_row['iso_a3']
    dollar_price = cheapest_row['dollar_price']
    return f"{cntr_n}({cntr_c}): ${dollar_price:.2f}"


def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv('big-mac-full-index.csv')
    query_text = f"date.str.startswith('{year}')"
    ebmpy = df.query(query_text)
    expen_r = ebmpy.loc[ebmpy['dollar_price'].idxmax()]
    cntr_n = expen_r['name']
    cntr_c = expen_r['iso_a3']
    dol_p = expen_r['dollar_price']
    return f"{cntr_n}({cntr_c}): ${dol_p:.2f}"




if __name__ == "__main__":
    result_a = get_big_mac_price_by_year(2009,"mex")
    print(result_a)
    result_b = get_big_mac_price_by_country ("mex")
    print(result_b)
    result_c = get_the_cheapest_big_mac_price_by_year (2008)
    print (result_c)
    result_d = get_the_most_expensive_big_mac_price_by_year (2014)
    print (result_d)