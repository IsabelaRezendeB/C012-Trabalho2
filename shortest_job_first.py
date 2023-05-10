import time
import curses

class Process:
    def __init__(self, name, burstTime):
        self.name = name
        self.burstTime = burstTime

def sort(processes):
    sorted_processes = sorted(processes, key=lambda x: x.burstTime)
    return (sorted_processes)

def sjf(processes, n):
    screen = curses.initscr()
    curses.noecho()

    table = [
        ["Processo", "Tempo"],
    ]

    screen.addstr(0, 0, "Processos")
    screen.addstr(0, 15, "Tempo")

    sorted_processes = sort(processes)

    tempos_espera = []
    ms = 0
    aux = 0

    for i, process in enumerate(sorted_processes):
        linha = ""
        tempos_espera.append(aux + process.burstTime)
        aux = aux + process.burstTime
        while process.burstTime > 0:
            row = [process.name, str(ms)]
            table.append(row)
            ms += 1
            time.sleep(1)
            antigo = linha
            linha = antigo + " " + str(ms)
            process.burstTime -= 1
            screen.addstr(i+2, 0, row[0])
            screen.addstr(i+2, 15, linha)
            screen.refresh()
    tempos_espera.pop()
    temp = sum(tempos_espera) / n
    time.sleep(1)
    screen.addstr(len(processes)+3, 0, f"Tempo Medio de Espera: {temp:.2f}")

    screen.getch()
    curses.endwin()



print("========== SHORTEST JOB FIRST ==========")

n = int(input ("Entre com a quantidade de processos: "))
burstTime = []
processes = []

print("Considerando que todos chegaram no mesmo instante, entre com o Burst Time dos processos:")

for x in range(0, n):
    processName = chr(ord('A')+x)
    print(processName, end = "")
    burstTime.append(float(input(" : ")))
    paux = Process(processName, burstTime[x])
    processes.append(paux)
    
sjf(processes, n)