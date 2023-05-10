import time
import curses

class Process:
    def __init__(self, name, burstTime):
        self.name = name
        self.burstTime = burstTime

def fcfs(processes, n):
    screen = curses.initscr()
    curses.noecho()

    table = [
        ["Processo", "Tempo"],
    ]

    screen.addstr(0, 0, "Processos")
    screen.addstr(0, 15, "Tempo")

    tempos_espera = []
    ms = 1
    aux = 0

    for i, process in enumerate(processes):
        linha = ""
        tempos_espera.append(aux + process.burstTime)
        aux = aux + process.burstTime
        while process.burstTime > 0:
            row = [process.name, str(ms)]
            table.append(row)
            time.sleep(1)
            process.burstTime -= 1
            # concatenate the old ms value with the new one
            antigo = linha
            linha = antigo + " " + str(ms)
            ms += 1
            # print the updated row with the new time next to the old one
            screen.addstr(i+2, 0, row[0])
            screen.addstr(i+2, 15, linha)
            screen.refresh()
    tempos_espera.pop()
    temp = sum(tempos_espera) / n
    time.sleep(1)
    screen.addstr(len(processes)+3, 0, f"Tempo Medio de Espera: {temp:.2f}")

    screen.getch()
    curses.endwin()



print("========== FIRST COME FIRST SERVED ==========")

n = int(input ("Entre com a quantidade de processos: "))
burstTime = []
processes = []

print("Em ordem de chegada, entre com o Burst Time dos processos:")

for x in range(0, n):
    processName = chr(ord('A')+x)
    print(processName, end = "")
    burstTime.append(float(input(" : ")))
    paux = Process(processName, burstTime[x])
    processes.append(paux)
    
fcfs(processes, n)