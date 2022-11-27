"""
Speichern Sie die Namen einiger Ihrer Freunde in einer Liste mit Namen. Drucken Sie den Namen jeder Person, indem Sie nacheinander auf jedes Element in der Liste zugreifen.
"""
freunde = ["A", "B", "C", "D"]


def print_freundes_liste(freunde):
    print(freunde[0])
    print(freunde[1])
    print(freunde[2])
    print(freunde[3])


# print_freundes_liste(freunde)

"""
Beginnen Sie mit der Liste, die Sie in Übung 1.1 verwendet haben: Begrüssen Sie jede Person mit einer personalisierten Nachricht.
"""


def print_begruesse_freunde(freunde):
    print(f"Hallo {freunde[0]}")
    print(f"Hallo {freunde[1]}")
    print(f"Hallo {freunde[2]}")
    print(f"Hallo {freunde[3]}")

# print_begruesse_freunde(freunde)


"""
Erstellen Sie eine Funktion die eine Liste von Personen enthält. Die Funktion nimmt dann denn Index einer spezifischen Person als Argument und begrüsst dann die spezifische Person.
"""


def print_begruesse_freund_by_index(index):
    freunde = ["A", "B", "C", "D"]
    print(f"Hallo {freunde[index]}")


# print_begruesse_freund_by_index(0)
