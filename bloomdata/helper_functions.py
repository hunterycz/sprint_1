'''
This provides functions to speed up basic math problems
'''

# import needed for the following
import pandas as pd
import numpy as np
import random

adjectives = ['blue', 'large', 'grainy',
              'substantial', 'potent', 'thermonuclear']
nouns = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']


def random_phrase(list1, list2):
    '''
    Returns a concatenated string of 2 variables
    randomly selected from inputed lists

    Args:
        arg1 (int/string/float): The first item
        arg2 (int/string/float): The second item

    Returns:
        string: "arg1 + space + arg2"
    '''
    item1 = random.choice(list1)
    item2 = random.choice(list2)
    return str(item1) + ' ' + str(item2)


def random_float(min_val, max_val):
    '''
    Return a random float data type from a
    minimum value and maximun value set by user

    Parameter
    ---------
    min_val: int/float
    max_val: int/float

    Returns
    -------
    float (between the min_val and max_val)
    '''
    flt = random.uniform(min_val, max_val)
    flt = f'{flt:.1f}'
    return float(flt)


def random_bowling_score():
    '''
    Returns a random bowling score from 0 to 300
    '''
    return random.randint(0, 300)


def silly_tuple():
    '''
    Returns a tuple in the following order:
    ("random phrase", random float(between 1 and 5), random bowling score)

    Examples:
        >>> silly_tuple()
        ("blue food", 1.3, 275)

        >>> silly_tuple()
        ("large bicycle", 2.7, 125)
    '''
    my_tuple = (random_phrase(adjectives, nouns),
                random_float(1, 5), random_bowling_score())
    return my_tuple


def silly_tuple_list(num_tuples):
    '''
    Returns a tuple with a specified
    number of tuples within itself

    Args:
        arg1: int

    Returns:
        tuple: (tuple, tuple, tuple)

    Examples:
        >>> silly_tuple_list(2)
        (["blue food", 1.3, 275], ["large bicycle", 2.7, 125])

        >>> silly_tuple_list(1)
        ("grainy phone", 4.2, 300)
    '''
    mylist = []
    for _ in range(num_tuples):
        mylist.append(silly_tuple())
    return mylist


test_df = pd.DataFrame({'column_1': [1, 2, np.nan],
                        'column_2': [4, 5, 6],
                        'column_3': [7, np.nan, 9]})


def null_count(df):
    '''
    Returns the total amount of null values in a pandas dataframe

    Args:
        arg1: pandas dataframe

    Returns:
        int: number of null values

    Example:
        df = pd.DataFrame({'column_1': [1, 2, np.nan],
                           'column_2': [4, 5, 6],
                           'column_3': [7, np.nan, 9]})
        >>> null_count(df)
        2

        df = pd.DataFrame({'column_1': [1, 2, np.nan],
                           'column_2': [np.nan, np.nan, np.nan],
                           'column_3': [7, np.nan, 9]})
        >>> null_count(df)
        5
    '''
    num_null = df.isnull().sum().sum()
    return num_null


def train_test_split(df, frac):
    '''
    Returns a tuple with 2 pandas dataframes
    split based on the fraction parameter

    Args:
        arg1: pandas dataframe
        arg2: percent you would like to split
              the pandas dataframe in decimal format

    Returns:
        tuple: (dataframe1, dataframe2)

    Example:
        df = pd.DataFrame({'column_1': [1, 2, 3],
                           'column_2': [4, 5, 6],
                           'column_3': [7, 8, 9]})
        >>> train_test_split(df, 0.2)
        (df1, df2)

        df1: | column_1 | column_2 | column_3 |
             |     1    |     2    |    3     |

        df2: | column_1 | column_2 | column_3 |
             |     4    |     5    |    6     |
             |     7    |     8    |    9     |
    '''
    rows = df.shape[0]
    mask = int(rows*frac)
    df_tuple = (df[:mask], df[mask:])
    return df_tuple


def randomize(df, seed):
    '''
    Returns a pandas dataframe with all values shuffled

    Args:
        arg1: pandas dataframe
        arg2: int

    Returns:
        dataframe: shuffled values

    Example:
        df = pd.DataFrame({'column_1': [1, 2, 3],
                           'column_2': [4, 5, 6],
                           'column_3': [7, 8, 9]})
        >>> randomize(df, 30)
            | column_1 | column_2 | column_3 |
             |     4    |     2    |    7     |
             |     1    |     8    |    3     |
             |     5    |     9    |    6     |
    '''
    data_array = df.values
    np.random.seed(seed)
    np.random.shuffle(data_array)
    shuffled_df = pd.DataFrame(data_array, columns=df.columns)
    return shuffled_df


def addy_split(addy_series):
    '''
    Inputs a series with addresses organized/unorganized
    and returns a pandas dataframe with 'city', 'state',
    and 'zip' seperated

    Args:
        arg1: pandas series

    Returns:
        pandas dataframe: | city | state | zip |

    Examples:
        series = pd.series({'address': [890 Jennifer Brooks\n \
                                        North Janet, WY 24785,
                                        8394 Kim Meadow\n \
                                        Darrenville, AK 27389,
                                        379 Cain Plaza\nJosephburgh, WY 06332,
                                        5303 Tina Hill\nAudreychester, \
                                        VA 97036]})
        >>> addy_split(series)
            | city | state | zip   |
            | 890  | WY    | 24785 |
            | 8394 | AK    | 27389 |
            | 379  | WY    | 06332 |
            | 5303 | VA    | 97036 |
    '''
    df = pd.DataFrame({'address': addy_series.address})
    str_address = df['address'].str.extract(r'[0-9]+\s[a-zA-z]+\ \
                                            s[a-zA-z]+\n([a-zA-Z]+\ \
                                            s?[a-zA-Z]*),\s([a-zA-Z]+) \
                                            \s([0-9]+)')
    str_address.columns = ('city', 'state', 'zip')
    return str_address
