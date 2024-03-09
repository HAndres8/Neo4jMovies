from src.conf.configDB import connectionDB
from src.schema import movieModel

# Obtener todas las peliculas
def getMovie():
    try:
        driver_neo4j = connectionDB()
        session = driver_neo4j.session()
        query="""
        MATCH (m:Movie) RETURN m.title as ti, m.released as fe, m.tagline as tl
        """

        results = session.run(query)
        movie = [{"Titulo": row["ti"], "Fecha Lanzamiento": row["fe"], "Descripcion": row["tl"]}
                for row in results]
        
        return movie
    except Exception as ex:
        return ("Error:", ex.message)

# Obtener las peliculas y sus reseñas
def getMovieRe():
    try:
        driver_neo4j = connectionDB()
        session = driver_neo4j.session()
        query="""
        MATCH (p:Person)-[r:REVIEWED]->(m:Movie) RETURN m.title as ti, 
        COLLECT({Nombre: p.name, Comentario: r.summary, Puntuacion: r.rating}) as re
        """

        results = session.run(query)
        rta = [{"Titulo": row["ti"], "Reseña": row["re"]} for row in results]
        
        return rta
    except Exception as ex:
        return ("Error:", ex.message)

# Agregar una pelicula
def postMovie(nodeM:movieModel):
    try:
        driver_neo4j = connectionDB()
        session = driver_neo4j.session()
        query="""
        CREATE (m:Movie {released:$re, tagline:$tl, title:$ti})
        """

        x = {"re":nodeM.released, "tl":nodeM.tagline, "ti":nodeM.title}
        session.run(query,x)

        return {"response": "Nodo de Pelicula creado.", "movie": nodeM}
    except Exception as ex:
        return ("Error:", ex.message)

# Modificar una pelicula
def updateMovie(nodeM:movieModel, inputTitle):
    try:
        driver_neo4j = connectionDB()
        session = driver_neo4j.session()
        query="""
        MATCH (m:Movie {title:$inpT}) set m.released=$re, m.tagline=$tl, m.title=$ti
        RETURN m
        """

        x = {"inpT":inputTitle, "re":nodeM.released, "tl":nodeM.tagline, "ti":nodeM.title}
        result = session.run(query,x)
        summary = result.consume().counters
        cant = summary.properties_set

        if (cant > 0):
            return {"response": f"La pelicula '{inputTitle}' se ha actualizado"}
        else:
            return {"response": "Esta pelicula no se encuentra actualmente"}
    except Exception as ex:
        return ("Error:", ex)

# Eliminar una pelicula
def deleteMovie(inputTitle):
    try:
        driver_neo4j = connectionDB()
        session = driver_neo4j.session()
        query="""
        MATCH (m:Movie {title:$inpT}) DETACH DELETE m
        """

        x = {"inpT":inputTitle}
        result = session.run(query,x)
        summary = result.consume().counters
        cant = summary.nodes_deleted

        if(cant > 0):
            return {"response": f"La pelicula '{inputTitle}' ha sido eliminada"}
        else:
            return {"response": "Esta pelicula no se encuentra actualmente"}
    except Exception as ex:
        return ("Error:", ex)