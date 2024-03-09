from src.conf.configDB import connectionDB
from src.schema import personModel

# Obtener todas las personas
def getPerson():
    try:
        driver_neo4j = connectionDB()
        session = driver_neo4j.session()
        query="""
        MATCH (p:Person) RETURN p.name as nom, p.born as bo
        """

        results = session.run(query)
        person = [{"Nombre": row["nom"], "Año Nacimiento": row["bo"]}
                for row in results]
        
        return person
    except Exception as ex:
        return ("Error:", ex.message)

# Obtener los actores de una pelicula
def getPersonInM(inputTitle):
    try:
        driver_neo4j = connectionDB()
        session = driver_neo4j.session()
        query="""
        MATCH (m:Movie {title:$inpT})<-[:ACTED_IN]-(p:Person)
        RETURN COLLECT (p.name) as nom
        """

        x = {"inpT":inputTitle}
        results = session.run(query,x)
        rta = [{"Titulo": inputTitle, "Actores": row["nom"]} for row in results]
        
        return rta
    except Exception as ex:
        return ("Error:", ex.message)

# Agregar una persona
def postPerson(nodeP:personModel):
    try:
        driver_neo4j = connectionDB()
        session = driver_neo4j.session()
        query="""
        CREATE (p:Person {name:$nom, born:$bo})
        """

        x = {"nom":nodeP.name, "bo":nodeP.born}
        session.run(query,x)

        return {"response": "Nodo de Persona creado.", "person": nodeP}
    except Exception as ex:
        return ("Error:", ex.message)

# Modificar una persona
def updatePerson(nodeP:personModel, inputName):
    try:
        driver_neo4j = connectionDB()
        session = driver_neo4j.session()
        query="""
        MATCH (p:Person {name:$inpN}) set p.name=$nom, p.born=$bo
        RETURN p
        """

        x = {"inpN":inputName, "nom":nodeP.name, "bo":nodeP.born}
        result = session.run(query,x)
        summary = result.consume().counters
        cant = summary.properties_set

        if (cant > 0):
            return {"response": f"La persona '{inputName}' se ha actualizado"}
        else:
            return {"response": "Esta persona no se encuentra actualmente"}
    except Exception as ex:
        return ("Error:", ex)

# Eliminar una persona
def deletePerson(inputName):
    try:
        driver_neo4j = connectionDB()
        session = driver_neo4j.session()
        query="""
        MATCH (p:Person {name:$inpN}) DETACH DELETE p
        """

        x = {"inpN":inputName}
        result = session.run(query,x)
        summary = result.consume().counters
        cant = summary.nodes_deleted

        if(cant > 0):
            return {"response": f"La persona '{inputName}' ha sido eliminada"}
        else:
            return {"response": "Esta persona no se encuentra actualmente"}
    except Exception as ex:
        return ("Error:", ex)