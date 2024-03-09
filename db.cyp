// Creacion de Peliculas
CREATE (:Movie {released:1993, tagline:'La verdadera historia de un hombre común que hizo algo extraordinario', title:'La Lista de Schindler'})
CREATE (:Movie {released:1994, tagline:'Agarrate los pantalones', title:'Tiempos Violentos'})
CREATE (:Movie {released:2010, tagline:'La mente es la escena del crimen', title:'Inception'})
CREATE (:Movie {released:1997, tagline:'Nada en la Tierra podía separarlos. Nada en el cielo podía salvarlos', title:'Titanic'})
CREATE (:Movie {released:2016, tagline:'Aquí está al sueño que llevamos en nuestros corazones. Aquí está la vida que viven en nuestras almas', title:'La La Land'})
CREATE (:Movie {released:1994, tagline:'La vida es como una caja de chocolates, nunca sabes lo que te va a tocar', title:'Forrest Gump'})
CREATE (:Movie {released:2012, tagline:'Nunca subestimes el poder de una mujer', title:'La Dama de Hierro'})
CREATE (:Movie {released:2002, tagline:'La vida es un guion', title:'Adaptation'})
CREATE (:Movie {released:2003, tagline:'Estar perdido nunca se sintió tan bien', title:'Lost in Translation'})

// Creacion de Personas
CREATE (:Person {name:'Steven Spielberg', born:1946})
CREATE (:Person {name:'Quentin Tarantino', born:1963})
CREATE (:Person {name:'Christopher Nolan', born:1970})
CREATE (:Person {name:'James Cameron', born:1954})
CREATE (:Person {name:'Damien Chazelle', born:1985})
CREATE (:Person {name:'Leonardo DiCaprio', born:1974})
CREATE (:Person {name:'Meryl Streep', born:1949})
CREATE (:Person {name:'Emma Stone', born:1988})
CREATE (:Person {name:'Charlie Kaufman', born:1958})
CREATE (:Person {name:'Nicolas Cage', born:1964})
CREATE (:Person {name:'Sofia Coppola', born:1971})
CREATE (:Person {name:'Elena', born:1993})
CREATE (:Person {name:'Juan Carlos', born:1998})

// Creacion de Relaciones

// Actores
MATCH (p:Person {name:'Tom Hanks'})
MATCH (m:Movie {title:'Forrest Gump'})
WHERE NOT (p)-[:ACTED_IN]->(m)
CREATE (p)-[:ACTED_IN {roles:['Forrest Gump']}]->(m);
MATCH (p:Person {name:'Leonardo DiCaprio'})
MATCH (m:Movie {title:'Titanic'})
WHERE NOT (p)-[:ACTED_IN]->(m)
CREATE (p)-[:ACTED_IN {roles:['Jack Dawson']}]->(m);
MATCH (p:Person {name:'Meryl Streep'})
MATCH (m:Movie {title:'La Dama de Hierro'})
WHERE NOT (p)-[:ACTED_IN]->(m)
CREATE (p)-[:ACTED_IN {roles:['Margaret Thatcher']}]->(m);
MATCH (p:Person {name:'Emma Stone'})
MATCH (m:Movie {title:'La La Land'})
WHERE NOT (p)-[:ACTED_IN]->(m)
CREATE (p)-[:ACTED_IN {roles:['Mia Dolan']}]->(m);
MATCH (p:Person {name:'Nicolas Cage'})
MATCH (m:Movie {title:'Adaptation'})
WHERE NOT (p)-[:ACTED_IN]->(m)
CREATE (p)-[:ACTED_IN {roles:['Charlie Kaufman','Donald Kaufman']}]->(m);

