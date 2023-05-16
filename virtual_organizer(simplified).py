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
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    TITLE = '\033[43;30m'
    SELECTOR = '\033[33m'

# Main variables
select = 0
menu = 0
options = [["Esmerilhadeira", "Parafusadeira", "Furadeira"], [f"Makita({colors.GREEN}Verde{colors.END})", f"Dewalt({colors.YELLOW}Amarelo{colors.END})", f"Bosch({colors.BLUE}Azul{colors.END})"], [f"Adicionar({colors.GREEN}+{colors.END})", f"Remover({colors.RED}-{colors.END})"]]
info = [f"{colors.RED}--{colors.END} Aperte ESC para fechar o programa", f"{colors.RED}<={colors.END} Aperte ESC para retornar ao menu anterior", f"{colors.RED}<={colors.END} Aperte ESC para retornar ao menu anterior", "[^] [v] Use as setas para navegar\n[Enter¬] Use Enter para selecionar"]
cursor = f"{colors.SELECTOR}> {colors.END}"
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
    print(f"\n{info[menu]}")

while True:
    if is_pressed("enter") and menu < 2:
        if menu == 0:
            tool = select
            menu += 1
        else:
            brand = select
            menu += 1
        select = 0
        delay = True
    elif is_pressed("esc"):
        if menu > 0:
            menu -= 1
        else:
            system('cls')
            print("Virtual Organizer foi fechado.")
            quit()
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
        print(f"{colors.TITLE}Virtual Organizer{colors.END}\n")
        print(f"{info[3]}\n")
        option(select)
        sleep(0.2)
    sleep(0.005)
    delay = False
