import time
import json
import psutil
import paho.mqtt.client as mqtt

MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_TOPIC = "/telemetria/sensores"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(MQTT_BROKER, MQTT_PORT, 60)

DEVICE_ID = "SERVIDOR-001"  # Identificador único do dispositivo real
EXEMPLO_DEVICE_ID = "SERVIDOR-002"
EXEMPLO_DEVICE_ID_1 = "SERVIDOR-003"
print(f"Iniciando envio de telemetria REAL do dispositivo {DEVICE_ID}...")

try:
    ciclo = 0
    while True:
        cpu_uso = psutil.cpu_percent(interval=1)
        ram_uso = psutil.virtual_memory().percent

        payload = {
            "device_id": DEVICE_ID,
            "cpu_uso": cpu_uso,
            "ram_uso": ram_uso
        }

        client.publish(MQTT_TOPIC, json.dumps(payload))
        print(f"[REAL] CPU: {cpu_uso}% | RAM: {ram_uso}%")

        # Exemplo visual: alterna entre alerta amarelo e critico.
        exemplo_critico = ciclo % 2 == 1
        exemplo_payload = {
            "device_id": EXEMPLO_DEVICE_ID,
            "cpu_uso": 92 if exemplo_critico else 80,
            "ram_uso": 94 if exemplo_critico else 90
        }
        client.publish(MQTT_TOPIC, json.dumps(exemplo_payload))
        print(f"[EXEMPLO] CPU: {exemplo_payload['cpu_uso']}% | RAM: {exemplo_payload['ram_uso']}%")
        ciclo += 1
        
        time.sleep(18)  # Envia a cada 18 segundos para não sobrecarregar o broker

except KeyboardInterrupt:
    print("\nColeta interrompida.")
    client.disconnect()