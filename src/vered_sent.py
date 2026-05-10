import os
import json
from datetime import datetime
import time

LOG_FILE = "security_events.json"

def monitor_ssh():
    print("\033[92m--- VEREDICT SENTINEL: MONITORIZACIÓN ACTIVA ---\033[0m")
    cmd = "journalctl -u ssh -n 5 | grep 'Failed password'"  # Extraer últimos intentos fallidos de SSH
    
    while True:
        output = os.popen(cmd).read()
        if "Failed password" in output:
            event = {
                "timestamp": datetime.now().isoformat(),
                "status": "ALERTA",
                "attack_type": "Brute Force SSH",
                "message": "Intento de acceso no autorizado detectado"
            }
            print("\033[91m[!] AMENAZA DETECTADA: Registro generado en JSON\033[0m")
            
            # Evidencia para el análisis forense
            with open(LOG_FILE, "a") as f:
                f.write(json.dumps(event) + "\n")
                f.flush()
                
            time.sleep(2) 
        
        time.sleep(3) # Frecuencia de descaneo

if __name__ == "__main__":
    monitor_ssh()