// Reseñas
MATCH (p:Person {name:'Elena'})
MATCH (m:Movie {title:'La Lista de Schindler'})
WHERE NOT (p)-[:REVIEWED]->(m)
CREATE (p)-[:REVIEWED {summary:'Spielberg entrega una narrativa poderosa e inolvidable.', rating:87}]->(m);
MATCH (p:Person {name:'Elena'})
MATCH (m:Movie {title:'La La Land'})
WHERE NOT (p)-[:REVIEWED]->(m)
CREATE (p)-[:REVIEWED {summary:'Chazelle captura la magia del cine musical con una historia encantadora.', rating:89}]->(m);
MATCH (p:Person {name:'Elena'})
MATCH (m:Movie {title:'Inception'})
WHERE NOT (p)-[:REVIEWED]->(m)
CREATE (p)-[:REVIEWED {summary:'Una experiencia cinematográfica que te deja reflexionando.', rating:93}]->(m);
MATCH (p:Person {name:'Elena'})
MATCH (m:Movie {title:'La Dama de Hierro'})
WHERE NOT (p)-[:REVIEWED]->(m)
CREATE (p)-[:REVIEWED {summary:'Presenta una visión superficial y simplista de la vida.', rating:44}]->(m);
MATCH (p:Person {name:'Juan Carlos'})
MATCH (m:Movie {title:'Titanic'})
WHERE NOT (p)-[:REVIEWED]->(m)
CREATE (p)-[:REVIEWED {summary:'Predecible en ocasiones pero emocional.', rating:80}]->(m);
MATCH (p:Person {name:'Juan Carlos'})
MATCH (m:Movie {title:'Tiempos Violentos'})
WHERE NOT (p)-[:REVIEWED]->(m)
CREATE (p)-[:REVIEWED {summary:'Un clásico moderno.', rating:98}]->(m);
MATCH (p:Person {name:'Juan Carlos'})
MATCH (m:Movie {title:'Lost in Translation'})
WHERE NOT (p)-[:REVIEWED]->(m)
CREATE (p)-[:REVIEWED {summary:'Un viaje melancólico y hermoso a través de las calles de Tokio.', rating:84}]->(m);
MATCH (p:Person {name:'Juan Carlos'})
MATCH (m:Movie {title:'Forrest Gump'})
WHERE NOT (p)-[:REVIEWED]->(m)
CREATE (p)-[:REVIEWED {summary:'La narrativa carece de profundidad y coherencia.', rating:20}]->(m);
MATCH (p:Person {name:'Juan Carlos'})
MATCH (m:Movie {title:'La La Land'})
WHERE NOT (p)-[:REVIEWED]->(m)
CREATE (p)-[:REVIEWED {summary:'La mejor pelicula jamas creada', rating:100}]->(m);

// Direcciones
MATCH (p:Person {name:'Steven Spielberg'})
MATCH (m:Movie {title:'La Lista de Schindler'})
WHERE NOT (p)-[:DIRECTED]->(m)
CREATE (p)-[:DIRECTED]->(m);
MATCH (p:Person {name:'Quentin Tarantino'})
MATCH (m:Movie {title:'Tiempos Violentos'})
WHERE NOT (p)-[:DIRECTED]->(m)
CREATE (p)-[:DIRECTED]->(m);
MATCH (p:Person {name:'Christopher Nolan'})
MATCH (m:Movie {title:'Inception'})
WHERE NOT (p)-[:DIRECTED]->(m)
CREATE (p)-[:DIRECTED]->(m);
MATCH (p:Person {name:'James Cameron'})
MATCH (m:Movie {title:'Titanic'})
WHERE NOT (p)-[:DIRECTED]->(m)
CREATE (p)-[:DIRECTED]->(m);
MATCH (p:Person {name:'Damien Chazelle'})
MATCH (m:Movie {title:'La La Land'})
WHERE NOT (p)-[:DIRECTED]->(m)
CREATE (p)-[:DIRECTED]->(m);
MATCH (p:Person {name:'Sofia Coppola'})
MATCH (m:Movie {title:'Lost in Translation'})
WHERE NOT (p)-[:DIRECTED]->(m)
CREATE (p)-[:DIRECTED]->(m);

// Producciones
MATCH (p:Person {name:'Steven Spielberg'})
MATCH (m:Movie {title:'La Lista de Schindler'})
WHERE NOT (p)-[:PRODUCED]->(m)
CREATE (p)-[:PRODUCED]->(m);
MATCH (p:Person {name:'Quentin Tarantino'})
MATCH (m:Movie {title:'Tiempos Violentos'})
WHERE NOT (p)-[:PRODUCED]->(m)
CREATE (p)-[:PRODUCED]->(m);

// Guiones
MATCH (p:Person {name:'Charlie Kaufman'})
MATCH (m:Movie {title:'Adaptation'})
WHERE NOT (p)-[:WROTE]->(m)
CREATE (p)-[:WROTE]->(m);
MATCH (p:Person {name:'Sofia Coppola'})
MATCH (m:Movie {title:'Lost in Translation'})
WHERE NOT (p)-[:WROTE]->(m)
CREATE (p)-[:WROTE]->(m);