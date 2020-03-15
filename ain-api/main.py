from enum import Enum

from fastapi import FastAPI
from starlette.responses import RedirectResponse


app = FastAPI()

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


@app.get("/")
async def index():
    response = RedirectResponse(url="/docs")
    return response

@app.get("/search/{search_type}")
def search(search_type: SearchType, q: str = None):
    if search_type == SearchType.alexnet:
        asdf = 'asdf'
    if q:
        return {
            "type": f"{search_type}",
            "term": f"{q}",
        }
    return {
        "type": f"{search_type}",
    }
