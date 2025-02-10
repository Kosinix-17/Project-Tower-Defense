def position_fleche():
    x = 70 * t + 10
    y = 9.8 * t + 20
    return x, y


def position_mob():
    x = 28.4 * t
    y = 5
    return x, y


def tire_fleche():
    while (t < (haut_init - 10) / 70):
        x, y = position_fleche(t)
        print("La fléche est à {} m de hauteur et à {} m de distance à {} secondes".format(x, y, t))
        t += 0.1
        sleep(0.1)

