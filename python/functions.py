'''File for functions that are used in the main file'''
import pandas as pd
from pandas.api.types import is_numeric_dtype
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def nan_replace_t(t):
    '''Replace NaN values in a pandas dataframe with the mean of the column'''
    assert isinstance(t, pd.DataFrame)
    for v in t.columns:
        if any(t[v].isna()):
            if is_numeric_dtype(t[v]):
                t[v].fillna(t[v].mean(), inplace=True)
            else:
                t[v].fillna(t[v].mode()[0], inplace=True)


#tratarea valorilor extreme
def treat_outliers(t):
    '''Treat outliers in a pandas dataframe'''
    assert isinstance(t, pd.DataFrame)
    for v in t.columns:
        if is_numeric_dtype(t[v]):
            q1 = t[v].quantile(0.25)
            q3 = t[v].quantile(0.75)
            iqr = q3 - q1
            t[v] = np.where(t[v] < q1 - 1.5 * iqr, q1, t[v])
            t[v] = np.where(t[v] > q3 + 1.5 * iqr, q3, t[v])


#functie pentru definirea listelor si dictionarelor pe setul de date
def define_lists(t):
    '''Define lists and dictionaries for the dataset'''
    if not isinstance(t, pd.DataFrame):
        print('The input should be a pandas dataframe')
    # define the lists and dictionaries
    # list of numerical columns
    num_cols = [v for v in t.columns if is_numeric_dtype(t[v])]
    # list of categorical columns
    cat_cols = [v for v in t.columns if not is_numeric_dtype(t[v])]
    # dictionary of numerical columns
    num_dict = {v: t[v].mean() for v in num_cols}
    # dictionary of categorical columns
    cat_dict = {v: t[v].mode()[0] for v in cat_cols}
    return num_cols, cat_cols, num_dict, cat_dict


# metode specifice listelor si dictionarelor de ex: add(), discard(),
# union(), intersection(), etc.
def list_methods(t):
    '''Specific methods for lists and dictionaries'''
    # call to define lists
    num_cols, cat_cols, num_dict, cat_dict = define_lists(t)
    print("Trying to add, discard, union and intersect elements in the "
          "lists and dictionaries.\n")
    # add a new element to the list of numerical columns
    num_cols.append('new_col')
    print(f"Added new_col to the list of numerical columns")
    for num_col in num_cols:
        print(f"{num_col}")
    # add a new element to the dictionary of numerical columns
    num_dict['new_col'] = 0
    print(f"\nAdded new_col to the dictionary of numerical columns")
    for k, v in num_dict.items():
        print(f"{k}: {v}")
    # discard an element from the list of categorical columns
    try:
        cat_cols.remove('new_col')
        print(f"Discarded new_col from the list of categorical columns")
        for cat_col in cat_cols:
            print(f"{cat_col}")
    except ValueError:
        pass
    # discard an element from the dictionary of categorical columns
    cat_dict.pop('new_col', None)
    print(f"Discarded new_col from the dictionary of categorical columns")
    for k, v in cat_dict.items():
        print(f"{k}: {v}")
    # union of the two lists
    num_cat_cols = num_cols + cat_cols
    print(f"Union of the two lists")
    for num_cat_col in num_cat_cols:
        print(f"{num_cat_col}")
    # intersection of the two dictionaries
    num_cat_dict = {k: num_dict[k] for k in num_dict if k in cat_dict}
    print(f"Intersection of the two dictionaries")
    for k, v in num_cat_dict.items():
        print(f"{k}: {v}")
    return num_cols, cat_cols, num_dict, cat_dict, num_cat_cols, num_cat_dict


#creare, manipulare, comparare a seturilor si tuplurilor
def set_tuple(t):
    '''Create, manipulate, compare sets and tuples'''
    # call to define lists
    num_cols, cat_cols, num_dict, cat_dict = define_lists(t)
    # create a set from the list of numerical columns
    num_set = set(num_cols)
    # create a set from the list of categorical columns
    cat_set = set(cat_cols)
    # create a tuple from the dictionary of numerical columns
    num_tuple = tuple(num_dict.items())
    # create a tuple from the dictionary of categorical columns
    cat_tuple = tuple(cat_dict.items())
    # compare the two sets
    set_comp = num_set == cat_set
    # compare the two tuples
    tuple_comp = num_tuple == cat_tuple
    return num_set, cat_set, num_tuple, cat_tuple, set_comp, tuple_comp


