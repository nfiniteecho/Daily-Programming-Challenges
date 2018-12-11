import re

# Given three integers between 0 and 255, corresponding to the red, green, 
# and blue channel values of a color, find the hex string for that color.
def hexcolor(r, g, b):

    red = hex(r).split('0x')
    green = hex(g).split('0x')
    blue = hex(b).split('0x')

    def pad(hc):
        if int(hc, 16) < 16:
            return '0' + str(hc)
        else:
            return str(hc)
 
    hexrbg = '#'+ pad(red[1]) + pad(green[1]) + pad(blue[1])
    return print(hexrbg.upper())

# Blend any number of hex colors together
# This is not actually the best way to blend two hex colors: 
# to do it properly you need gamma correction. 
# But we'll leave that for another time!
def blend(color_list):
    n = len(color_list)

    # Remove hash before hex characters & use regex to split
    for i in range (0, n):
        color_list[i] = color_list[i][1:]
        color_list[i] = re.findall('..', color_list[i])

    blended = '#'

    # Three values (r, g, b)
    for rgb in range(0, 3):

        # Reset average each iteration
        av = 0

        # n hex colors to average
        for numHex in range(0, n):
            av += int(color_list[numHex][rgb], 16)

        # calculate average, convert to hex/split, round, add to hex string
        av = round(av / n)
        av = hex(av).split('0x')
        blended += str(av[1])

    return print('Blended ' + str(n) + ' number of hex colors to obtain: ' + blended.upper())

hexcolor(255, 99, 71)
hexcolor(184, 134, 11)
hexcolor(189, 183, 107)
hexcolor(0, 0, 205)
hexcolor(15, 9, 205)
blend(['#000000', '#778899'])
blend(['#E6E6FA', '#FF69B4', '#B0C4DE'])