import schedule
import time
import threading

class SorteioAutomatico():
  
    def sorteioLoteria():
        print( 'testando2')
    
    schedule.every(10).seconds.do(sorteioLoteria) 
    
    def main():
        
        schedule.run_pending()
        time.sleep(1)