# Metode specifice: add(), discard(), union(), intersection(), etc. ale
# seturilor si tuplurilor
def set_tuple_methods(tuples, t):
    '''Specific methods for sets and tuples'''
    # call to define lists
    num_cols, cat_cols, num_dict, cat_dict = define_lists(t)
    # extract the sets and tuples from the tuples argument
    num_set, cat_set, num_tuple, cat_tuple, set_comp, tuple_comp = tuples
    # add a new element to the set of numerical columns
    num_set.add('new_col')
    print(f"Added new_col to the set of numerical columns")
    for num_col in num_set:
        print(f"{num_col}")
    # add a new element to the set of categorical columns
    cat_set.add('new_col')
    print(f"\nAdded new_col to the set of categorical columns")
    for cat_col in cat_set:
        print(f"{cat_col}")
    # discard an element from the set of numerical columns
    num_set.discard('new_col')
    print(f"\nDiscarded new_col from the set of numerical columns")
    for num_col in num_set:
        print(f"{num_col}")
    # discard an element from the set of categorical columns
    cat_set.discard('new_col')
    print(f"\nDiscarded new_col from the set of categorical columns")
    for cat_col in cat_set:
        print(f"{cat_col}")
    # union of the two sets
    num_cat_set = num_set.union(cat_set)
    print(f"\nUnion of the two sets")
    for num_cat_col in num_cat_set:
        print(f"{num_cat_col}")
    # intersection of the two tuples
    num_cat_tuple = set(num_tuple).intersection(set(cat_tuple))
    print(f"\nIntersection of the two tuples")
    for num_cat_tup in num_cat_tuple:
        print(f"{num_cat_tup}")
    return num_set, cat_set, num_tuple, cat_tuple, num_cat_set, num_cat_tuple


#calcularea mediei, medianei, deviatiei standard, varianței, corelației
def calculate_stats(t):
    '''Calculate statistics for a pandas dataframe'''
    assert isinstance(t, pd.DataFrame)
    # select only the numeric columns in the dataframe
    numeric_t = t.select_dtypes(include=[np.number])
    # calculate the mean of the numeric columns in the dataframe
    mean_df = numeric_t.mean()
    print(f"\nMean of the numeric columns in the dataframe:\n{mean_df}")
    # calculate the median of the numeric columns in the dataframe
    median_df = numeric_t.median()
    print(f"\nMedian of the numeric columns in the dataframe:\n{median_df}")
    # calculate the standard deviation of the numeric columns in the dataframe
    std_df = numeric_t.std()
    print(f"\nStandard deviation of the numeric columns in the dataframe:\n{std_df}")
    # calculate the variance of the numeric columns in the dataframe
    var_df = numeric_t.var()
    print(f"\nVariance of the numeric columns in the dataframe:\n{var_df}")
    # calculate the correlation of the numeric columns in the dataframe
    corr_df = numeric_t.corr()
    print(f"\nCorrelation of the numeric columns in the dataframe:\n{corr_df}")
    return mean_df, median_df, std_df, var_df, corr_df


# generarea de grafice pentru setul de date(histograma, grafic de linie,
# grafic de bare)
def generate_plots(t):
    '''Generate plots for a pandas dataframe'''
    assert isinstance(t, pd.DataFrame)
    # select only the numeric or datetime columns in the dataframe
    numeric_t = t.select_dtypes(include=[np.number, 'datetime'])
    # check if numeric_t is not empty
    if not numeric_t.empty:
        # generate a histogram for the numeric or datetime columns in the dataframe
        numeric_t.hist()
        plt.savefig('../python/diagrams_plots/histogram.png')
        plt.close()
    # select only the numeric columns in the dataframe for line plot
    numeric_t = t.select_dtypes(include=[np.number])
    # check if numeric_t is not empty
    if not numeric_t.empty:
        # generate a line plot for the numeric columns in the dataframe
        numeric_t.plot()
        plt.savefig('../python/diagrams_plots/line_plot.png')
        plt.close()
    # select only the numeric columns in the dataframe for bar plot
    numeric_t = t.select_dtypes(include=[np.number])
    # check if numeric_t is not empty
    if not numeric_t.empty:
        # generate a bar plot for the numeric columns in the dataframe
        numeric_t.plot(kind='bar')
        plt.savefig('../python/diagrams_plots/bar_plot.png')
        plt.close()
    return None

# Utilizarea pachetului scikit-learn pentru analiză și predicții: Aplicarea
# algoritmilor de clusterizare și regresie logistică pe datele existente.
def apply_ml(t):
    '''Apply machine learning algorithms on a pandas dataframe'''
    assert isinstance(t, pd.DataFrame)
    # select only the numeric columns in the dataframe
    numeric_t = t.select_dtypes(include=[np.number])
    # check if numeric_t is not empty
    if not numeric_t.empty:
        # apply the KMeans clustering algorithm on the dataframe
        kmeans = KMeans(n_clusters=2)
        kmeans.fit(numeric_t)
        t['cluster'] = kmeans.labels_
        # apply the Logistic Regression algorithm on the dataframe
        X = t.drop('cluster', axis=1)
        y = t['cluster']
        print(f"\nApplied machine learning algorithms on the dataframe:\n{t}")
        return X, y
    else:
        print("The dataframe does not contain any numeric columns to apply machine learning algorithms.")
        return None, None

