# test_place_wsdl.py
# Fecha de creación: 2025-07-11 19:45:00
# Prueba básica del endpoint WSDL de preproducción de PLACE con zeep
# No requiere autenticación para métodos públicos como consultarListaÓrganosContratación

import logging
from zeep import Client
from zeep.exceptions import Fault

SCRIPT_NAME = "test_place_wsdl"
logging.basicConfig(level=logging.INFO, format="%(asctime)s - " + SCRIPT_NAME + " - %(message)s")

WSDL_URL = "https://publicacion.preprod-contrataciondelestado.es/ServiciosPLACEB2B?wsdl"

def main():
    logging.info("Cargando cliente SOAP desde WSDL...")
    client = Client(WSDL_URL)

    logging.info("Invocando consultarListaÓrganosContratación()...")
    try:
        result = client.service.consultarListaÓrganosContratación()
        logging.info(f"Resultado recibido: {type(result)}")
        print(result)
    except Fault as e:
        logging.error(f"SOAP Fault: {e}")

if __name__ == "__main__":
    main()
