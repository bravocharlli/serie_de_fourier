from fourier import *
import pygame

USER = 0
FOURIER = 1
TWO_PI = pi * 2

x = []
fourierX = []
time = 0
path = []
drawing = []
state = -1


def init(drawing):
    for i in range(len(drawing)):
        x.insert(0, Complex(drawing[i][0], drawing[i][1]))

    fourierX = dft(x)
    debut = fourierX[:int(len(fourierX)/2)]
    fin = fourierX[int(len(fourierX)/2):]
    temp = []
    for i in range(min(len(debut), len(fin))):
        temp.append(debut[i])
        temp.append(fin[-i])

    fourierX = temp
    return fourierX

def epicycles(screen, x, y, rotation, fourier):
  for i in range(len(fourier)):
    prevx = x
    prevy = y
    freq = fourier[i][2]
    radius = fourier[i][3]
    phase = fourier[i][4]
    x += radius * cos(freq * time + phase + rotation)
    y += radius * sin(freq * time + phase + rotation)

    # desiner la ligne
    pygame.draw.line(screen, [0, 0, 0], [x + 600, y + 360], [prevx + 600, prevy + 360] )

  return x + 600, y + 360




pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
time = 0

figure = [[-200, -200], [-196, -200], [-192, -200], [-188, -200], [-184, -200], [-180, -200], [-176, -200], [-172, -200], [-168, -200], [-164, -200], [-160, -200], [-156, -200], [-152, -200], [-148, -200], [-144, -200], [-140, -200], [-136, -200], [-132, -200], [-128, -200], [-124, -200], [-120, -200], [-116, -200], [-112, -200], [-108, -200], [-104, -200], [-100, -200], [-96, -200], [-92, -200], [-88, -200], [-84, -200], [-80, -200], [-76, -200], [-72, -200], [-68, -200], [-64, -200], [-60, -200], [-56, -200], [-52, -200], [-48, -200], [-44, -200], [-40, -200], [-36, -200], [-32, -200], [-28, -200], [-24, -200], [-20, -200], [-16, -200], [-12, -200], [-8, -200], [-4, -200], [0, -200], [4, -200], [8, -200], [12, -200], [16, -200], [20, -200], [24, -200], [28, -200], [32, -200], [36, -200], [40, -200], [44, -200], [48, -200], [52, -200], [56, -200], [60, -200], [64, -200], [68, -200], [72, -200], [76, -200], [80, -200], [84, -200], [88, -200], [92, -200], [96, -200], [100, -200], [104, -200], [108, -200], [112, -200], [116, -200], [120, -200], [124, -200], [128, -200], [132, -200], [136, -200], [140, -200], [144, -200], [148, -200], [152, -200], [156, -200], [160, -200], [164, -200], [168, -200], [172, -200], [176, -200], [180, -200], [184, -200], [188, -200], [192, -200], [196, -200], [200, -196], [200, -192], [200, -188], [200, -184], [200, -180], [200, -176], [200, -172], [200, -168], [200, -164], [200, -160], [200, -156], [200, -152], [200, -148], [200, -144], [200, -140], [200, -136], [200, -132], [200, -128], [200, -124], [200, -120], [200, -116], [200, -112], [200, -108], [200, -104], [200, -100], [200, -96], [200, -92], [200, -88], [200, -84], [200, -80], [200, -76], [200, -72], [200, -68], [200, -64], [200, -60], [200, -56], [200, -52], [200, -48], [200, -44], [200, -40], [200, -36], [200, -32], [200, -28], [200, -24], [200, -20], [200, -16], [200, -12], [200, -8], [200, -4], [200, 0], [200, 4], [200, 8], [200, 12], [200, 16], [200, 20], [200, 24], [200, 28], [200, 32], [200, 36], [200, 40], [200, 44], [200, 48], [200, 52], [200, 56], [200, 60], [200, 64], [200, 68], [200, 72], [200, 76], [200, 80], [200, 84], [200, 88], [200, 92], [200, 96], [200, 100], [200, 104], [200, 108], [200, 112], [200, 116], [200, 120], [200, 124], [200, 128], [200, 132], [200, 136], [200, 140], [200, 144], [200, 148], [200, 152], [200, 156], [200, 160], [200, 164], [200, 168], [200, 172], [200, 176], [200, 180], [200, 184], [200, 188], [200, 192], [200, 196], [196, 200], [192, 200], [188, 200], [184, 200], [180, 200], [176, 200], [172, 200], [168, 200], [164, 200], [160, 200], [156, 200], [152, 200], [148, 200], [144, 200], [140, 200], [136, 200], [132, 200], [128, 200], [124, 200], [120, 200], [116, 200], [112, 200], [108, 200], [104, 200], [100, 200], [96, 200], [92, 200], [88, 200], [84, 200], [80, 200], [76, 200], [72, 200], [68, 200], [64, 200], [60, 200], [56, 200], [52, 200], [48, 200], [44, 200], [40, 200], [36, 200], [32, 200], [28, 200], [24, 200], [20, 200], [16, 200], [12, 200], [8, 200], [4, 200], [0, 200], [-4, 200], [-8, 200], [-12, 200], [-16, 200], [-20, 200], [-24, 200], [-28, 200], [-32, 200], [-36, 200], [-40, 200], [-44, 200], [-48, 200], [-52, 200], [-56, 200], [-60, 200], [-64, 200], [-68, 200], [-72, 200], [-76, 200], [-80, 200], [-84, 200], [-88, 200], [-92, 200], [-96, 200], [-100, 200], [-104, 200], [-108, 200], [-112, 200], [-116, 200], [-120, 200], [-124, 200], [-128, 200], [-132, 200], [-136, 200], [-140, 200], [-144, 200], [-148, 200], [-152, 200], [-156, 200], [-160, 200], [-164, 200], [-168, 200], [-172, 200], [-176, 200], [-180, 200], [-184, 200], [-188, 200], [-192, 200], [-196, 200], [-200, 192], [-200, 188], [-200, 184], [-200, 180], [-200, 176], [-200, 172], [-200, 168], [-200, 164], [-200, 160], [-200, 156], [-200, 152], [-200, 148], [-200, 144], [-200, 140], [-200, 136], [-200, 132], [-200, 128], [-200, 124], [-200, 120], [-200, 116], [-200, 112], [-200, 108], [-200, 104], [-200, 100], [-200, 96], [-200, 92], [-200, 88], [-200, 84], [-200, 80], [-200, 76], [-200, 72], [-200, 68], [-200, 64], [-200, 60], [-200, 56], [-200, 52], [-200, 48], [-200, 44], [-200, 40], [-200, 36], [-200, 32], [-200, 28], [-200, 24], [-200, 20], [-200, 16], [-200, 12], [-200, 8], [-200, 4], [-200, 0], [-200, -4], [-200, -8], [-200, -12], [-200, -16], [-200, -20], [-200, -24], [-200, -28], [-200, -32], [-200, -36], [-200, -40], [-200, -44], [-200, -48], [-200, -52], [-200, -56], [-200, -60], [-200, -64], [-200, -68], [-200, -72], [-200, -76], [-200, -80], [-200, -84], [-200, -88], [-200, -92], [-200, -96], [-200, -100], [-200, -104], [-200, -108], [-200, -112], [-200, -116], [-200, -120], [-200, -124], [-200, -128], [-200, -132], [-200, -136], [-200, -140], [-200, -144], [-200, -148], [-200, -152], [-200, -156], [-200, -160], [-200, -164], [-200, -168], [-200, -172], [-200, -176], [-200, -180], [-200, -184], [-200, -188], [-200, -192], [-200, -196]]

fourierX = init(figure)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill([255, 255, 255])

    # render
    x, y = epicycles(screen, 0, 0, 0, fourierX)
    path.append([x, y])
    for i in path:
        pygame.draw.rect(screen, [0, 0, 0], [i[0], i[1], 1, 1])




    dt = TWO_PI / len(fourierX)
    time += dt
    if time > TWO_PI:
      time = 0
      path = []


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
