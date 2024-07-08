# src/data/inegi_data_collection.py

import requests
import os
from pathlib import Path

def download_inegi_data(url, output_path):
    response = requests.get(url)
    if response.status_code == 200:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'wb') as f:
            f.write(response.content)
        print(f"Descarga exitosa: {output_path}")
    else:
        print(f"Error en la descarga: {response.status_code}")

def main():
    base_path = Path("data/raw/inegi")
    
    # Definir las URLs y rutas de salida para cada conjunto de datos
    datasets = {
        "mde": ("https://www.inegi.org.mx/app/geo2/elevacionesmex/", "mde_15m.tif"),
        "uso_suelo": ("https://www.inegi.org.mx/app/biblioteca/ficha.html?upc=889463776079", "uso_suelo.shp"),
        "hidrografia": ("https://www.inegi.org.mx/app/biblioteca/ficha.html?upc=889463776086", "hidrografia.shp"),
        "infraestructura": ("https://www.inegi.org.mx/app/biblioteca/ficha.html?upc=889463776093", "infraestructura.shp"),
        "limites": ("https://www.inegi.org.mx/app/biblioteca/ficha.html?upc=889463776109", "limites_administrativos.shp"),
    }
    
    for name, (url, filename) in datasets.items():
        output_path = base_path / name / filename
        download_inegi_data(url, str(output_path))

if __name__ == "__main__":
    main()