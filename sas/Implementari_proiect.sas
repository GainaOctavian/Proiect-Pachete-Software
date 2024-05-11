/* Definirea fisierului CSV si importarea datelor */
FILENAME CSV "/home/u63853491/unemployment.csv" TERMSTR=CRLF;

PROC IMPORT DATAFILE=CSV OUT=unemployment DBMS=CSV REPLACE;
RUN;

/* Setarea de opțiuni */
OPTIONS MPRINT MLOGIC SYMBOLGEN;

/* Afisarea primelor 5 observații din setul de date */
PROC PRINT DATA=unemployment(OBS=5);
RUN;

/* Crearea și folosirea de formate definite de utilizator pentru afișarea luni în limba română */
PROC FORMAT;
    VALUE $MonthFormat
        'January' = 'Ianuarie'
        'February' = 'Februarie'
        'March' = 'Martie'
        'April' = 'Aprilie'
        'May' = 'Mai'
        'June' = 'Iunie'
        'July' = 'Iulie'
        'August' = 'August'
        'September' = 'Septembrie'
        'October' = 'Octombrie'
        'November' = 'Noiembrie'
        'December' = 'Decembrie';
RUN;

/* Crearea unui subset de date pentru State = 'California' */
DATA unemployment_california;
    SET unemployment;
    WHERE 'Area Name'n = 'California';
RUN;

/* Afisarea primelor 5 observații din subsetul de date pentru California */
PROC PRINT DATA=unemployment_california(OBS=5);
    FORMAT Date DATE9.;
RUN;

/* Utilizarea de funcții SAS pentru calculul mediei șomajului pe grupe de vârstă */
DATA unemployment_summary;
    SET unemployment;
    Total_Unemployment_Rate = sum(of 'Age 16-19'n 'Age 20-24'n 'Age 25-34'n 'Age 35-44'n 'Age 45-54'n 'Age 55-64'n 'Age 65+'n);
    Total_Age_Groups = n(of 'Age 16-19'n 'Age 20-24'n 'Age 25-34'n 'Age 35-44'n 'Age 45-54'n 'Age 55-64'n 'Age 65+'n);
    Mean_Unemployment_Rate = Total_Unemployment_Rate / Total_Age_Groups;
RUN;

/* Afisarea primelor 5 observații din setul de date sumarizat */
PROC PRINT DATA=unemployment_summary(OBS=5);
    VAR Total_Unemployment_Rate Total_Age_Groups Mean_Unemployment_Rate;
RUN;

/* Generarea de grafice pentru rata medie a șomajului */
PROC SGSCATTER DATA=unemployment_summary;
    PLOT Mean_Unemployment_Rate*Total_Age_Groups;
RUN;

/* Crearea unui subset de date pentru luna Mai */
DATA unemployment_may;
    SET unemployment;
    WHERE Date = '01MAY2008'd;
RUN;

/* Generarea unui raport pentru statistici sumarizate pe luni */
PROC MEANS DATA=unemployment MEAN SUM;
    VAR 'Age 16-19'n 'Age 20-24'n 'Age 25-34'n 'Age 35-44'n 'Age 45-54'n 'Age 55-64'n 'Age 65+'n;
    CLASS Date;
RUN;

/* Alte operațiuni pot fi adăugate în funcție de cerințele specifice */
