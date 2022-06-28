# Date: June 16, 2022
# Title: PygameFonts
# Name: Daniel Liu | 101231285
# Description: This program lets you choose a font section in the terminal (eg. a-c, d-f, ...) and it will display 
# all the section's SysFonts

import pygame, fFuncts

N_SECTS = 8
WHITE = (240, 240, 240)
NAVY = (60, 55, 100)
N_MENU_SECTS = 11
        
#Function: - returns a valid section # in menu from 1 - 11, or 0 if user wants to quit
#          - if invalid sect # entered, user is prompted again
def get_validSectN():
    valid_sect = False
    sect_n = 0

    while valid_sect == False:
        u_input = input()

        if u_input.lower() == 'q':
            valid_sect = True;  break   # return sect_n = 0

        elif u_input.isdigit():
            sect_n = int(u_input)

            if sect_n >= 1 and sect_n <= N_MENU_SECTS:
                valid_sect = True;  break

        #else u_input is invalid
        print("Invalid option. Please enter again: ", end='')

    return sect_n
    

pygame.init()
pygame.display.set_caption("Pygame SysFonts Reference")
win = pygame.display.set_mode((850, 600))
win.fill(NAVY)

#main
fonts = pygame.font.get_fonts()
font_sects = fFuncts.sortFontsAlpha(fonts)
font_sects[0].remove('bookshelfsymbol7')

#Display sect lists of SysFonts
# for i in range(0, len(font_sects), 1):
#     print("Sect ", i, ": ", font_sects[i], sep='')
#     print("# fonts:", len(font_sects[i]), "\n")


sect_n = 0;  
quit = False
pygame.display.update()
fFuncts.display_sect(win, font_sects, 1)  #blit fonts
fFuncts.display_menu()

#Get sect # and display fonts
while quit == False:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            quit = True;  exit()

    sect_n = get_validSectN()
    
    if sect_n == 0:
        quit = True;  break

    win.fill(NAVY)
    fFuncts.display_sect(win, font_sects, sect_n)
    pygame.display.update()

    print("Sect #: ", end='')





    







