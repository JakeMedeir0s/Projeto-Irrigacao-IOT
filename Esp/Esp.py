from machine import Pin, ADC
import time
import dht

# Configuração do sensor de umidade de solo
PINO_SENSOR = 34  # Pino ADC para o sensor de umidade

# Configuração do módulo de relé
pin_rele = 33  # Pino para o controle do relé
rele = Pin(pin_rele, Pin.OUT)

# Configuração do sensor de temperatura DHT11
pin_dht = 27  # Pino do sensor DHT11
sensor = dht.DHT11(Pin(pin_dht))

# Definição do número de amostras
NUMERO_AMOSTRAS = 5

def ler_umidade_solo():
    pino_sensor = Pin(PINO_SENSOR, Pin.IN)
    adc = ADC(pino_sensor)
    adc.atten(ADC.ATTN_11DB)

    somatoria = 0

    for i in range(1, NUMERO_AMOSTRAS + 1):
        leitura_sensor = adc.read()
        somatoria += leitura_sensor
        tensao = leitura_sensor * (5 / 1023)
        print("Amostra {} | Leitura: {} | Tensao: {:.2f}".format(i, leitura_sensor, tensao))
        time.sleep_ms(1000)

    media = somatoria / NUMERO_AMOSTRAS
    return leitura_sensor

def acionar_rele():
    rele.value(1)  # Liga o relé
    print("Irrigação ligada")
    time.sleep(5)  # Tempo de irrigação por 5 segundos
    rele.value(0)  # Desliga o relé
    print("Irrigação desligada")

while True:
    umidade = ler_umidade_solo()
    print("Umidade do solo:", umidade)

    sensor.measure()  # Realiza a medição da temperatura e umidade
    temp = sensor.temperature()
    print('Temperatura: %3.1f C' % temp)

    if umidade > 500:  # Defina o limite de umidade desejado para acionar a irrigação
        acionar_rele()

    time.sleep(1)  # Aguarda 10 segundos antes de verificar novamente a umidade e temperatura