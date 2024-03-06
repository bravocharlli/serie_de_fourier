from vecteur import *

# figure = [[-200, -200], [-196, -200], [-192, -200], [-188, -200], [-184, -200], [-180, -200], [-176, -200], [-172, -200], [-168, -200], [-164, -200], [-160, -200], [-156, -200], [-152, -200], [-148, -200], [-144, -200], [-140, -200], [-136, -200], [-132, -200], [-128, -200], [-124, -200], [-120, -200], [-116, -200], [-112, -200], [-108, -200], [-104, -200], [-100, -200], [-96, -200], [-92, -200], [-88, -200], [-84, -200], [-80, -200], [-76, -200], [-72, -200], [-68, -200], [-64, -200], [-60, -200], [-56, -200], [-52, -200], [-48, -200], [-44, -200], [-40, -200], [-36, -200], [-32, -200], [-28, -200], [-24, -200], [-20, -200], [-16, -200], [-12, -200], [-8, -200], [-4, -200], [0, -200], [4, -200], [8, -200], [12, -200], [16, -200], [20, -200], [24, -200], [28, -200], [32, -200], [36, -200], [40, -200], [44, -200], [48, -200], [52, -200], [56, -200], [60, -200], [64, -200], [68, -200], [72, -200], [76, -200], [80, -200], [84, -200], [88, -200], [92, -200], [96, -200], [100, -200], [104, -200], [108, -200], [112, -200], [116, -200], [120, -200], [124, -200], [128, -200], [132, -200], [136, -200], [140, -200], [144, -200], [148, -200], [152, -200], [156, -200], [160, -200], [164, -200], [168, -200], [172, -200], [176, -200], [180, -200], [184, -200], [188, -200], [192, -200], [196, -200], [200, -196], [200, -192], [200, -188], [200, -184], [200, -180], [200, -176], [200, -172], [200, -168], [200, -164], [200, -160], [200, -156], [200, -152], [200, -148], [200, -144], [200, -140], [200, -136], [200, -132], [200, -128], [200, -124], [200, -120], [200, -116], [200, -112], [200, -108], [200, -104], [200, -100], [200, -96], [200, -92], [200, -88], [200, -84], [200, -80], [200, -76], [200, -72], [200, -68], [200, -64], [200, -60], [200, -56], [200, -52], [200, -48], [200, -44], [200, -40], [200, -36], [200, -32], [200, -28], [200, -24], [200, -20], [200, -16], [200, -12], [200, -8], [200, -4], [200, 0], [200, 4], [200, 8], [200, 12], [200, 16], [200, 20], [200, 24], [200, 28], [200, 32], [200, 36], [200, 40], [200, 44], [200, 48], [200, 52], [200, 56], [200, 60], [200, 64], [200, 68], [200, 72], [200, 76], [200, 80], [200, 84], [200, 88], [200, 92], [200, 96], [200, 100], [200, 104], [200, 108], [200, 112], [200, 116], [200, 120], [200, 124], [200, 128], [200, 132], [200, 136], [200, 140], [200, 144], [200, 148], [200, 152], [200, 156], [200, 160], [200, 164], [200, 168], [200, 172], [200, 176], [200, 180], [200, 184], [200, 188], [200, 192], [200, 196], [196, 200], [192, 200], [188, 200], [184, 200], [180, 200], [176, 200], [172, 200], [168, 200], [164, 200], [160, 200], [156, 200], [152, 200], [148, 200], [144, 200], [140, 200], [136, 200], [132, 200], [128, 200], [124, 200], [120, 200], [116, 200], [112, 200], [108, 200], [104, 200], [100, 200], [96, 200], [92, 200], [88, 200], [84, 200], [80, 200], [76, 200], [72, 200], [68, 200], [64, 200], [60, 200], [56, 200], [52, 200], [48, 200], [44, 200], [40, 200], [36, 200], [32, 200], [28, 200], [24, 200], [20, 200], [16, 200], [12, 200], [8, 200], [4, 200], [0, 200], [-4, 200], [-8, 200], [-12, 200], [-16, 200], [-20, 200], [-24, 200], [-28, 200], [-32, 200], [-36, 200], [-40, 200], [-44, 200], [-48, 200], [-52, 200], [-56, 200], [-60, 200], [-64, 200], [-68, 200], [-72, 200], [-76, 200], [-80, 200], [-84, 200], [-88, 200], [-92, 200], [-96, 200], [-100, 200], [-104, 200], [-108, 200], [-112, 200], [-116, 200], [-120, 200], [-124, 200], [-128, 200], [-132, 200], [-136, 200], [-140, 200], [-144, 200], [-148, 200], [-152, 200], [-156, 200], [-160, 200], [-164, 200], [-168, 200], [-172, 200], [-176, 200], [-180, 200], [-184, 200], [-188, 200], [-192, 200], [-196, 200], [-200, 192], [-200, 188], [-200, 184], [-200, 180], [-200, 176], [-200, 172], [-200, 168], [-200, 164], [-200, 160], [-200, 156], [-200, 152], [-200, 148], [-200, 144], [-200, 140], [-200, 136], [-200, 132], [-200, 128], [-200, 124], [-200, 120], [-200, 116], [-200, 112], [-200, 108], [-200, 104], [-200, 100], [-200, 96], [-200, 92], [-200, 88], [-200, 84], [-200, 80], [-200, 76], [-200, 72], [-200, 68], [-200, 64], [-200, 60], [-200, 56], [-200, 52], [-200, 48], [-200, 44], [-200, 40], [-200, 36], [-200, 32], [-200, 28], [-200, 24], [-200, 20], [-200, 16], [-200, 12], [-200, 8], [-200, 4], [-200, 0], [-200, -4], [-200, -8], [-200, -12], [-200, -16], [-200, -20], [-200, -24], [-200, -28], [-200, -32], [-200, -36], [-200, -40], [-200, -44], [-200, -48], [-200, -52], [-200, -56], [-200, -60], [-200, -64], [-200, -68], [-200, -72], [-200, -76], [-200, -80], [-200, -84], [-200, -88], [-200, -92], [-200, -96], [-200, -100], [-200, -104], [-200, -108], [-200, -112], [-200, -116], [-200, -120], [-200, -124], [-200, -128], [-200, -132], [-200, -136], [-200, -140], [-200, -144], [-200, -148], [-200, -152], [-200, -156], [-200, -160], [-200, -164], [-200, -168], [-200, -172], [-200, -176], [-200, -180], [-200, -184], [-200, -188], [-200, -192], [-200, -196]]

