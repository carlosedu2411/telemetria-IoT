from flask import render_template
import json
from datetime import datetime, timezone
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import paho.mqtt.client as mqtt

# config flask e sqlalchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///telemetria.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# models db
class LeiturasIoT(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(50), nullable=False)
    temperatura = db.Column(db.Float, nullable=False)
    umidade = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default="NORMAL")
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def to_dict(self):
        return {
            "id": self.id,
            "device_id": self.device_id,
            "temperatura": self.temperatura,
            "cpu_uso": self.temperatura,
            "ram_uso": self.umidade,
            "umidade": self.umidade,
            "status": self.status,
            "timestamp": self.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        }

# config MQTT
MQTT_BROKER = "test.mosquitto.org"  
MQTT_PORT = 1883
MQTT_TOPIC = "/telemetria/sensores"

def on_connect(client, _userdata, _flags, rc, _properties=None):
    print(f"[MQTT] Conectado ao Broker com código de resultado: {rc}")
    client.subscribe(MQTT_TOPIC)
    print(f"[MQTT] Inscrito no tópico: {MQTT_TOPIC}")

def on_message(_client, _userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        print(f"[MQTT] Mensagem recebida: {payload}")
        
        cpu_uso = payload.get("cpu_uso", payload.get("temperatura", 0))
        ram_uso = payload.get("ram_uso", payload.get("umidade", 0))
        if cpu_uso > 85.0 or ram_uso > 90.0:
            status = "CRITICAL"
        elif cpu_uso > 70.0 or ram_uso > 75.0:
            status = "WARNING"
        else:
            status = "NORMAL"

        # salvar informações no sqlite
        with app.app_context():
            nova_leitura = LeiturasIoT(
                device_id=payload.get("device_id", "DESCONHECIDO"),
                temperatura=cpu_uso,
                umidade=ram_uso,
                status=status
            )
            db.session.add(nova_leitura)
            db.session.commit()
            print("[BD] Leitura registrada com sucesso!")

    except Exception as e:
        print(f"[ERRO] Falha ao processar mensagem MQTT: {e}")

# inicia o cliente MQTT
mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
mqtt_client.loop_start()  # executa o loop do MQTT em background

# rotas da API
@app.route('/api/telemetria', methods=['GET'])
def listar_leituras():
    leituras = LeiturasIoT.query.order_by(LeiturasIoT.id.desc()).limit(20).all()
    return jsonify([l.to_dict() for l in leituras]), 200

@app.route('/api/telemetria/<string:device_id>', methods=['GET'])
def leituras_por_dispositivo(device_id):
    leituras = LeiturasIoT.query.filter_by(device_id=device_id).order_by(LeiturasIoT.id.desc()).all()
    return jsonify([l.to_dict() for l in leituras]), 200

@app.route('/api/telemetria', methods=['DELETE'])
def limpar_leituras():
    LeiturasIoT.query.delete()
    db.session.commit()
    return jsonify({"message": "Leituras removidas com sucesso"}), 200

# cria as tabelas antes de iniciar o html
with app.app_context():
    db.create_all()
@app.route('/')
def dashboard():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True, port=5000)