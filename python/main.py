'''
Main python file for the project
'''
# Importați funcțiile din fișierul functions
from functions import *
import pandas as pd
import numpy as np

if __name__ == "__main__":
    # Citirea setului de date din folderul resurse
    t = pd.read_csv('../resurse/netflix.csv', sep=',', header=0)

    # Înlocuirea valorilor NaN în setul de date cu medii pentru a menține
    # integritatea datelor și pentru a facilita analiza ulterioară
    nan_replace_t(t)

    # Tratarea valorilor extreme în setul de date pentru a elimina potențialele
    # distorsiuni și pentru a obține rezultate mai precise în analiză
    treat_outliers(t)

    # Definirea listelor și dicționarelor pentru setul de date, care
    # furnizează o structură clară și ușor de gestionat a datelor
    # pentru analiză
    num_cols, cat_cols, num_dict, cat_dict = define_lists(t)

    # Aplicarea unor metode specifice pentru liste și dicționare pentru a
    # obține informații utile despre structura și conținutul setului de date
    list_methods(t)

    # Definirea unui set de tupluri pentru a reprezenta și analiza relații
    # între perechi de date
    tuples = set_tuple(t)

    # Aplicarea metodelor specifice pentru seturi de tupluri pentru a
    # identifica corelații și tendințe relevante în datele furnizate
    set_tuple_methods(tuples, t)

    # Calcularea statisticilor pentru setul de date, inclusiv medii, mediane
    # și corelații, pentru a oferi o înțelegere mai profundă a distribuției
    # și relațiilor din setul de date
    calculate_stats(t)

    # Generarea graficelor pentru setul de date pentru a vizualiza și
    # interpreta mai ușor datele, evidențiind modele și tendințe
    generate_plots(t)

    # Aplicarea algoritmilor de învățare automată pentru a identifica posibile
    # modele sau tendințe care să sugereze oportunități de extindere sau
    # îmbunătățire a serviciilor Netflix
    apply_ml(t)

    # Afișarea primelor 5 rânduri ale setului de date pentru a oferi o privire
    # de ansamblu asupra datelor analizate
    print("\nPrimele 5 rânduri ale setului de date:")
    print(t.head())
