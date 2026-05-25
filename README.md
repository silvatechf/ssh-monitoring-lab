# Veredict Sentinel - SSH Telemetry Monitor

Este repositorio contiene el **Lab 1** de la plataforma Veredict, enfocado en la monitorización de telemetría nativa de Linux y la detección de ataques de fuerza bruta en servicios críticos (SSH).

## 🏛️ Conceptos Aplicados y Estándares
* **Captura de Telemetría Nativa:** Uso del módulo `subprocess` de Python para interactuar con `journalctl` y el demonio de SSH, evitando la lectura pasiva de archivos de texto estáticos.
* **Mapeo MITRE ATT&CK:** Clasificación formal del incidente bajo la técnica **T1110 (Brute Force)**, asegurando que las alertas generadas sigan los estándares globales de la industria de la ciberseguridad.
* **Preparación para CTI:** El script actúa como la primera línea de defensa, aislando las direcciones IP atacantes (IoCs) para que puedan ser procesadas por motores de inteligencia automatizados (como el Lab 2 - Veredict CTI Lite).
