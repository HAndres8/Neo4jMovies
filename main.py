from fastapi import FastAPI
from src.schema import *
from src.services.servicePerson import *
from src.services.serviceMovie import *
from src.services.serviceRelation import *

app=FastAPI()

@app.get("/")
def default():
    return {"response": "You are in root pathhhh"}

# === Metodos GET === #

@app.get("/obtenerM")
def obtenerPeliculas():
    return getMovie()

@app.get("/obtenerP")
def obtenerPersonas():
    return getPerson()

@app.get("/obtenerPersonInMovie")
def obtenerPersonasDePelicula(inputTitle):
    return getPersonInM(inputTitle)

@app.get("/obtenerReviews")
def obtenerResenias():
    return getMovieRe()


# === Metodos POST === #

@app.post("/crearM")
def crearPeliculas(nodeM:movieModel):
    return postMovie(nodeM)

@app.post("/crearP")
def crearPersonas(nodeP:personModel):
    return postPerson(nodeP)


# === Metodos PUT === #

@app.put("/actualizarM")
def actualizarPeliculas(nodeM:movieModel, inputTitle):
    return updateMovie(nodeM, inputTitle)

@app.put("/actualizarP")
def actualizarPersonas(nodeP:personModel, inputName):
    return updatePerson(nodeP, inputName)


# === Metodos DELETE === #

@app.delete("/eliminarM")
def eliminarPeliculas(inputTitle):
    return deleteMovie(inputTitle)

@app.delete("/eliminarP")
def eliminarPersonas(inputName):
    return deletePerson(inputName)


# === RELACIONAR Y DESRELACIONAR NODOS === #

@app.put("/relaPAM")
def relacionPersonaActuaPelicula(nodeA:actingModel, inputTitle, inputName):
    return relacPAM(nodeA, inputTitle, inputName)

@app.put("/drelaPAM")
def desrelacionPersonaActuaPelicula(inputTitle, inputName):
    return drelacPAM(inputTitle, inputName)

@app.put("/relaPRM")
def relacionPersonaReseniaPelicula(nodeR:reviewModel, inputTitle, inputName):
    return relacPRM(nodeR, inputTitle, inputName)

@app.put("/drelaPRM")
def desrelacionPersonaReseniaPelicula(inputTitle, inputName):
    return drelacPRM(inputTitle, inputName)

@app.put("/relaPDM")
def relacionPersonaDirigePelicula(inputTitle, inputName):
    return relacPDM(inputTitle, inputName)

@app.put("/drelaPDM")
def desrelacionPersonaDirigePelicula(inputTitle, inputName):
    return drelacPDM(inputTitle, inputName)

@app.put("/relaPPM")
def relacionPersonaProducePelicula(inputTitle, inputName):
    return relacPPM(inputTitle, inputName)

@app.put("/drelaPPM")
def desrelacionPersonaProducePelicula(inputTitle, inputName):
    return drelacPPM(inputTitle, inputName)

@app.put("/relaPWM")
def relacionPersonaEscribePelicula(inputTitle, inputName):
    return relacPWM(inputTitle, inputName)

@app.put("/drelaPWM")
def desrelacionPersonaEscribePelicula(inputTitle, inputName):
    return drelacPWM(inputTitle, inputName)