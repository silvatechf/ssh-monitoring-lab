# Veredict Sentinel - SSH Telemetry Monitor & Mitre Mapping

**Veredict Sentinel** es un motor de monitorización de telemetría de seguridad nativa en entornos Linux, especializado en la detección, análisis y triaje en tiempo real de ataques de autenticación por fuerza bruta sobre el protocolo SSH. 

Este componente actúa como el **Lab 1** de la arquitectura Veredict, sirviendo como la primera línea de defensa activa (SIEM-ready) que detecta las amenazas en la capa de transporte para aislar Indicadores de Compromiso (IoCs) antes de su escalada en la infraestructura corporativa.

---

## 📊 Evidencia Operacional (Detección en Tiempo Real)

El motor captura los flujos del sistema de forma reactiva y mapea los incidentes bajo taxonomía internacional. Los logs enriquecidos se visualizan con el siguiente formato estructurado:

```plaintext
======================================================================
🛡️ MOTOR VEREDICT SENTINEL - MONITORIZACIÓN DE TELEMETRÍA SSH
🔗 Mapeo de Matriz MITRE ATT&CK: T1110 (Brute Force)
======================================================================
[+] Monitor activo. Escuchando eventos de autenticación...

[!] ALERT: Intento de acceso fallido detectado.
    - IP Origen: 192.168.1.50
    - Táctica MITRE: Credential Access
    - Técnica Core: T1110 - Brute Force
    - Acción SOC recomendada: Extraer IoC e iniciar enriquecimiento CTI.
