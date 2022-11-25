"""
Schreiben Sie eine Funktion, welche die Seitenlänge eines gleichseitigen Dreiecks entgegennimmt und den Umfang des Dreiecks berechnet.
"""


def umfang_dreieck(seitenlaenge):
    return seitenlaenge * 3


# print(umfang_dreieck(10))


"""
Schreiben Sie eine Funktion, welche das Alter einer Person entgegen nimmt und daraus die theoretische maximale Herzfrequenz berechnet. 

Die Formel für die Berechnung der Herzfrequenz lautet:

max Herzfrequenz = 220 − Alter in Jahren
"""


def berechne_herzfrequenz(alter):
    return 220 - alter


# print(berechne_herzfrequenz(25))

"""
Schreiben Sie eine Funktion ausgabe1000(), die 1000 mal den Satz "Heute scheint die Sonne" ausgibt!
"""


def ausgabe1000():
    return "Heute scheint die Sonne\n" * 1000


# print(ausgabe1000())


"""
a) Schreiben Sie ein Programm, dass nach dem Namen und dem Alter der Person fragt und dann in einer personalisierten Mitteilung der Person mitteilt, in welchem Jahr sie 100 Jahre alt wird.

Bsp:

> Bitte gib deinen Namen ein.

    Fabian

> Bitte gib dein Alter an.

    25

> Fabian, du wirst im Jahre 2092 100 Jahre alt sein.
"""


def hundert_jahre_alt():
    name = input("> Bitte gib deinen Namen ein.\n")
    alter = int(input("> Bitte gib dein Alter an.\n"))
    differenz = 100 - alter

    print(f"> {name}, du wirst im Jahr {2022 + differenz} 100 Jahre alt sein.")


# hundert_jahre_alt()

"""
b) Erweitern Sie das Programm in dem Sie den Benutzer um eine zusätzliche Zahl bitten die die Anzahl der Ausgaben der Nachricht definiert.

    Bsp:

    > Wie oft soll die Nachricht ausgegeben werden?

       3

    > Fabian, du wirst im Jahre 2092 100 Jahre alt sein. Fabian, du wirst im Jahre 2092 100 Jahre alt sein. Fabian, du wirst im Jahre 2092 100 Jahre alt sein.
"""


def hundert_jahre_alt():
    name = input("> Bitte gib deinen Namen ein.\n")
    alter = int(input("> Bitte gib dein Alter an.\n"))
    differenz = 100 - alter
    anzahl_ausgaben = int(
        input("> Wie oft soll die Nachricht ausgegeben werden?\n"))

    print(f"> {name}, du wirst im Jahr {2022 + differenz} 100 Jahre alt sein.\n" * anzahl_ausgaben)


# hundert_jahre_alt()

"""
Fragen Sie den Benutzer nach einer Zahl. Geben Sie dann zurück, ob diese Zahl gerade oder ungerade ist.

    Bsp:

    > Bitte Zahl eingeben:

    4

    > Die Zahl 4 ist gerade.
"""


def gerade_ungerade():
    zahl = int(input("> Bitte Zahl eingeben: \n"))
    gerade = zahl % 2 == 0
    suffix = "gerade" if gerade else "ungerade"
    print(f"> Die Zahl {zahl} ist {suffix}.")


# gerade_ungerade()
