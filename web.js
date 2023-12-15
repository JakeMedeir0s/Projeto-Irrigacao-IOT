const mqttSubTopic = 'IOT/Regador';
let mqttTemperature = '';
let mqttHumidity = '';
let relayStatus = 'Desligado';

mqttClient.on('connect', () => {
  console.log('Connected to MQTT Broker');
  mqttClient.subscribe([mqttSubTopic], () => {
    console.log(`Subscribed to topic '${mqttSubTopic}`);
  });
});

mqttClient.on('message', (topic, payload) => {
  console.log('Received Message:', topic, payload.toString());
  const data = JSON.parse(payload.toString());
  mqttTemperature = data.temp; // Assuming temperature is sent as 'temp' in the MQTT payload
  mqttHumidity = data.humidity; // Assuming humidity is sent as 'humidity' in the MQTT payload
});

app.get('/', (req, res) => {
  res.send(`
    <!DOCTYPE html>
    <html>
      <body>
        <h1>MQTT Server</h1>
        <p>Temperature: ${mqttTemperature}  Celsius</p>
        <p>Humidity: ${mqttHumidity}%</p>
        <p>Relay Status: ${relayStatus}</p>
      </body>
    </html>
  `);
});

app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});