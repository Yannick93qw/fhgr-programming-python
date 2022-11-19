"""
Schreiben Sie eine Funktion die den Preis für eine Taxifahrt berechnet:

Pro Fahrt wird ein Startpreis von 8.-CHF am Tag und 10.-CHF in der Nacht berechnet.
Pro gefahrener Kilometer werden 3.-CHF am Tag und 4.-CHF in der Nacht berechnet.
Die ersten 2 Kilometer sind im Startpreis inbegriffen.

Die Funktion soll dabei folgende Argumente entgegen nehmen:
Tageszeit (“Tag” oder “Nacht”)
Die Strecke in Kilometer

Erweitern Sie die Funktion sodass sie den Benutzer nach den Daten abfragt, also ohne Argumente aufgerufen werden muss.
"""


def strecke_in_km():
    km = int(input("Wie viele Kilometer bist du heute gefahren? "))
    tageszeit = input("Was ist für eine Tageszeit (Nacht/Tag)? ")

    ist_nacht = tageszeit.lower() == "nacht"
    preis = 10 if ist_nacht else 8
    km_preis = 4 if ist_nacht else 3

    preis += (km - 2) * km_preis

    print(
        f"Preis für {km} km in der Tageszeit '{tageszeit}' ist {preis} CHF")


strecke_in_km()
