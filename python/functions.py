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


# tratarea valorilor extreme
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


# functie pentru definirea listelor si dictionarelor pe setul de date
def define_lists(t):
    '''Define lists and dictionaries for the dataset'''
    if not isinstance(t, pd.DataFrame):
        print('The input should be a pandas dataframe')
    num_cols = [v for v in t.columns if is_numeric_dtype(t[v])]
    cat_cols = [v for v in t.columns if not is_numeric_dtype(t[v])]
    num_dict = {v: t[v].mean() for v in num_cols}
    cat_dict = {v: t[v].mode()[0] for v in cat_cols}
    return num_cols, cat_cols, num_dict, cat_dict


# metode specifice listelor si dictionarelor de ex: add(), discard(),
# union(), intersection(), etc.
def list_methods(t):
    '''Specific methods for lists and dictionaries'''
    num_cols, cat_cols, num_dict, cat_dict = define_lists(t)
    print("Trying to add, discard, union and intersect elements in the "
          "lists and dictionaries.\n")
    num_cols.append('new_col')
    print(f"Added new_col to the list of numerical columns")
    for num_col in num_cols:
        print(f"{num_col}")
    num_dict['new_col'] = 0
    print(f"\nAdded new_col to the dictionary of numerical columns")
    for k, v in num_dict.items():
        print(f"{k}: {v}")
    try:
        cat_cols.remove('new_col')
        print(f"Discarded new_col from the list of categorical columns")
        for cat_col in cat_cols:
            print(f"{cat_col}")
    except ValueError:
        pass
    cat_dict.pop('new_col', None)
    print(f"Discarded new_col from the dictionary of categorical columns")
    for k, v in cat_dict.items():
        print(f"{k}: {v}")
    num_cat_cols = num_cols + cat_cols
    print(f"Union of the two lists")
    for num_cat_col in num_cat_cols:
        print(f"{num_cat_col}")
    num_cat_dict = {k: num_dict[k] for k in num_dict if k in cat_dict}
    print(f"Intersection of the two dictionaries")
    for k, v in num_cat_dict.items():
        print(f"{k}: {v}")
    return num_cols, cat_cols, num_dict, cat_dict, num_cat_cols, num_cat_dict


# creare, manipulare, comparare a seturilor si tuplurilor
def set_tuple(t):
    '''Create, manipulate, compare sets and tuples'''
    num_cols, cat_cols, num_dict, cat_dict = define_lists(t)
    num_set = set(num_cols)
    cat_set = set(cat_cols)
    num_tuple = tuple(num_dict.items())
    cat_tuple = tuple(cat_dict.items())
    set_comp = num_set == cat_set
    tuple_comp = num_tuple == cat_tuple
    return num_set, cat_set, num_tuple, cat_tuple, set_comp, tuple_comp


# Metode specifice: add(), discard(), union(), intersection(), etc. ale
# seturilor si tuplurilor
def set_tuple_methods(tuples, t):
    '''Specific methods for sets and tuples'''
    num_set, cat_set, num_tuple, cat_tuple, set_comp, tuple_comp = tuples
    num_set.add('new_col')
    print(f"Added new_col to the set of numerical columns")
    for num_col in num_set:
        print(f"{num_col}")
    cat_set.add('new_col')
    print(f"\nAdded new_col to the set of categorical columns")
    for cat_col in cat_set:
        print(f"{cat_col}")
    num_set.discard('new_col')
    print(f"\nDiscarded new_col from the set of numerical columns")
    for num_col in num_set:
        print(f"{num_col}")
    cat_set.discard('new_col')
    print(f"\nDiscarded new_col from the set of categorical columns")
    for cat_col in cat_set:
        print(f"{cat_col}")
    num_cat_set = num_set.union(cat_set)
    print(f"\nUnion of the two sets")
    for num_cat_col in num_cat_set:
        print(f"{num_cat_col}")
    num_cat_tuple = set(num_tuple).intersection(set(cat_tuple))
    print(f"\nIntersection of the two tuples")
    for num_cat_tup in num_cat_tuple:
        print(f"{num_cat_tup}")
    return num_set, cat_set, num_tuple, cat_tuple, num_cat_set, num_cat_tuple


# calcularea mediei, medianei, deviatiei standard, varianței, corelației
def calculate_stats(t):
    '''Calculate statistics for a pandas dataframe'''
    assert isinstance(t, pd.DataFrame)
    numeric_t = t.select_dtypes(include=[np.number])
    mean_df = numeric_t.mean()
    print(f"\nMean of the numeric columns in the dataframe:\n{mean_df}")
    median_df = numeric_t.median()
    print(f"\nMedian of the numeric columns in the dataframe:\n{median_df}")
    std_df = numeric_t.std()
    print(f"\nStandard deviation of the numeric"
          f" columns in the dataframe:\n{std_df}")
    var_df = numeric_t.var()
    print(f"\nVariance of the numeric columns in the dataframe:\n{var_df}")
    corr_df = numeric_t.corr()
    print(f"\nCorrelation of the numeric columns in the dataframe:\n{corr_df}")
    return mean_df, median_df, std_df, var_df, corr_df


# generarea de grafice pentru setul de date(histograma, grafic de linie,
# grafic de bare)
def generate_plots(t):
    '''Generate plots for a pandas dataframe'''
    assert isinstance(t, pd.DataFrame)
    numeric_t = t.select_dtypes(include=[np.number, 'datetime'])
    if not numeric_t.empty:
        numeric_t.hist()
        plt.savefig('../python/diagrams_plots/histogram.png')
        plt.close()
    numeric_t = t.select_dtypes(include=[np.number])
    if not numeric_t.empty:
        numeric_t.plot()
        plt.savefig('../python/diagrams_plots/line_plot.png')
        plt.close()
    numeric_t = t.select_dtypes(include=[np.number])
    if not numeric_t.empty:
        numeric_t.plot(kind='bar')
        plt.savefig('../python/diagrams_plots/bar_plot.png')
        plt.close()
    return None

# Utilizarea pachetului scikit-learn pentru analiză și predicții: Aplicarea
# algoritmilor de clusterizare și regresie logistică pe datele existente.
def apply_ml(t):
    '''Apply machine learning algorithms on a pandas dataframe'''
    assert isinstance(t, pd.DataFrame)
    numeric_t = t.select_dtypes(include=[np.number])
    if not numeric_t.empty:
        kmeans = KMeans(n_clusters=2)
        kmeans.fit(numeric_t)
        t['cluster'] = kmeans.labels_
        X = t.drop('cluster', axis=1)
        y = t['cluster']
        print(f"\nApplied machine learning algorithms on the dataframe:\n{t}")
        return X, y
    else:
        print("The dataframe does not contain any numeric columns to apply "
              "machine learning algorithms.")
        return None, None

