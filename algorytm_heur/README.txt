Aplikacja została napisana w języku python i składa się z trzech plików:
- app.py (plik odpowiadający za GUI)
- entropia.py (plik zawierający algorytm)
- entropy.py (plik łączący GUI z algorytmem, czyli odpowiedzialny za uruchomienie aplikacji)

Do uruchomienia aplikacji niezbędne jest wywołanie pliku entropy.py.

#Opis GUI
- wartości X i Y - rozmiar rastra który chcemy wygenerować
- liczba klas - liczba klas z której chcemy wygenerować entropię
- Wartość entropii - entropia dla której chcemy wygenerować raster (placeholder informuje
o maksymalnej wartości entropii dla danej liczby klas)

#Opis algorytmu
Podstawową filozofią algorytmu jest wyznaczenie początkowej listy w której kategorie mają
równą liczbą wartości. Potem w każdej iteracji następuje zamiana wartości np. 2 na 1 i porównanie 
entropii z tą podaną przez użytkownika. Jeżeli entropia jest mniejsza od tej podanej przez
użytkownika następuje przerwanie algorytmu. 
Podejście takie ma jednak pewne poważne wady. Ze względu na nie algorytm został poddany pewnym 
modyfikacjom.

1. Wada (czas wykonania algorytmu)
Sprawdzanie entropii przy każdej iteracji jest bardzo czasochłonne i często nie ma sensu. Przykładowo
jeżeli entropia podana przez użytkownika to 0.1, a pierwotnie wygenerowana wynosi 1 to wymiana jednej
wartości z listy na pewno nie wystarczy do osiągnięcia odpowiedniej wartości. Z tego względu algorytm 
jest w stanie wykonać zamiany wartości dla pewnej części listy, a nie tylko jednej wartości i dopiero
potem następuje wyliczenie entropii.
Liczba elementów która ma być wymieniona jest obliczana na podstawie wzoru:
(różnica pomiędzy entropią pierwotną i zadaną) * liczba elementów w liście / wartość p

wartość p początkowo wynosi 2, ale jest zwiększana przy każdej iteracji. Ma to ograniczyć zachłanność
algorytmu.

Dzięki temu algorytm przy pierwszej iteracji jest w stanie wymienić dużą część listy, ale przy kolejnych 
coraz mniejszą. Dzięki temu jest w stanie utrzymać swoją dokładność.

2. Wada (problem z dokładnością)
Przyjmijmy że użytkownik podał wartość entropii 0.25. Algorytm w pewnej iteracji wyznaczył entropię 0.26,
a w kolejnej 0.12. 0.12 jest mniejsze niż 0.25, a 0.26 nie, więc 0.12 zostanie wyznaczone jako przybliżona 
wartość mimo że różnica pomiędzy nią a wartością daną przez użytkownika jest większa.
Problem ten został naprawiony w następujący sposób:
-stworzona została lista zapisująca po kolei wszystkie przybliżone wartości entropii wyznaczone przez
użytkownika
-stworzona zostałą druga pętla wykonująca operację odwrotną niż pierwsza.
Przykładowo jeżeli zostanie osiągnięta wartość 0.12 to druga pętla zwiększy wartość entropii do poprzedniej
(0.26) i porówna która wartość jest bliższa zadanej entropii:
-ostatnia wartość z listy entropii wyznaczonej przez pierwszą pętlę (0.12) czy wartość "testowa" entropii
wyznaczona przez drugą pętlę (0.26). W tym przypadku wartość entropii zostanie nadpisana przez wartość
"testową" i wtedy algorytm się zakończy.
