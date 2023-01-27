from typing import List, Union
from fastapi import FastAPI,Body
from fastapi.responses import HTMLResponse #devolver valores html
from pydantic import BaseModel
from typing import Optional



#creación de una aplicación fastAPI:

app = FastAPI()

#cambiar titulo:
app.title = "mi app con fastAPI"

#cambiar versión:
app.version = "0.0.1"

class Movie(BaseModel):
    id: Optional[int]
    title: str
    overview: str
    year: int
    rating: float
    category: str

movies =[
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    },
    
    {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    },
]


@app.get("/", tags=['home']) #cambiar en documentación el titulo de la ruta

def read_root():
    return HTMLResponse('<H1> Hello World </H1>')

@app.get("/movies", tags=['movies'])
def get_movies():
    return movies

#parmetros de ruta
@app.get('/movies/{id}',tags=['movies'])
def get_movie(id:int):
    for item in movies:
        if item["id"] == id:
            return item
    return []


#parametros query

@app.get('/movies/',tags=['movies'])
def get_movies_by_category(category:str,year:int):

    return [item for item in movies if item['category'] == category]

#Metodo post
@app.post('/movies', tags=['movies'])
def create_movie(movie:Movie):
    movies.append(movie)
    return movies

#Metodo put y delete

#put
@app.put('/movies/{id}',tags=['movies'])
def update_movie(id:int, movie:Movie):
    for item in movies:
            if item["id"] == id:
                item['title'] = movie.title,
                item['overview'] = movie.overview,
                item['year'] = movie.year,
                item['rating'] = movie.rating,
                item['category'] = movie.category
                
                return movies

#delete
@app.delete('/movies/{id}',tags=['movies'])
def delete_movie(id:int):
    for item in movies:
            if item["id"] == id:
                movies.remove(item)
                return movies



# @app.get('/types/', tags=['types'])

# # def get_full_name(first_name, last_name):
# #     full_name = first_name.title() + " " + last_name.title()
# #         return full_name

# def get_full_name(first_name: str, last_name: str):
#     full_name = first_name.title() + " " + last_name.title()
#     return full_name

# @app.get('/error/', tags=['error'])

# def get_name_with_age(name: str, age: int):
#     name_with_age = name + " is this old: " + str(age)
#     return name_with_age


# #tipos con subtipos 
# #listas
# def process_items(items: List[str]):
#     for item in items:
#         print(item)
        

# #tuplas
