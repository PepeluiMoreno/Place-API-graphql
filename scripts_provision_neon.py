# provision_neon.py
# Fecha de creación: 2025-07-11 08:22:52
# Crea un proyecto y base de datos PostgreSQL en Neon vía API REST y guarda la DB_URL en un archivo .env.
# Depende de: variables NEON_API_KEY, NEON_PROJECT_NAME. Requiere: requests.

import os
import sys
import logging
import requests

SCRIPT_NAME = "provision_neon.py"
logging.basicConfig(level=logging.INFO, format="%(asctime)s - " + SCRIPT_NAME + " - %(message)s")
logger = logging.getLogger(__name__)

API_BASE = "https://console.neon.tech/api/v2"

def write_env_var(key, value):
    env_path = Path(".env")
    lines = []
    if env_path.exists():
        lines = env_path.read_text(encoding="utf-8").splitlines()
        lines = [l for l in lines if not l.startswith(f"{key}=")]
    lines.append(f"{key}={value}")
    env_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    logger.info(f"Variable {key} escrita en .env")

def main():
    api_key = os.getenv("NEON_API_KEY")
    project_name = os.getenv("NEON_PROJECT_NAME")

    if not api_key or not project_name:
        logger.error("Faltan variables requeridas: NEON_API_KEY o NEON_PROJECT_NAME")
        sys.exit(1)

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # 1. Crear proyecto
    logger.info("Creando proyecto en Neon...")
    resp = requests.post(f"{API_BASE}/projects", json={"name": project_name}, headers=headers)
    if resp.status_code not in (200, 201):
        logger.error(f"Error creando proyecto: {resp.text}")
        sys.exit(1)
    project_id = resp.json().get("id")
    logger.info(f"Proyecto creado con ID: {project_id}")

    # 2. Obtener información del proyecto para URL de conexión
    logger.info("Recuperando URL de conexión...")
    resp = requests.get(f"{API_BASE}/projects/{project_id}", headers=headers)
    if resp.status_code != 200:
        logger.error(f"Error obteniendo info de proyecto: {resp.text}")
        sys.exit(1)
    db_url = resp.json().get("connection_uri") or resp.json().get("connectionString")
    if not db_url:
        logger.error("No se encontró DB_URL en la respuesta")
        sys.exit(1)

    write_env_var("DB_URL", db_url)
    logger.info("Provisioning completado correctamente.")

if __name__ == "__main__":
    main()
