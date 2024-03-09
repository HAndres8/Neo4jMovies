from pydantic import BaseModel

# Modelos de como estan conformadas los nodos y algunas relaciones en Neo4j
class movieModel(BaseModel):
    released:int
    tagline:str
    title:str

class personModel(BaseModel):
    name:str
    born:int

class reviewModel(BaseModel):
    rating: int
    summary: str

class actingModel(BaseModel):
    roles: list