from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()
movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado pandora viven",
        "year": 2009,
        "rating": 7.8,
        "category": "Acción"

    },
    {
        "id": 2,
        "title": "Avatar2",
        "overview": "En un exuberante planeta llamado pandora viven",
        "year": 2005,
        "rating": 7.9,
        "category": "Acción"

    }
]

app.title = "Mi app con FastAPi"
app.version = "0.0.1"

class Movie(BaseModel):
    id: Optional[int]= None
    title: str = Field(max_length=20)
    overview: str
    year: int
    rating: float
    category: str
    
@app.get('/', tags=['home'])
def message():
    return HTMLResponse("<h1>Hello World</h1>")


@app.get('/movies', tags=['movies'])
def get_movies():
    return JSONResponse(content=movies)

@app.get('/movies/{id}', tags=['movies'])
def get_movie(id: int = Path(ge=1,le=2000)):
    for item in movies:
        if item["id"] == id:
            return JSONResponse(content=item)
    return JSONResponse(content=[])


@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str = Query(max_length=20)):
    return JSONResponse(content=list(filter(lambda item:item['category']==category,movies)))


@app.post('/movies', tags=['movies'])
def create_movie(movie: Movie):
    movies.append(movie)
    return JSONResponse(content={"message":"se ha registrado la pelicula"})

@app.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, movie: Movie):

    for movie_aux in movies:
        if movie_aux.get("id") == id:
            movie_update=movie_aux
            break
    
    if movie_aux:
        movie_update["title"]=movie.title
        movie_update["overview"]=movie.overview
        movie_update["year"]=movie.year
        movie_update["rating"]=movie.rating
        movie_update["category"]=movie.category
        return JSONResponse(content={"message":"se ha modfificado la eplicula"})
    else:
        return JSONResponse(content={"message":"no esta esa pelicula"})


@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    for movie_aux in movies:
        if movie_aux.get("id") == id:
            movie_update=movie_aux
            break
    if movie_aux:
        movies.remove(movie_aux)
        return JSONResponse(content={"message":"se ha eliminado la elicula"})
    else:
        return JSONResponse(content={"message":"se ha registrado la elicula"})