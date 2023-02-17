# Anime-Recommender
Aplikacja rekomendująca Anime na podstawie wybranego tytułu przez użytkownika. 
Wykorzystuje algorytmy TfidfVectorizer i cosine_similarity do obliczenia podobieństwa między anime. 
Użytkownik może wybrać tytuł z listy i zobaczyć listę pięciu rekomendowanych anime oraz ich plakaty. 

Zbiór danych: https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2019/2019-04-23/tidy_anime.csv

Aby uruchomić program, należy najpierw zainstalować wymagane biblioteki z pliku requirements.txt. 
Należy to zrobić za pomocą polecenia <code>pip install -r requirements.txt</code> w terminalu. 
Następnie, w terminalu należy wywołać komendę <code>streamlit run app.py</code>, aby uruchomić aplikację.
