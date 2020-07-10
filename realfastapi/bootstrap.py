from dynaconf import settings
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from realfastapi.db.mongodb_utils import dbConnect, dbDisconnect
from realfastapi.routes.routes import api_router

app_description = """Servicio de datos REST-API de la AAPS.\n
Ofrece puntos de acceso a los conjuntos de datos de la AAPS. Los conjuntos de datos actualmente integrados al servicio de datos son:\n
* **Register**: Datos de EPSAs registradas.
* **Music**: Datos de EPSAs registradas.
"""

app = FastAPI(
    debug=True,  # settings.DEBUG,
    title="RealFastAPI",
    description=app_description,
    version="0.1.0",
    openapi_url="/openapi.json",
    docs_url="/openapi",
    redoc_url="/redoc",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler("startup", dbConnect)
app.add_event_handler("shutdown", dbDisconnect)

# routes
app.include_router(api_router, prefix=str(settings.API_V1_STR))
