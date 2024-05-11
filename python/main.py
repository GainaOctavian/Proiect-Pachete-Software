'''
Main pyhton file for the project
'''
# import the functions from the functions file
from functions import *
import pandas as pd
import numpy as np

if __name__ == "__main__":
    # read the dataset from resurse folder
    t = pd.read_csv('../resurse/unemployment.csv',
                    sep=',', header=0)
    # replace NaN values in the dataset
    nan_replace_t(t)

    # treat outliers in the dataset
    treat_outliers(t)

    # define lists and dictionaries for the dataset
    num_cols, cat_cols, num_dict, cat_dict = define_lists(t)

    # specific methods for lists and dictionaries
    list_methods(t)

    # define a set of tuples
    tuples = set_tuple(t)

    # specific methods for sets of tuples
    set_tuple_methods(tuples, t)

    # calculate statistics for the dataset
    calculate_stats(t)

    # generate plots for the dataset
    generate_plots(t)

    # apply machine learning algorithms to the dataset
    apply_ml(t)

    # print the first 5 rows of the dataset
    print("\nFirst 5 rows of the dataset:")
    print(t.head())
