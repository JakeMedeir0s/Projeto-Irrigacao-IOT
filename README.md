# Projeto-Sistema-de-Irrigacao-IOT

## Introdução

* Componentes: Josefa Jakelyne, Ludimila Kelly, Luiz Felipe e Luiz Henrique 
* Nossa motivação: Tivemos como motivação automatizar o processo de irrigação para economizar tempo e não ser necessário fazer a irrigação manualmente. Além disso, pensamos na sustentabilidade ambiental, pois otimizando o uso da água, o projeto pode ser uma pequena contribuição para um ambiente mais equilibrado.
* Nosso objetivo primordial é criar um sistema de irrigação automatizado capaz de monitorar as condições ambientais, como umidade do solo e temperatura. Além disso, o projeto visa proporcionar controle remoto por meio de uma aplicação móvel ou interface web, permitindo que os usuários ajustem as configurações e recebam notificações relevantes.

* Os conceitos mais utilizados no projeto foram:
  * MQTT que funciona no modelo de publicação/assinatura, permitindo a comunicação assíncrona entre dispositivos. No projeto ele foi usado para enviar dados de umidade do solo, temperatura, e status de irrigação para uma central de controle remoto.
  * O hardware principal no projeto é o ESP32, um microcontrolador que combina Wi-Fi e Bluetooth. Ele é usado para ler os sensores, controlar o relé e se comunicar com outros dispositivos por meio do protocolo MQTT.
  * Mesmo não estando completo, foi utilizado conceitos de Node.js no desenvolvimento web. Com Node.js, podemos criar uma interface web que se conecta ao MQTT broker para exibir informações em tempo real sobre a umidade do solo, temperatura e estado da irrigação.
  * Foi utilizado MicroPython que é uma implementação do Python projetada para usar a linguagem Python para programar microcontroladores como o ESP32.

## Componentes

* Para realizar o sistema de irrigação. Usamos:
  - Esp 32;
  - Sensor de umidade do solo;
  - Sensor DHT11
  - Cano de pvc
  - Uma muda de maracujazeiro;
  - Uma garrafa pet de 500ml;
  - Válvula solenóide de vazão;
  - Jumpers;

## Metodologia / Solução Proposta  

* Usamos o micropython para programar no esp32. A lógica usada neste código foi, principalmente, na leitura do sensor de umidade do solo. Quando a umidade do solo está baixa o eps32 manda o relé ativar, assim abrindo a válvula solenóide de vazão. O DHT11 foi usado para coletar os dados do ambiente da planta, como temperatura e umidade.
* Os programas usados neste projeto foram o Thonny para micropython, Replit para o nodeJs, Wokwi para testar os código enquanto não tínhamos o eps em mãos. 
* A montagem do projeto se deu em conectar os sensores ao esp32, também tendo um cano de pvc conectado a válvula e uma garrafa de 500ml conectada ao cano. 

* Abaixo encontra-se a imagem do circuito pronto do sistema de irrigação com o esp32

<div align="center">
    <img src="circuito-completo.jpg"  width="275" height="200"/>
    <>
    <img src="ampliado_esp"  width="275" height="200"/>
    <>
    <img src="ampliado_sensor.jpg"  width="275" height="200"/>
</div>

* Abaixo encontra-se o prototipo finalizado

<div align="center">
    <img src="prototipo.jpg"  width="275" height="200"/>
</div>

## Ligações

* A tabela abaixo ilustra o uso dos pinos do sensor de temperatura e umidade do ar:

| Sensor DHT11    | ESP32 |
| --------------- | ----- | 
| -               | GND   | 
|  +              | 3.3v  | 
| S               | D27   | 

* A tabela abaixo ilustra o uso dos pinos do sensor de umidade do solo:

| Sensor de Umidade do Solo | ESP32 |
| ------------------------- | ----- |
| G                         | GND   |
| V+                        | 3.3v  |
| S                         | D34   |

## Códigos 

* Este foi o código utilizado para função do sensor de umidade do solo, onde é realizado a leitura do sensor, é feito 5 amostras de leitura e no final a função retorna a última leitura.

```python
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
```

* Este código é o da função de ligar e desligar o relé

```python
def acionar_rele():
    rele.value(1)  # Liga o relé
    print("Irrigação ligada")
    time.sleep(5)  # Tempo de irrigação por 5 segundos
    rele.value(0)  # Desliga o relé
    print("Irrigação desligada")
```

* Este é o código que serve como "coração" do programa, pois é onde tem as condições para ligar e desligar o relé, assim como a medição do sensor de temperatura

```python
while True:
    umidade = ler_umidade_solo()
    print("Umidade do solo:", umidade)

    sensor.measure()  # Realiza a medição da temperatura e umidade
    temp = sensor.temperature()
    print('Temperatura: %3.1f C' % temp)

    if umidade > 500:  # Defina o limite de umidade desejado para acionar a irrigação
        acionar_rele()

    time.sleep(1) 
```

## Experimentos 

* Apresentar os experimentos ou testes executados. 
* Explicar os resultados. 

* Foram realizados testes para o código do sistema de irrigação e abaixo pode-se encontrar a imagem dos resultados obtidos: 

  <div align="center">
    <img src="resultado1.jpg"  width="275" height="200"/>
  </div>

  - A imagem acima mostra o resultado do teste do código do sistema de irrigação, podemos ver as leituras quando o sensor estava fora do solo e quando foi adicionado ao solo.

  <div align="center">
    <img src="resultado2.jpg"  width="275" height="200"/>
  </div>

  - A imagem acima mostra o resultado de outro teste do código do sistema de irrigação, podemos ver as leituras quando o sensor estava dentro do solo e quando foi retirado ao solo.

* Também foi realizado experimento utilizando a plataforma wokwi e apenas a lógica do sistema de irrigação com o sensor de temperatura DHT22.

  <div align="center">
    <img src="resultado3.jpg"  width="275" height="200"/>
  </div>

  - Pode-se observar o circuito do esp32 com o sensor DHT22 e um led que liga quando a irrigação está ligada.

## Links dos códigos testes para web

* https://wokwi.com/projects/322577683855704658
* https://replit.com/@luiz-felipef116/serverdominepirata#index.js

## Referências

* https://github.com/Natalnet/lib_ura_esp/tree/master/ESP32/SoilMoistureSensor
* https://github.com/Natalnet/lib_ura_esp/tree/master/ESP32/Blink
* https://github.com/Natalnet/lib_ura_esp/tree/master/ESP32/DHT11 
* https://github.com/orivaldosantana/mini_central_iot
