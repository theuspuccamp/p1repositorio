import network
from machine import Pin, PWM
from micropyserver import MicroPyServer
# Configuração dos pinos do motor direito
motor_direito_pino1 = Pin(2, Pin.OUT)
motor_direito_pino2 = Pin(15, Pin.OUT)
motor_direito_pwm = PWM(Pin(16), freq=1000)
# Configuração da rede Wi-Fi
ssid = 'PUC-ACD'
password = ''

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while not station.isconnected():
    pass

print('Conectado à rede', ssid)
print('Configuração de rede:', station.ifconfig())

# Funções para controlar os motores
def motor_direito(sentido, velocidade):
    if sentido == 'horario':
        motor_direito_pino1.on()
        motor_direito_pino2.off()
        
    elif sentido == 'frente':
        motor_direito_pino1.on()
        motor_direito_pino2.on()
        
    elif sentido == 'anti-horario':
        motor_direito_pino1.off()
        motor_direito_pino2.on()
        
    else:
        motor_direito_pino1.off()
        motor_direito_pino2.off()
        
    motor_direito_pwm.duty(velocidade)

# Página HTML para controle
html = """<!DOCTYPE html><html><head>
<title>Controle do Carrinho</title></head>
<body><h1>Controles do Carrinho </h1></body></html>
"""

def index(request):
    app.send(html)

def direita(request):
    print('horario')
    motor_direito('horario', 950)
    resp = """<html><head><title>Controle do Carrinho</title></head><body>
                  <h1>Direita</h1></body></html>"""
    app.send(resp)

def esquerda(request):
    print('Esquerda')
    motor_direito('anti-horario', 950)
    resp = """<html><head><title>Controle do Carrinho</title></head><body>
                  <h1>Esquerda</h1></body></html>"""
    app.send(resp)
    
def parar(request):
    print('parar')
    motor_direito('parar', 0)
    resp = """<html><head><title>Controle do Carrinho</title></head><body>
                  <h1>Parar</h1></body></html>"""  
    app.send(resp)
    
def andar(request):
    print('Frente')
    motor_direito('frente',950)
    resp = """<html><head><title>Controle do Carrinho</title></head><body>
                  <h1>Frente</h1></body></html>"""
    app.send(resp)
    
def reverso(request):
    print('Reverso')
    motor_direito('reverso', 950)
    resp = """<html><head><title>Controle do Carrinho</title></head><body>
                  <h1>Reverso</h1></body></html>"""
    app.send(resp)
          
app = MicroPyServer()
app.add_route("/", index)
app.add_route("/dir", direita)
app.add_route("/parar", parar)
app.add_route("/andar", andar)
app.add_route("/esquerda", esquerda)
app.add_route("/reverso", reverso)

app.start()

    