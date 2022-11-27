"""
1.  Gerade und Ungerade

Schreiben Sie ein Programm, das eine ganze Zahl vom Benutzer liest. Dann sollte Ihr Programm eine Meldung anzeigen, die angibt, ob die ganze Zahl gerade oder ungerade ist.
"""


def check_even_odd():
    try:
        number = int(input("> Please enter a number\n"))
        output = f"Number {number} is even" if number % 2 == 0 else f"Number {number} is odd"
        print(output)
    except:
        print(f"Try entering a text you swine!")


# check_even_odd()


"""
2. Hundejahre

Es wird allgemein gesagt, dass ein Menschenjahr 7 Hundejahren entspricht. Diese einfache Umwandlung übersieht jedoch, dass Hunde in etwa zwei Jahren das Erwachsenenalter erreichen. Infolgedessen glauben einige Leute, dass es besser ist, jedes der ersten beiden Menschenjahre als 10,5 Hundejahre zu zählen und dann jedes weitere Menschenjahr als 4 Hundejahre.

Schreiben Sie ein Programm, das die im vorherigen Abschnitt beschriebene Umstellung von Menschenjahren auf Hundejahre implementiert. Stellen Sie sicher, dass Ihr Programm bei Konvertierungen von weniger als zwei Menschenjahren und bei Konvertierungen von zwei oder mehr Menschenjahren korrekt funktioniert. Ihr Programm sollte eine entsprechende Fehlermeldung anzeigen, wenn der Benutzer eine negative Zahl eingibt.
"""


def mensch_in_hunde_jahren(menschen_jahre):
    if menschen_jahre < 0:
        raise Exception(f"Zahl '{menschen_jahre}' kann nicht negativ sein!")
    hunde_jahre = 0
    for jahr in range(menschen_jahre):
        if jahr <= 1:
            hunde_jahre += 10.5
        else:
            hunde_jahre += 7.0
    return hunde_jahre


# try:
#     menschen_jahre = 7
#     hunde_jahre = mensch_in_hunde_jahren(menschen_jahre)
#     print(
#         f"Mensch mit Alter '{menschen_jahre}' ist '{hunde_jahre}' Hunde Jahre alt.")
# except Exception as error:
#     print(f"Fehler: {error}")

"""
3. Vokale

In dieser Übung erstellen Sie ein Programm, das einen Buchstaben des Alphabets vom Benutzer einliest. Wenn der Benutzer ein, e, i, o oder u eingibt, sollte Ihr Programm eine Meldung anzeigen die darauf hindeutet, dass der eingegebene Buchstabe ein Vokal ist. 

Wenn der Benutzer y eingibt, dann sollte Ihr Programm eine Meldung anzeigen, dass  y manchmal ein Vokal ist und manchmal y ein Konsonant ist.
"""


def print_maybe_vocal():
    vocals = list("aeiou")
    character = input("> Bitte gib einen Buchstaben ein\n").lower()

    if character in vocals:
        print(f"Buchstabe '{character}' ist ein Vokal")
    elif character == 'y':
        print("Buchstabe 'y' ist manchmal ein Vokal...")
    else:
        print(f"Buchstabe '{character}' ist kein Vokal")


# print_maybe_vocal()
