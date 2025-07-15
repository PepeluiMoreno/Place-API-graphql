# load_adjudicatarios.py
# Fecha de creación: 2025-07-11 18:55:49
# Script auto-generado como parte del pipeline ETL completo.
# Depende de: ETL/etl_utils.py, soap_client.py o db.models.py según fase

import logging
from ETL.etl_utils import leer_json_local
from db.session import SessionLocal
from db.models import Adjudicatario

SCRIPT_NAME = "load_adjudicatarios"
logging.basicConfig(level=logging.INFO, format="%(asctime)s - " + SCRIPT_NAME + " - %(message)s")

def main():
    session = SessionLocal()
    data = leer_json_local("adjudicatarios_transformado.json")
    logging.info("Cargando adjudicatarios...")
    for item in data:
        session.add(Adjudicatario(**item))  # adaptación al modelo real
    session.commit()
    session.close()
    logging.info("Carga finalizada")

if __name__ == "__main__":
    main()
