from src.conf.configDB import connectionDB
from src.schema import (actingModel, reviewModel)

# Des/Relacion Persona -> Actua -> Pelicula
def relacPAM(nodeA:actingModel, inputTitle, inputName):
    try:
        driver_neo4j = connectionDB()
        session = driver_neo4j.session()
        query="""
        MATCH (p:Person {name:$inpN})
        MATCH (m:Movie {title:$inpT})
        WHERE NOT (p)-[:ACTED_IN]->(m)
        CREATE (p)-[:ACTED_IN {roles:$ro}]->(m)
        """

        x = {"ro":nodeA.roles, "inpT":inputTitle, "inpN":inputName}
        result = session.run(query,x)
        summary = result.consume().counters
        cant = summary.relationships_created

        if (cant > 0):
            return {"response": "Relacion Creada"}
        else:
            return {"response": "Ingrese los nodos correctamente"}
    except Exception as ex:
        return ("Error:", ex)

def drelacPAM(inputTitle, inputName):
    try:
        driver_neo4j = connectionDB()
        session = driver_neo4j.session()
        query="""
        MATCH (p:Person {name:$inpN})-[r:ACTED_IN]->(m:Movie {title:$inpT})
        DELETE r
        """

        x = {"inpT":inputTitle, "inpN":inputName}
        result = session.run(query,x)
        summary = result.consume().counters
        cant = summary.relationships_deleted

        if (cant > 0):
            return {"response": "Relacion Eliminada"}
        else:
            return {"response": "Ingrese los nodos correctamente"}
    except Exception as ex:
        return ("Error:", ex)

# Des/Relacion Persona -> Reseña -> Pelicula
def relacPRM(nodeR:reviewModel, inputTitle, inputName):
    try:
        driver_neo4j = connectionDB()
        session = driver_neo4j.session()
        query="""
        MATCH (p:Person {name:$inpN})
        MATCH (m:Movie {title:$inpT})
        WHERE NOT (p)-[:REVIEWED]->(m)
        CREATE (p)-[:REVIEWED {summary:$su, rating:$ra}]->(m)
        """

        x = {"su":nodeR.summary, "ra":nodeR.rating, "inpT":inputTitle, "inpN":inputName}
        result = session.run(query,x)
        summary = result.consume().counters
        cant = summary.relationships_created

        if (cant > 0):
            return {"response": "Relacion Creada"}
        else:
            return {"response": "Ingrese los nodos correctamente"}
    except Exception as ex:
        return ("Error:", ex)

def drelacPRM(inputTitle, inputName):
    try:
        driver_neo4j = connectionDB()
        session = driver_neo4j.session()
        query="""
        MATCH (p:Person {name:$inpN})-[r:REVIEWED]->(m:Movie {title:$inpT})
        DELETE r
        """

        x = {"inpT":inputTitle, "inpN":inputName}
        result = session.run(query,x)
        summary = result.consume().counters
        cant = summary.relationships_deleted

        if (cant > 0):
            return {"response": "Relacion Eliminada"}
        else:
            return {"response": "Ingrese los nodos correctamente"}
    except Exception as ex:
        return ("Error:", ex)

# Des/Relacion Persona -> Dirige -> Pelicula
def relacPDM(inputTitle, inputName):
    try:
        driver_neo4j = connectionDB()
        session = driver_neo4j.session()
        query="""
        MATCH (p:Person {name:$inpN})
        MATCH (m:Movie {title:$inpT})
        WHERE NOT (p)-[:DIRECTED]->(m)
        CREATE (p)-[:DIRECTED]->(m)
        """

        x = {"inpT":inputTitle, "inpN":inputName}
        result = session.run(query,x)
        summary = result.consume().counters
        cant = summary.relationships_created

        if (cant > 0):
            return {"response": "Relacion Creada"}
        else:
            return {"response": "Ingrese los nodos correctamente"}
    except Exception as ex:
        return ("Error:", ex.message)

def drelacPDM(inputTitle, inputName):
    try:
        driver_neo4j = connectionDB()
        session = driver_neo4j.session()
        query="""
        MATCH (p:Person {name:$inpN})-[r:DIRECTED]->(m:Movie {title:$inpT})
        DELETE r
        """

        x = {"inpT":inputTitle, "inpN":inputName}
        result = session.run(query,x)
        summary = result.consume().counters
        cant = summary.relationships_deleted

        if (cant > 0):
            return {"response": "Relacion Eliminada"}
        else:
            return {"response": "Ingrese los nodos correctamente"}
    except Exception as ex:
        return ("Error:", ex.message)

# Des/Relacion Persona -> Produce -> Pelicula
def relacPPM(inputTitle, inputName):
    try:
        driver_neo4j = connectionDB()
        session = driver_neo4j.session()
        query="""
        MATCH (p:Person {name:$inpN})
        MATCH (m:Movie {title:$inpT})
        WHERE NOT (p)-[:PRODUCED]->(m)
        CREATE (p)-[:PRODUCED]->(m)
        """

        x = {"inpT":inputTitle, "inpN":inputName}
        result = session.run(query,x)
        summary = result.consume().counters
        cant = summary.relationships_created

        if (cant > 0):
            return {"response": "Relacion Creada"}
        else:
            return {"response": "Ingrese los nodos correctamente"}
    except Exception as ex:
        return ("Error:", ex.message)

def drelacPPM(inputTitle, inputName):
    try:
        driver_neo4j = connectionDB()
        session = driver_neo4j.session()
        query="""
        MATCH (p:Person {name:$inpN})-[r:PRODUCED]->(m:Movie {title:$inpT})
        DELETE r
        """

        x = {"inpT":inputTitle, "inpN":inputName}
        result = session.run(query,x)
        summary = result.consume().counters
        cant = summary.relationships_deleted

        if (cant > 0):
            return {"response": "Relacion Eliminada"}
        else:
            return {"response": "Ingrese los nodos correctamente"}
    except Exception as ex:
        return ("Error:", ex.message)

# Des/Relacion Persona -> Escribe -> Pelicula
def relacPWM(inputTitle, inputName):
    try:
        driver_neo4j = connectionDB()
        session = driver_neo4j.session()
        query="""
        MATCH (p:Person {name:$inpN})
        MATCH (m:Movie {title:$inpT})
        WHERE NOT (p)-[:WROTE]->(m)
        CREATE (p)-[:WROTE]->(m)
        """

        x = {"inpT":inputTitle, "inpN":inputName}
        result = session.run(query,x)
        summary = result.consume().counters
        cant = summary.relationships_created

        if (cant > 0):
            return {"response": "Relacion Creada"}
        else:
            return {"response": "Ingrese los nodos correctamente"}
    except Exception as ex:
        return ("Error:", ex.message)

def drelacPWM(inputTitle, inputName):
    try:
        driver_neo4j = connectionDB()
        session = driver_neo4j.session()
        query="""
        MATCH (p:Person {name:$inpN})-[r:WROTE]->(m:Movie {title:$inpT})
        DELETE r
        """

        x = {"inpT":inputTitle, "inpN":inputName}
        result = session.run(query,x)
        summary = result.consume().counters
        cant = summary.relationships_deleted

        if (cant > 0):
            return {"response": "Relacion Eliminada"}
        else:
            return {"response": "Ingrese los nodos correctamente"}
    except Exception as ex:
        return ("Error:", ex.message)
