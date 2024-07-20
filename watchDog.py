import subprocess
import sys
import time

# Nome del programma da controllare in esecuzione
nome_programma = "bot_LH_BM.py"

def is_program_running(program_name):
    """Controlla se un programma è in esecuzione."""
    try:
        # Esegui il comando 'pgrep' per cercare il programma
        output = subprocess.check_output(["pgrep", "-f", program_name])
        return True if output else False
    except subprocess.CalledProcessError:
        # Se 'pgrep' non trova il programma, solleva un'eccezione
        return False

def run_in_background(script_name):
    """Avvia un programma in background."""
    try:
        # Esegui il programma in background
        subprocess.Popen([sys.executable, script_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"{script_name} è stato avviato in background.")
    except Exception as e:
        print(f"Errore nell'avvio di {script_name}: {e}")

if __name__ == "__main__":
    while True:
        if is_program_running(nome_programma):
            print(f"{nome_programma} è attualmente in esecuzione.")
        else:
            print(f"{nome_programma} non è in esecuzione. Avvio...")
            run_in_background(nome_programma)
        
        # Attendi un intervallo di tempo prima di controllare di nuovo
        time.sleep(5)  # Controlla ogni 5 secondi
