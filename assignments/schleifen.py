"""
Schreiben Sie ein Programm, bei dem Städte und deren
Einwohnerzahlen eingegeben werden können. Wenn der Benutzer bei einer Stadt
ein „x“ eingibt, wird die Eingabe gestoppt.
Bsp.:
Geben Sie die Stadt ein: Zürich
Geben Sie die zugehörige Einwohnerzahl ein: 370000
Geben Sie die Stadt ein: Bern
Geben Sie die zugehörige Einwohnerzahl ein: 130000
Geben Sie die Stadt ein: x
Während der Eingabe soll im Programm eine Liste (list) erzeugt werden, wie die in
der ad hoc Übung 3.2 b). Bsp.: [["Zürich", 370000], ["Bern", 130000]]
Geben Sie die Liste am Ende des Programmes alphabetisch sortiert aus, d.h.
einfache Ausgabe mit print(liste). Bsp.: [["Bern", 130000], ["Zürich", 370000] ]
"""


def staedte_einwohner():
    mapping = []
    while True:
        stadt = input("Geben Sie die Stadt ein: ")
        if stadt.lower() == 'x':
            break
        einwohner = int(input("Geben Sie die zugehörige Einwohnerzahl ein: "))
        mapping.append([stadt, einwohner])
    print(mapping)


# staedte_einwohner()


"""
Erstellen Sie mittels einem Dictionary (dict) ein Mini-Deutsch-Englisch
Wörterbuch (10 Vokabeln). Ein zugehörige Vokabeltrainer soll alle
Vokabeln nach folgendem Muster abfragen:
Was heisst Haus: house
RICHTIG!
Was heisst Zahnarzt: dentist
RICHTIG!
Was heisst Zahn: dent
FALSCH!
… Nach Abfrage aller Vokabeln wird noch die Abfragestatistik ausgegeben:
Sie haben 7 von 10 Vokabeln richtig beantwortet!
"""


def vokabel_trainer():
    woerterbuch = {
        "haus": "house",
        "tier": "pet",
        "hund": "dog",
        "katze": "cat",
        "schlange": "snake",
        "apfel": "apple",
        "süssigkeiten": "sweets",
        "milch": "milk",
        "mutter": "mother",
        "vater": "father"
    }

    anzahl_richtige_worte = 0
    for deutsch, englisch in woerterbuch.items():
        wort = input(f"Was heisst {deutsch}: ")
        wort = wort.strip().lower()
        if wort == englisch:
            anzahl_richtige_worte += 1
            print("RICHTIG!")
        else:
            print(
                f"FALSCH!, die richtige Antwort ist: '{englisch}'")

    print(
        f"Sie haben {anzahl_richtige_worte} von {len(woerterbuch.keys())} Vokabeln richtig beantwortet!")


# vokabel_trainer()
