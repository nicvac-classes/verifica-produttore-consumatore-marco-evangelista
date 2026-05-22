import threading
import random

DIM_BUFFER = 7
N_PRODUTTORI = 4
N_CONSUMATORI = 3
N_RICHIESTE = 4

buffer = [None] * DIM_BUFFER
metti = 0
togli = 0

vuoto = threading.Semaphore(DIM_BUFFER)
pieno = threading.Semaphore(0)
mutexP = threading.Semaphore(1)
mutexC = threading.Semaphore(1)


def genera_drone():
    return f"DRN-{random.randint(100, 999)}"


class ProduttoreThread(threading.Thread):
    def __init__(self, idx):
        super().__init__()
        self.idx = idx

    # DA IMPLEMENTARE (run)
    def run(self)
        global metti
        while <= N_RICHIESTE:
            self.vuoto.acquire()
            self.mutexP.acquire()
            i_metti=metti
            self.dato=genera_drone()
            metti=(metti+1)%DIM_BUFFER
            self.mutexP.realise()
            self.buffer[drone]=metti
            print(f"[SENSOR-N] segnala {metti}")
            self.pieno.realise()

class ConsumatoreThread(threading.Thread):
    def __init__(self, idx):
        super().__init__()
        self.idx = idx

    # DA IMPLEMENTARE (run)
    def run(self)
        global togli
        termina=false
        while termina(false):
            self.pieno.acquire()
            self.mutexC.acquire()
            i_togli=togli
            togli=(togli+1)%DIM_BUFFER
            self.mutexC.realise()
            togli=self.buffer[i_togli]
            if togli==None:
                attiva= false
            else:
                print(f"[RUNWAY-N] autorizza atterraggio{togli}")
            
            self.vuoto.realise()

                

def main():
    global metti

    produttori = [ProduttoreThread(i + 1) for i in range(N_PRODUTTORI)]
    consumatori = [ConsumatoreThread(i + 1) for i in range(N_CONSUMATORI)]

    # DA IMPLEMENTARE: start dei thread produttori e consumatori
    for start in ProduttoreThread():
        ProduttoreThread.start()
    for start in ConsumatoreThread():
        ConsumatoreThread.start()

    # DA IMPLEMENTARE: join di tutti i produttori
    for join in ProduttoreThread():
        ProduttoreThread.join()

    print("Tutti i sensori hanno terminato. Chiusura piste...")

    # Invia una sentinella None per ogni pista attiva.
    for _ in range(N_CONSUMATORI):
        # DA IMPLEMENTARE: inserire None nel buffer
        buffer=None
        pass

    # DA IMPLEMENTARE: join di tutti i consumatori
    for join in ConsumatoreThread:
        ConsumatoreThread.join()

    print("Torre operativa chiusa.")


if __name__ == "__main__":
    main()
