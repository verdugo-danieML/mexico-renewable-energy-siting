import requests
import os

def download_inegi_data(url, output_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(response.content)
        print(f"Descarga exitosa: {output_path}")
    else:
        print(f"Error en la descarga: {response.status_code}")

# Ejemplo de uso (lo completaremos más adelante)
if __name__ == "__main__":
    # URL de ejemplo (necesitaremos la URL correcta de INEGI)
    dem_url = "https://www.inegi.org.mx/app/descarga/dem/example.tif"
    output_file = "data/raw/dem_example.tif"
    download_inegi_data(dem_url, output_file)