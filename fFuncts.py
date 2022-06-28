# Date: June 16, 2022
# Title: Test
# Name: Daniel Liu | 101231285
# Description: This is a program contains functs for PygameFonts

import pygame

WHITE = (240, 240, 240)
BLACK = (0, 0, 0)
N_SECTS = 8;  N_MENU_SECTS = 11
FONT_H = 30;  F_MARGIN = 10
NFONTS_COL = 12


def sortFontsAlpha(fonts):
    font_sects = []

    for i in range(0, N_SECTS, 1):
        font_sects.append([])

    #store fonts in letter1 - letter2 sects
    for f in fonts:
        first_c = f[0].lower()

        if ord(first_c) >= ord('a') and ord(first_c) <= ord('c'):
            # print(first_c, "'s dec ", ord(first_c), " is >= a's dec ", ord('a'), " and <= c's dec ", ord('c'), sep='')
            font_sects[0].append(f)

        elif ord(first_c) >= ord('d') and ord(first_c) <= ord('f'):
            font_sects[1].append(f)

        elif ord(first_c) >= ord('g') and ord(first_c) <= ord('i'):
            font_sects[2].append(f)
        
        elif ord(first_c) >= ord('j') and ord(first_c) <= ord('l'):
            font_sects[3].append(f)

        elif ord(first_c) >= ord('m') and ord(first_c) <= ord('o'):
            font_sects[4].append(f)

        elif ord(first_c) >= ord('p') and ord(first_c) <= ord('r'):
            font_sects[5].append(f)

        elif ord(first_c) >= ord('s') and ord(first_c) <= ord('v'):
            font_sects[6].append(f)

        else:   #w - z
            font_sects[7].append(f)

    #sort
    for sect in font_sects:
        sect.sort()

    return font_sects


def display_menu():
    print("Enter sect # for fonts you want to display, or 'q' to quit: ")
    print("1. a - c                 6. m - o")
    print("2. a - c (2)             7. m - o (2)")
    print("3. d - f                 8. p - r")
    print("4. g - i                 9. s - v")
    print("5. j - l                10. s - v (2)")
    print("                        11. w - z")
    print("")
    print("Sect #: ", end='')

#Args: win - window surface
#      font_sect - list of SysFonts a-c, d-f, or ...
#      start_i   - starting index to display SysFonts
#Function: Blits the SysFonts in 2 cols of 12 fonts each
def display_fontSect(win, font_sect, start_i):
    topL_x, topL_y = (50, 50)
    f_i = start_i

    #display 1st col
    for f in range(0, NFONTS_COL, 1):

        if f_i == len(font_sect): break

        font = pygame.font.SysFont(font_sect[f_i], FONT_H)
        font_sfc = font.render(font_sect[f_i], True, WHITE)
        f_rect =  font_sfc.get_rect(topleft=(topL_x, topL_y))
        win.blit(font_sfc, f_rect)

        f_i += 1;  topL_y += (FONT_H + F_MARGIN)

    #display 2nd col
    topL_x, topL_y = (350, 50)

    for f in range(0, NFONTS_COL, 1):

        if f_i == len(font_sect): break

        font = pygame.font.SysFont(font_sect[f_i], FONT_H)
        font_sfc = font.render(font_sect[f_i], True, WHITE)
        f_rect =  font_sfc.get_rect(topleft=(topL_x, topL_y))
        win.blit(font_sfc, f_rect)

        f_i += 1;  topL_y += (FONT_H + F_MARGIN)

    pygame.display.update()

#Args: win - window surface
#      font_sects - list of 8 lists, each containing SysFonts in sections a-c, d-f, ...
#      sect_n     - # of menu sect to display
#Function: checks which list of SysFonts in font_sects to display & calls display_fontSect(), which blits the SysFonts
def display_sect(win, font_sects, sect_n):

    if sect_n == 1: display_fontSect(win, font_sects[0], 0)
    elif sect_n == 2: display_fontSect(win, font_sects[0], 24)
    elif sect_n == 3: display_fontSect(win, font_sects[1], 0)
    elif sect_n == 4: display_fontSect(win, font_sects[2], 0)
    elif sect_n == 5: display_fontSect(win, font_sects[3], 0)

    elif sect_n == 6: display_fontSect(win, font_sects[4], 0)
    elif sect_n == 7: display_fontSect(win, font_sects[4], 24)
    elif sect_n == 8: display_fontSect(win, font_sects[5], 0)
    elif sect_n == 9: display_fontSect(win, font_sects[6], 0)
    elif sect_n == 10: display_fontSect(win, font_sects[6], 24)
    elif sect_n == 11: display_fontSect(win, font_sects[7], 0)


#test funct
def display_grid(win, win_w, win_h, square_w, square_h):
    #Vert lines
    for x in range(0, win_w, square_w):
        pygame.draw.line(win, BLACK, (x,0), (x,win_h), 1)

    #Hor lines
    for y in range(0, win_h, square_h):
        pygame.draw.line(win, BLACK, (0,y), (win_w,y), 1)


#test
