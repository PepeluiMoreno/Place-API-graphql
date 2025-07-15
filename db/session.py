# app/db/session.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Si usas python-dotenv, descomenta estas dos líneas:
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("La variable de entorno DATABASE_URL no está definida")

# create_engine parsea los parámetros de la cadena (incluyendo sslmode, channel_binding…)
engine = create_engine(
    DATABASE_URL,
    echo=(os.getenv("ENVIRONMENT") == "development"),  # para ver SQL en dev
    pool_pre_ping=True,
)

# cada vez que quieras una sesión:
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
