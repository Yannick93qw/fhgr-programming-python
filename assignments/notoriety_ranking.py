"""
Bauen Sie eine Funktion die anhand der eingegebenen Punktzahl den Notoriety-Level zurückgibt
"""


def notoriety_ranking(points):
    notoriety_ranks = {
        "Neutral": [x for x in range(0, 400)],
        "Accepted": [x for x in range(400, 1000)],
        "Liked": [x for x in range(1000, 2000)],
        "Trusted": [x for x in range(2000, 4000)],
        "Idolized": [x for x in range(4000, 8000)],
        "Renowed": [x for x in range(8000, 20000)],
    }

    glorious_points = 20000
    forever_alone_points = -1
    if points >= glorious_points:
        print("Glorious")
    elif points <= forever_alone_points:
        print("Forever Alone")
    else:
        for rank, point_range in notoriety_ranks.items():
            if points in point_range:
                print(rank)


notoriety_ranking(20000)