def add_pos_tab(tab1, tab2):
    return [tab1[0] + tab2[0], tab1[1] + tab2[1]]


def mult_tab_int(tab1, a):
    return [tab1[0] * a, tab1[1] * a]


class Dessin:
    def __init__(self, precision, path):
        self.para = []
        self.figure = []
        self.precision = precision

    def dessin(self):
        x, y = 0, 0
        n = 0
        for i in range(self.precision):
            oldx, oldy = x, y
            x, y = vecteur(screen, oldx, oldy, t, n, self.para[i])
            n = n + ((-1) ** i) * (i + 1)

        draw.append([x, y])
        for i in draw:
            point(screen, pygame.Vector2(i[0], i[1]))
        if len(draw) > 600:
            draw.pop(0)

        for i in range(len(figure)):
            point(screen, pygame.Vector2(path(i)))

    def path(self, f):
        return self.figure[f]

    def calcul_tout_param(self, precision, figure):
        self.para = []
        n = 0

        for i in range(precision):
            self.para.append(self.parameter(n, figure))
            n = n + (-1) ** i * (i + 1)

    def parameter(self, n, figure):
        a = [0, 0]
        dt = 1 / len(figure)
        for i in range(len(figure)):
            t = i * dt
            tempo = mult_pos_tab(self.path(i), dummy_vecteur(t, n))
            tempo = mult_tab_int(tempo, dt)
            a = add_pos_tab(a, tempo)
        return a


def mult_pos_tab(tab1, tab2):
    a = tab1[0]
    b = tab1[1]
    ap = tab2[0]
    bp = tab2[1]
    return [a * ap - b * bp, a * bp + b * ap]

def mult_pos_vec(vec1, vec2):
    a = vec1.x
    b = vec1.y
    ap = vec2.x
    bp = vec2.y
    return [a * ap + b * bp, a * bp + b * ap]

def dummy_vecteur(t, n):
    x = math.cos(-n * t * (math.pi * 2))
    y = math.sin(-n * t * (math.pi * 2))
    return [x, y]