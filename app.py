from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = "API_KEY"
BASE_URL = 'http://api.openweathermap.org/data/2.5/'

# Endpoint to get current weather
@app.route('/current', methods=['GET'])
def current_weather():
    city_name = request.args.get('city')
    if not city_name:
        return jsonify({'error': 'City parameter is required'}), 400

    url = f"{BASE_URL}weather?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({'error': 'Unable to fetch weather data'}), response.status_code

    return jsonify(response.json())

# Endpoint to get weather forecast
@app.route('/forecast', methods=['GET'])
def forecast_weather():
    city_name = request.args.get('city')
    if not city_name:
        return jsonify({'error': 'City parameter is required'}), 400

    url = f"{BASE_URL}forecast?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({'error': 'Unable to fetch forecast data'}), response.status_code

    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


