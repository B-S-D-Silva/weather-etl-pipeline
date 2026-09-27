import requests
import json
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

api_key = '2b3381ec70684c932c36f6f541e091a8'


def extract_weather_data(city: str, api_key: str) -> list:
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'units': 'metric', 'appid': api_key}

    response = requests.get(url, params=params)

    if response.status_code != 200:
        logging.error(f"Erro na requisição: {response.status_code}")
        return []

    data = response.json()

    if not data:
        logging.warning("Nenhum dado retornado")
        return []

    output_path = 'data/weather_data.json'
    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w') as f:
        json.dump(data, f, indent=4)

    logging.info(f"Arquivo salvo em {output_path}")

    return data

