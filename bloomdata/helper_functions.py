import pandas as pd
import numpy as np
import random

adjectives = ['blue', 'large', 'grainy',
              'substantial', 'potent', 'thermonuclear']
nouns = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']


def random_phrase(list1, list2):
    item1 = random.choice(list1)
    item2 = random.choice(list2)
    return str(item1) + ' ' + str(item2)


def random_float(min_val, max_val):
    flt = random.uniform(min_val, max_val)
    flt = f'{flt:.1f}'
    return flt


def random_bowling_score():
    return random.randint(0, 300)


def silly_tuple():
    my_tuple = (random_phrase(), random_float(1, 5), random_bowling_score())
    return my_tuple


def silly_tuple_list(num_tuples):
    mylist = []
    for _ in range(num_tuples):
        mylist.append(silly_tuple())
    return mylist


test_df = pd.DataFrame({'column_1': [1, 2, np.nan],
                        'column_2': [4, 5, 6],
                        'column_3': [7, np.nan, 9]})


def null_count(df):
    num_null = df.isnull().sum().sum()
    return num_null

# print(null_count(test_df))


def train_test_split(df, frac):
    rows = df.shape[0]
    mask = int(rows*frac)
    df_tuple = (df[:mask], df[mask:])
    return df_tuple


def randomize(df, seed):
    data_array = df.values
    np.random.seed(seed)
    np.random.shuffle(data_array)
    shuffled_df = pd.DataFrame(data_array, columns=df.columns)
    return shuffled_df


def addy_split(addy_series):
    df = pd.DataFrame({'address': addy_series.address})
    str_address = df['address'].str.extract(r'[0-9]+\s[a-zA-z]+\ \
                                            s[a-zA-z]+\n([a-zA-Z]+\ \
                                            s?[a-zA-Z]*),\s([a-zA-Z]+) \
                                            \s([0-9]+)')
    str_address.columns = ('city', 'state', 'zip')
    return str_address


def abbr_2_st(state_series, abbr_2_st=True):
    new_list = []

    if abbr_2_st:
        for i in range(len(state_series[0])):
            if state_series[0][i] == 'AL':
                new_list.append('Alabama')
            elif state_series[0][i] == 'AZ':
                new_list.append('Arizona')
            elif state_series[0][i] == 'CA':
                new_list.append('California')
            elif state_series[0][i] == 'DE':
                new_list.append('Delaware')
            elif state_series[0][i] == 'OH':
                new_list.append('Ohio')
            new_title = 'states'
    else:
        for i in range(len(state_series[0])):
            if state_series[0][i] == 'Alabama':
                new_list.append('AL')
            elif state_series[0][i] == 'Arizona':
                new_list.append('AZ')
            elif state_series[0][i] == 'California':
                new_list.append('CA')
            elif state_series[0][i] == 'Delaware':
                new_list.append('DE')
            elif state_series[0][i] == 'Ohio':
                new_list.append('OH')
            new_title = 'st_2_abbr'
    new_list = pd.Series({new_title: new_list})
    return new_list


def list_2_series(list_2_series, df):
    lst = pd.Series(list_2_series)
    df['list'] = lst
    return df


if __name__ == '__main__':
    print(random_phrase(adjectives, nouns))
