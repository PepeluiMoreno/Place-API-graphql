# test_place_expedientes_colab.py
# Fecha de creación: 2025-07-11
# Invoca el método consultarExpedientes() del WSDL público de PLACE en preproducción

!pip install zeep --quiet

import logging
from zeep import Client
from zeep.exceptions import Fault

SCRIPT_NAME = "colab_place_expedientes"
logging.basicConfig(level=logging.INFO, format="%(asctime)s - " + SCRIPT_NAME + " - %(message)s")

WSDL_URL = "https://publicacion.preprod-contrataciondelestado.es/ServiciosPLACEB2B?wsdl"
client = Client(WSDL_URL)

try:
    logging.info("Invocando consultarExpedientes()...")
    result = client.service.consultarExpedientes()
    print("✅ Expedientes recibidos:")
    for i, exp in enumerate(result[:3]):
        print(f"\nExpediente #{i+1}:\n{exp}")
except Fault as e:
    logging.error(f"SOAP Fault: {e}")
except Exception as e:
    logging.error(f"Error inesperado: {e}")
