# load_all.py
# Fecha de creación: 2025-07-11 18:55:49
# Script auto-generado como parte del pipeline ETL completo.
# Depende de: ETL/etl_utils.py, soap_client.py o db.models.py según fase

import logging
from ETL.load import (
    load_organos, load_expedientes, load_adjudicatarios,
    load_pliegos, load_documentos, load_lotes, load_anuncios
)

SCRIPT_NAME = "load_all"
logging.basicConfig(level=logging.INFO, format="%(asctime)s - " + SCRIPT_NAME + " - %(message)s")

def main():
    load_organos.main()
    load_expedientes.main()
    load_adjudicatarios.main()
    load_pliegos.main()
    load_documentos.main()
    load_lotes.main()
    load_anuncios.main()

if __name__ == "__main__":
    main()
