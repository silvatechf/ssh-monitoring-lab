import subprocess
import re
import sys
import time

# ==============================================================================
# CONFIGURACIÓN Y ESTÁNDARES INTERNACIONALES
# ==============================================================================
# Identificador de la matriz MITRE ATT&CK para Ataques de Fuerza Bruta
MITRE_TACTIC = "Credential Access"
MITRE_TECHNIQUE_ID = "T1110"
MITRE_TECHNIQUE_NAME = "Brute Force"

print("=" * 70)
print(f"🛡️ MOTOR VEREDICT SENTINEL - MONITORIZACIÓN DE TELEMETRÍA SSH")
print(f"🔗 Mapeo de Matriz MITRE ATT&CK: {MITRE_TECHNIQUE_ID} ({MITRE_TECHNIQUE_NAME})")
print("=" * 70)

def monitor_ssh_telemetry():
    """
    Captura y analiza los eventos de autenticación SSH en tiempo real utilizando
    herramientas nativas del sistema (journalctl) mediante flujos de subprocess.
    """
    cmd = ["journalctl", "-u", "ssh", "-f", "-n", "0"]
    
    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("[+] Monitor activo. Escuchando eventos de autenticación...")
        
        failed_pattern = re.compile(r"Failed password for .* from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")

        while True:
            line = process.stdout.readline()
            if not line:
                break
                
            match = failed_pattern.search(line)
            if match:
                attacker_ip = match.group(1)
                print(f"\n[!] ALERT: Intento de acceso fallido detectado.")
                print(f"    - IP Origen: {attacker_ip}")
                print(f"    - Táctica MITRE: {MITRE_TACTIC}")
                print(f"    - Técnica Core: {MITRE_TECHNIQUE_ID} - {MITRE_TECHNIQUE_NAME}")
                print(f"    - Acción SOC recomendada: Extraer IoC e iniciar enriquecimiento CTI.")
                
    except KeyboardInterrupt:
        print("\n[-] Monitorización detenida por el analista.")
        process.terminate()
    except Exception as e:
        print(f"[!] Error crítico en el flujo de telemetría: {e}")
        sys.exit(1)

if __name__ == "__main__":
    monitor_ssh_telemetry()
