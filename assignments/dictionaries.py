"""
Verwenden Sie ein Wörterbuch, um Daten über eine Person zu speichern, die Sie kennen.
Speichern Sie deren Vornamen, Nachnamen, Alter und die Stadt, in der sie lebt. Sie
sollte dazu Schlüssel wie Vorname, Nachname, Alter und Stadt verwenden. Geben Sie die Daten die im Dictionary gespeichert sind schön formatiert aus.
"""
person = {
    "vorname": "Yannick",
    "nachname": "Hutter",
    "alter": 29,
    "stadt": "Mels"
}

# welcome_message = f"Informationen zur Person {person['vorname']} {person['nachname']}"
# print("#" * len(welcome_message))
# print(welcome_message)
# print("#" * len(welcome_message))
# print(f"Vorname: {person['vorname']}")
# print(f"Nachname: {person['nachname']}")
# print(f"Alter: {person['alter']}")
# print(f"Stadt: {person['stadt']}")

"""
Schreiben Sie eine Funktion, die ein Begriff entgegen nimmt und dessen Bedeutung/Erklärung zurück gibt.
"""


def begriffsdefinition(begriff):
    lexikon = {
        "Spam": "Spam is a very delicious food and also it is Spam",
        "42": "The answer to all things"
    }

    if lexikon.get(begriff) == None:
        print(f"Für den Begriff '{begriff}' gibt es keine Definition")
    else:
        print(f"Definition für {begriff} ist: {lexikon[begriff]}")

# begriffsdefinition("Spam")
# begriffsdefinition("Something")


"""
Überlegen Sie sich, welche zusätzlichen Inhalte in so einem Eintrag möglich oder interessant wären.
"""
...
