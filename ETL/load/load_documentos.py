# load_documentos.py
# Fecha de creación: 2025-07-11 18:55:49
# Script auto-generado como parte del pipeline ETL completo.
# Depende de: ETL/etl_utils.py, soap_client.py o db.models.py según fase

import logging
from ETL.etl_utils import leer_json_local
from db.session import SessionLocal
from db.models import Documento

SCRIPT_NAME = "load_documentos"
logging.basicConfig(level=logging.INFO, format="%(asctime)s - " + SCRIPT_NAME + " - %(message)s")

def main():
    session = SessionLocal()
    data = leer_json_local("documentos_transformado.json")
    logging.info("Cargando documentos...")
    for item in data:
        session.add(Documento(**item))  # adaptación al modelo real
    session.commit()
    session.close()
    logging.info("Carga finalizada")

if __name__ == "__main__":
    main()
