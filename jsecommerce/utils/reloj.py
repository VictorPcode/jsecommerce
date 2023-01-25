import datetime
import threading
import sys
import time

class Reloj(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        while True:
            tiempoTranscurrido = time.time()
            fecha = datetime.datetime.fromtimestamp(tiempoTranscurrido)
            horaFormateada = fecha.strftime('%H:%M:%S')
            print(horaFormateada)
            
            sys.stdout.flush()
            time.sleep(1)
            return horaFormateada
            
reloj = Reloj()

