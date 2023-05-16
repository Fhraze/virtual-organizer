from os import system
from keyboard import is_pressed
from time import sleep

# Terminal colors
class colors:
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    PINK = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Main variables
select = 0
menu = 0
options = [["Esmirilhadeira", "Parafusadeira", "Furadeira"], [f"{colors.GREEN}Makita(Verde){colors.END}", f"{colors.YELLOW}Dewalt(Amarelo){colors.END}", f"{colors.BLUE}Bosch(Azul){colors.END}"], [f"Adicionar({colors.GREEN}+{colors.END})", f"Remover({colors.PINK}-{colors.END})"]]
cursor = f"{colors.PINK}> {colors.END}"
delay = True

# Selections
tool = 0
brand = 0

def option(_select):
    for i in range(0, len(options[menu])):
        if i == _select:
            print(f"{cursor}{options[menu][i]}")
        else:
            print(f"{options[menu][i]}")

while True:
    if is_pressed("enter") and menu < 2:
        if menu == 0:
            tool = options[menu][select]
            menu += 1
        else:
            brand = options[menu][select]
            menu += 1
        delay = True
    elif is_pressed("esc") and menu > 0:
        menu -= 1
        delay = True
    elif is_pressed("up"):
        if select > 0:
            select -= 1
        else:
            select = len(options[menu]) - 1
        delay = True
    
    elif is_pressed("down"):
        if select < len(options[menu]) - 1:
            select += 1
        else:
            select = 0
        delay = True

    if delay:
        system('cls')
        print(f"  /      {colors.PINK}O{colors.END}      \\")
        print(f" /    {colors.PINK}o{colors.END}          \\")
        print(f"|          {colors.PINK}°{colors.END}      |")
        print(f"|{colors.PINK}{colors.UNDERLINE}{colors.BOLD}Virtual Organizer{colors.END}|")
        print("|_________________|\n")
        option(select)
        sleep(0.2)
    sleep(0.005)
    delay = False

# máquinas de coloração: Verde, Amarela e Azul
# marca Makita, Dewalt e Bosch
# esmirilhadeira, parafusadeira, furadeira
# prateleiras: 1 e 4,   2 e 5,   3 e 6

# Funções
# seleção de máquina
# seleção de marca/cor
# adicionar e remover
# gráfico sempre visível

# salva os dados em um arquivo
#| |  | |  | |  | |  | |  | |
#| |  | |  | |  | |  | |  | |
#| |  | |  | |  | |  | |  | |
#| |  | |  | |  | |  | |  | |
#| |  | |  | |  | |  | |  | |
#| |  | |  | |  | |  | |  | |
#| |  | |  | |  | |  | |  | |
#| |  | |  | |  | |  | |  | |
#| |  | |  | |  | |  | |  | |
#| |  | |  | |  | |  | |  | |
#| |  | |  | |  | |  | |  | |
#| |  | |  | |  | |  | |  | |
#| |  | |  | |  | |  | |  | |
#| |  | |  | |  | |  | |  | |
#| |  | |  | |  | |  | |  | |
