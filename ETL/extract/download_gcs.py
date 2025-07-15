# download_gcs.py
# 2025-07-12 22:15
# Descarga catálogos .gc oficiales usados por CODICE desde el portal PLACE y los guarda en ETL/catalogos/gc_files/
# Requiere: requests, pathlib, logging

import requests
from pathlib import Path
import logging

SCRIPT_NAME = "download_gcs"
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(message)s")

GC_URLS = {
    "ContractCode": "https://contrataciondelestado.es/codice/cl/2.08/ContractCode-2.08.gc",
    "WorksContractCode": "https://contrataciondelestado.es/codice/cl/1.04/WorksContractCode-1.04.gc",
    # Los siguientes son conjeturales: se añadirán solo si existen
    "ServiceContractCode": "https://contrataciondelestado.es/codice/cl/1.04/ServiceContractCode-1.04.gc",
    "SupplyContractCode": "https://contrataciondelestado.es/codice/cl/1.04/SupplyContractCode-1.04.gc",
    "ProcedureCode": "https://contrataciondelestado.es/codice/cl/1.04/ProcedureCode-1.04.gc",
    "UrgencyCode": "https://contrataciondelestado.es/codice/cl/1.04/UrgencyCode-1.04.gc",
    "UnitCode": "https://contrataciondelestado.es/codice/cl/1.04/UnitCode-1.04.gc",
    "FundingTypeCode": "https://contrataciondelestado.es/codice/cl/1.04/FundingTypeCode-1.04.gc",
    "EconomicOperatorRoleCode": "https://contrataciondelestado.es/codice/cl/1.04/EconomicOperatorRoleCode-1.04.gc",
    "AwardCriterionTypeCode": "https://contrataciondelestado.es/codice/cl/1.04/AwardCriterionTypeCode-1.04.gc",
    "AwardStatusCode": "https://contrataciondelestado.es/codice/cl/1.04/AwardStatusCode-1.04.gc",
    "NoticeTypeCode": "https://contrataciondelestado.es/codice/cl/1.04/NoticeTypeCode-1.04.gc",
    "DocumentTypeCode": "https://contrataciondelestado.es/codice/cl/1.04/DocumentTypeCode-1.04.gc",
    "ProcedureLegalBasisCode": "https://contrataciondelestado.es/codice/cl/1.04/ProcedureLegalBasisCode-1.04.gc",
    "ContractNatureCode": "https://contrataciondelestado.es/codice/cl/1.04/ContractNatureCode-1.04.gc",
}

def download_file(name, url, dest_dir):
    try:
        response = requests.get(url, timeout=10)
        if response.ok and response.text.strip().startswith("<?xml"):
            path = dest_dir / f"{name}.gc"
            path.write_text(response.text, encoding="utf-8")
            logging.info(f"Descargado: {name}")
        else:
            logging.warning(f"No se pudo descargar {name} desde {url}")
    except Exception as e:
        logging.error(f"Error descargando {name}: {e}")

def main():
    dest_dir = Path("ETL/catalogos/gc_files")
    dest_dir.mkdir(parents=True, exist_ok=True)
    for name, url in GC_URLS.items():
        download_file(name, url, dest_dir)

if __name__ == "__main__":
    main()
