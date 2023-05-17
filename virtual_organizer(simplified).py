from os import system, path, mkdir, environ, getppid
from keyboard import is_pressed
from time import sleep
from numpy import asarray, savetxt, loadtxt
from matplotlib import pyplot as plt
from win32process import GetWindowThreadProcessId
from win32gui import GetForegroundWindow

current_process_pid = getppid()
home = environ['USERPROFILE'] + "\\"
directory = 'Documents\\VirtO_data'
VirtO_path = home + directory

# Create data folder
try:
    mkdir(VirtO_path)
except:
    print("")

# Get or create data.csv
data_path = VirtO_path + '\\data.csv'
if path.isfile(data_path):
    data = loadtxt(data_path, delimiter = ',')
else:
    data = asarray([[0, 0, 0,  0, 0, 0]])
    savetxt(data_path, data, delimiter = ',')
    data = loadtxt(data_path, delimiter = ',')

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
    ERROR = '\033[41;30m'

# Main variables
select = 0
hor_select = 0
menu = 0
months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
options = [["Adicionar/remover máquina", "Gerar gráfico"], ["Esmerilhadeira", "Parafusadeira", "Furadeira"], [f"Makita({colors.GREEN}Verde{colors.END})", f"Dewalt({colors.YELLOW}Amarelo{colors.END})", f"Bosch({colors.BLUE}Azul{colors.END})"], [f"Adicionar({colors.GREEN}+{colors.END})", f"Remover({colors.RED}-{colors.END})"], [f"Mês [{colors.GREEN}<={colors.END}] {months[hor_select]} [{colors.GREEN}=>{colors.END}]", f"{colors.UNDERLINE}Gerar{colors.END}"]]
info = [f"{colors.RED}X{colors.END} Aperte ESC para fechar o programa", f"{colors.RED}<={colors.END} Aperte ESC para retornar ao menu anterior", f"{colors.RED}<={colors.END} Aperte ESC para retornar ao menu anterior", f"{colors.RED}<={colors.END} Aperte ESC para retornar ao menu anterior", f"{colors.RED}<={colors.END} Aperte ESC para retornar ao menu anterior", "[^] [v] Use as setas para navegar\n[Enter¬] Use Enter para selecionar"]
cursor = f"{colors.SELECTOR}> {colors.END}"
delay = True
update = ""

# Selections
tool = 0
brand = 0

# pyplot variables
fig, ax = plt.subplots()
shelves = ['Makita', 'Dewalt', 'Bosch', 'Makita 2', 'Dewalt 2', 'Bosch 2']
shelf = 1
bar_labels = ['Makita', 'Dewalt', 'Bosch', '_Makita 2', '_Dewalt 2', '_Bosch 2']
bar_colors = ['tab:green', 'gold', 'tab:blue', 'tab:green', 'gold', 'tab:blue']

# Print options
def option(_select):
    for i in range(0, len(options[menu])):
        if i == _select:
            print(f"{cursor}{options[menu][i]}")
        else:
            print(f"{options[menu][i]}")
    print(f"\n{info[menu]}")

# Add/remove values from data
def data_change(operation):
    match operation:
        case "add":
            if not update == f"{colors.ERROR}! Todas as prateleiras para essa marca estão cheias!{colors.END}":
                data[shelf] += 1
                savetxt(data_path, data, delimiter = ',')
        case "remove":
            if not update == f"{colors.ERROR}! Todas as prateleiras para essa marca estão vazias!{colors.END}":
                data[shelf] -= 1
                savetxt(data_path, data, delimiter = ',')

# Get appropriate shelf
def calc_shelf(operation):
    global shelf
    global update
    match operation:
        case "add":
            if data[brand] < 15:
                shelf = brand
                update = f"{colors.GREEN}+{colors.END} {options[1][tool]} da marca {shelves[brand]} foi adicionada à prateleira {shelf+1}."
            elif data[brand+3] < 15:
                shelf = brand + 3
                update = f"{colors.GREEN}+{colors.END} {options[1][tool]} da marca {shelves[brand]} foi adicionada à prateleira {shelf+1}."
            else:
                update = f"{colors.ERROR}! Todas as prateleiras para essa marca estão cheias!{colors.END}"
        case "remove":
            if data[brand+3] > 0:
                shelf = brand+3
                update = f"{colors.RED}-{colors.END} {options[1][tool]} da marca {shelves[brand]} foi removida da prateleira {shelf+1}."
            elif data[brand] > 0:
                shelf = brand
                update = f"{colors.RED}-{colors.END} {options[1][tool]} da marca {shelves[brand]} foi removida da prateleira {shelf+1}."
            else:
                update = f"{colors.ERROR}! Todas as prateleiras para essa marca estão vazias!{colors.END}"

# Generate graph
def gen_graph():
    ax.bar(shelves, data, label = bar_labels, color = bar_colors)
    ax.set_title(f"Prateleiras - {months[hor_select]}", fontsize = 20)
    ax.set_ylabel('Lotação das prateleiras')
    ax.legend(title = 'Marcas')
    plt.savefig(f"{VirtO_path}\\{months[hor_select]}-Gráfico-Prateleiras.png")
    plt.show()

# Main loop
while True:
    focus_window_pid = GetWindowThreadProcessId(GetForegroundWindow())[1]
    if focus_window_pid == current_process_pid:
        if is_pressed("enter"):
            match menu:
                case 0:
                    if select == 0:
                        menu = 1
                    else:
                        menu = 4
                case 1:
                    tool = select
                    menu = 2
                case 2:
                    brand = select
                    menu = 3
                case 3:
                    if select == 0:
                        calc_shelf("add")
                        data_change("add")
                    else:
                        calc_shelf("remove")
                        data_change("remove")
                    menu = 0
                case 4:
                    if select == 1:
                        gen_graph()
                        update = f"{colors.SELECTOR}?{colors.END} Gráfico salvo em: {VirtO_path}\\{months[hor_select]}-Gráfico-Prateleiras.png"
                        menu = 0
            select = 0
            delay = True
        elif is_pressed("esc"):
            if menu > 0:
                if menu == 4:
                    menu = 0
                else:
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

    if menu == 4 and select == 0:
        if is_pressed("left"):
            if hor_select > 0:
                hor_select -= 1
            else:
                hor_select = 11
            options[4][0] = f"Mês [{colors.GREEN}<={colors.END}] {months[hor_select]} [{colors.GREEN}=>{colors.END}]"
            delay = True
        if is_pressed("right"):
            if hor_select < 11:
                hor_select += 1
            else:
                hor_select = 0
            options[4][0] = f"Mês [{colors.GREEN}<={colors.END}] {months[hor_select]} [{colors.GREEN}=>{colors.END}]"
            delay = True
    
    if delay:
        data = loadtxt(data_path, delimiter = ',')
        system('cls')
        print(f"{colors.TITLE}Virtual Organizer{colors.END}\n")
        print(f"{info[-1]}\n")
        option(select)
        print(f"\n{update}")
        sleep(0.2)
    sleep(0.005)
    delay = False
