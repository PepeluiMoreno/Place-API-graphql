# place_api_graphql: ETL + GraphQL API para Contratación Pública del Estado

**Fecha de creación:** 2025-07-11 18:38:50  
**Autor:** Generado automáticamente vía especificaciones de usuario

---

## 🚀 Descripción

Este proyecto implementa un pipeline ETL completo y una API GraphQL para explotar los datos ofrecidos por el servicio web [https://contrataciondelestado.es](https://contrataciondelestado.es). Incluye:

- Extracción vía sindicación (Atoms Feeds)
- Transformación y almacenamiento intermedio en JSON
- Carga a base de datos PostgreSQL (hospedada en [Neon](https://neon.tech))
- Exposición vía API GraphQL con filtros básicos
- Despliegue automatizado vía GitHub Actions
- Dockerización completa del entorno

---

## 🗂 Estructura del Proyecto

```
place_api_graphql/
├── ETL/
│   ├── extract/
│   ├── transform/
│   ├── load/
│   ├── etl_utils.py
│   └── __init__.py
├── db/
│   ├── models.py
│   ├── session.py
│   └── __init__.py
├── graphql/
│   ├── graphql_server.py
│   ├── resolvers.py
│   ├── schema.py
│   └── __init__.py
├── tests/
├── .env
├── .env.example
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .github/
    └── workflows/
        └── deploy.yml
```

---

## ⚙️ Variables de Entorno

Usa el archivo `.env.example` como plantilla para generar el `.env`. Variables necesarias:

- `DATABASE_URL`: URL de conexión a PostgreSQL (Neon recomendado)

> ⚠️ El script `provision_neon.py` puede generar automáticamente tu base de datos en Neon y escribir esta URL en el `.env`.

---

## 🔧 Uso

### Extraer, transformar y cargar:

```bash
python ETL/extract/extract_organos.py
python ETL/extract/extract_expedientes.py
python ETL/transform/transform_expedientes.py
python ETL/load/load_all.py
```

### Levantar la API localmente:

```bash
docker-compose up --build
```

> Accede a `http://localhost:8000/graphql`

---

## 🧪 Consultas disponibles (GraphQL)

- `expedientes(organo_id, anio)`
- `adjudicatarios(nombre_contains, nif)`
- `organos(nombre_contains)`
- `documentos(expediente_id)`
- `pliegos(expediente_id)`
- `lotes(expediente_id)`

---

## 📦 Despliegue automático

El workflow GitHub Actions (`deploy.yml`) construye y publica la imagen Docker en GitHub Container Registry al hacer `push` en `main`.

---

## 🛠 Notas Técnicas

- Todos los scripts tienen cabecera con metadatos: nombre, fecha y dependencias.
- Logging uniforme con `SCRIPT_NAME` y timestamp en todos los scripts.
- Preparado para modo debug (JSON intermedios), pero se puede desactivar en producción.


