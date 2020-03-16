from enum import Enum
from typing import List, Optional

from fastapi import FastAPI
from pydantic.main import BaseModel
from starlette.responses import RedirectResponse
from .search_db import get_results
from .search_es import get_es_results

app = FastAPI(
    title="AIN API",
    description="This is an AIN data search API",
    version="0.1.0",
)


class SearchOut(BaseModel):
    patentes: List[Optional[dict]]
    programas: List[Optional[dict]]
    cultivar: List[Optional[dict]]
    equipamentos: List[Optional[dict]]
    laboratorios: List[Optional[dict]]
    marcas: List[Optional[dict]]
    empresas: List[Optional[dict]]
    empresas_juniores: List[Optional[dict]]
    documentos: List[Optional[dict]]


class SearchType(str, Enum):
    all = 'all'
    patentes = "patentes"
    programas = "programas"
    cultivar = "cultivar"
    equipamentos = "equipamentos"
    laboratorios = "laboratorios"
    marcas = "marcas"
    empresas = "empresas"
    empresas_juniores = "empresas_juniores"
    documentos = "documentos"
    map = 'map'


@app.get("/", tags=['documentation'])
async def index():
    response = RedirectResponse(url="/docs")
    return response


@app.get("/search/{search_type}", response_model=SearchOut, tags=['search'], summary="Search endpoint")
def search(search_type: SearchType = 'all', q: str = None):
    """
    Search for a term in the AIN data repository

    - **search_type**: each item must have a name
    - **q**: term to search for
    """
    if search_type == SearchType.all:
        if q:
            results = get_results(q)
            results['lattesuser'] = get_es_results(q)
            return results
        return {
            "error": "Please specify a search term",
        }
