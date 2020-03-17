tabelas = ["patentes", "programas", "cultivar", "equipamentos", "laboratorios", "marcas", "empresas",
           "empresas_juniores", "documentos"]
tabelas_map = ["laboratorios", "instituicoes", "empresas", "empresas_juniores"]


def get_results(db, q: str = None):
    resultset = {}
    for tabela in tabelas:
        query = "SHOW COLUMNS FROM " + tabela
        records = db.execute(query)
        query_likes = []
        for row in records:
            query_likes.append( dict(row)['Field'] + f" LIKE '%{q}%'")
        final_query = 'SELECT * FROM ' + tabela + ' WHERE ' + " OR ".join(query_likes)
        results = db.execute(final_query)
        resultset[tabela] = [ dict(result) for result in results]

    return resultset

def get_results_by_type(db, search_type: str = 'all', q: str = None):
    resultset = {}
    new_tabelas = [tabela for tabela in tabelas if tabela == search_type]
    for tabela in new_tabelas:
        query = "SHOW COLUMNS FROM " + tabela
        columns = db.execute(query)
        query_likes = []
        for column in columns:
            query_likes.append(dict(column)['Field'] + f" LIKE '%{q}%'")
        final_query = 'SELECT * FROM ' + tabela + ' WHERE ' + " OR ".join(query_likes)
        results = db.execute(final_query)
        resultset[tabela] = [dict(result) for result in results]
    return resultset

def get_map_results(db):
    resultset = []
    for tabela in tabelas_map:
        query = f"SELECT id, sigla, nome, logotipo, latitude, longitude FROM {tabela} WHERE latitude is not NULL and longitude is not null and latitude <> 0 and longitude <> 0"
        results = db.execute(query)
        for result in results:
            resultset.append(dict(result))

