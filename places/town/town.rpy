image town = "places/town/town.png"

label town:
    scene town
    "Stai in citta"

    menu:
        "Che faccio?"

        "Vai al bar":
            call bar

        "Vai alla piazza":
            call square

        "Vai alla chiesa":
            call church

        "Vai alla torre del orologio":
            call clock_tower

    jump town

    return
    