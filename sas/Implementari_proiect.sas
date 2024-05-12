/* Definirea fisierului CSV si importarea datelor */
FILENAME netflix "/home/u63853491/netflix.csv" TERMSTR=CRLF;

/* Definirea variabilelor din dataset */
DATA netflix_data;
   INFILE netflix DLM=',' FIRSTOBS=2; /* Specificați delimiterul ca fiind virgulă și ignorăm prima linie care conține doar numele coloanelor */
   INPUT Date :DDMMYY10. Global_Revenue UCAN_Streaming_Revenue EMEA_Streaming_Revenue LATM_Streaming_Revenue APAC_Streaming_Revenue UCAN_Members EMEA_Members LATM_Members APAC_Members Netflix_Streaming_Memberships;
   FORMAT Date DDMMYY10.; /* Specificați formatul pentru variabila de tip dată */
RUN;

/* Verificarea importului datelor */
PROC PRINT DATA=netflix_data;
RUN;

/* Calcularea sumelor și mediilor pentru veniturile globale și veniturile din diferite regiuni */
/* Util în identificarea performanței financiare și a distribuției geografice a veniturilor */
PROC MEANS DATA=netflix_data SUM MEAN;
   VAR Global_Revenue UCAN_Streaming_Revenue EMEA_Streaming_Revenue LATM_Streaming_Revenue APAC_Streaming_Revenue;
RUN;

/* Analiza evoluției numărului de membri din diferite regiuni */
/* Util pentru a identifica tendințele în adopția serviciului în diferite piețe geografice */
PROC SGSCATTER DATA=netflix_data;
   PLOT UCAN_Members*Date EMEA_Members*Date LATM_Members*Date APAC_Members*Date;
RUN;

/* Analiza trendurilor în ceea ce privește numărul total de abonamente la serviciul de streaming Netflix */
/* Util în evaluarea creșterii sau scăderii abonamentelor și identificarea factorilor care contribuie la acestea */
PROC SGPLOT DATA=netflix_data;
   SERIES x=Date y=Netflix_Streaming_Memberships / MARKERS;
   XAXIS LABEL="Date";
   YAXIS LABEL="Netflix Streaming Memberships";
RUN;

/* Analiza distribuțiilor */
/* Util în înțelegerea distribuției variabilelor cheie și a posibilelor discrepanțe între regiuni */
PROC UNIVARIATE DATA=netflix_data;
   VAR Global_Revenue UCAN_Streaming_Revenue EMEA_Streaming_Revenue LATM_Streaming_Revenue APAC_Streaming_Revenue UCAN_Members EMEA_Members LATM_Members APAC_Members Netflix_Streaming_Memberships;
RUN;

/* Calcularea matricei de corelații */
/* Util în identificarea relațiilor între diferite variabile și în dezvoltarea strategiilor de extindere */
PROC CORR DATA=netflix_data;
   VAR Global_Revenue UCAN_Streaming_Revenue EMEA_Streaming_Revenue LATM_Streaming_Revenue APAC_Streaming_Revenue UCAN_Members EMEA_Members LATM_Members APAC_Members Netflix_Streaming_Memberships;
RUN;
