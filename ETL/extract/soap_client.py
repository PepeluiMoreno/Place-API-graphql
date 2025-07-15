# SOAP_client.py
# 2025-07-12
# Cliente SOAP unificado para interactuar con los servicios WSDL de PLACE:
# Consulta, CODICE y Publicación
# Requiere: variables de entorno con las URLs de los WSDL reales

from zeep import Client
from zeep.transports import Transport
from os import getenv
from dotenv import load_dotenv
import logging

load_dotenv()

SCRIPT_NAME = "SOAP_client"

def log(msg):
    print(f"{SCRIPT_NAME} - {msg}")

try:
    consulta_wsdl = getenv("PLACE_CONSULTA_WSDL_URL")
    codice_wsdl = getenv("PLACE_CODICE_WSDL_URL")
    publicacion_wsdl = getenv("PLACE_PUBLICACION_WSDL_URL")

    if not all([consulta_wsdl, codice_wsdl, publicacion_wsdl]):
        raise ValueError("Faltan URLs WSDL en el .env")

    consulta_client = Client(wsdl=consulta_wsdl)
    codice_client = Client(wsdl=codice_wsdl)
    publicacion_client = Client(wsdl=publicacion_wsdl)

except Exception as e:
    log(f"Error al inicializar clientes SOAP: {e}")
    raise

# ===============================
# Métodos de CONSULTA
# ===============================

def get_buyer_profile_data(buyer_id: str):
    return consulta_client.service.getBuyerProfileData(buyerProfile={"nif": buyer_id})


def get_expedient_state_full(codexp: str):
    return consulta_client.service.getExpedientStateFull(expedientState={"codigoExpediente": codexp})


# ===============================
# Métodos de CODICE
# ===============================

def validate_codice(notice_xml: str):
    return codice_client.service.validateCODICE(notice={"xmlDocument": notice_xml})


def view_codice(document_id: str):
    return codice_client.service.viewCODICE(document={"documentId": document_id})


# ===============================
# Métodos de PUBLICACIÓN
# ===============================

def get_expedient_state(codexp: str):
    return publicacion_client.service.getExpedientState(parameters={"codigoExpediente": codexp})
