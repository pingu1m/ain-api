from pprint import pprint

import MySQLdb

dbconnect = MySQLdb.connect("127.0.0.1", "root", "password", "ain_php")

cursor = dbconnect.cursor(MySQLdb.cursors.DictCursor)

tabelas = ["patentes", "programas", "cultivar", "equipamentos", "laboratorios", "marcas", "empresas",
           "empresas_juniores", "documentos"]
tabelas_map = ["laboratorios", "instituicoes", "empresas", "empresas_juniores"]


def get_results(q: str = None):
    resultset = {}
    for tabela in tabelas:
        query = "SHOW COLUMNS FROM " + tabela
        try:
            cursor.execute(query)
            records = cursor.fetchall()
            print(str(len(records)) + " Records found")
            query_likes = []
            for row in records:
                query_likes.append(row['Field'] + f" LIKE '%{q}%'")
        except Exception as error:
            print("Encountered error while retrieving data from database", error)

        final_query = 'SELECT * FROM ' + tabela + ' WHERE ' + " OR ".join(query_likes)
        print(final_query)

        try:
            cursor.execute(final_query)
            resultset[tabela] = list(cursor.fetchall())

        except:
            print("Encountered error while retrieving data from database")
    dbconnect.close()
    return resultset


def get_results_by_type(search_type: str = 'all', q: str = None):
    resultset = []
    new_tabelas = [tabela for tabela in tabelas if tabela == search_type]
    for tabela in new_tabelas:
        query = "SHOW COLUMNS FROM " + tabela
        try:
            cursor.execute(query)
            columns = cursor.fetchall()
            query_likes = []
            for column in columns:
                query_likes.append(column + f" LIKE '%{q}%'")
            final_query = 'SELECT * FROM ' + tabela + ' WHERE ' + " OR ".join(query_likes)
            cursor.execute(final_query)
            resultset.append(cursor.fetchall())
            return resultset
        except:
            print("Encountered error while retrieving data from database")
        finally:
            dbconnect.close()


def get_map_results():
    resultset = []
    for tabela in tabelas_map:
        query = f"SELECT id, sigla, nome, logotipo, latitude, longitude FROM {tabela} WHERE latitude is not NULL and longitude is not null and latitude <> 0 and longitude <> 0"
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            for result in results:
                resultset.append(result)
        except:
            print("Encountered error while retrieving data from database")
        finally:
            dbconnect.close()


# results = get_results('vidro')
# pprint(results)
