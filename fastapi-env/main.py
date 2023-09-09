from fastapi import FastAPI #Aqui estamos importando o framework FastAPI para nosso arquivo main.py
from typing import Optional
from pydantic import BaseModel
import uvicorn


#Aqui eu estou atribuindo a função "FastAPI()" para uma variavel que chamei de "myapp"
myapp = FastAPI() 


#Aqui eu uso um "decorador" que é uma caracteristica que o Python tem de poder usar funções ou métodos existentes sem modificar diretamente o código fonte das mesmas
#Aqui defini uma função que chamei de "index" para testa o JSON que estou passando no "return".
#Neste return eu estou returnando um dicionario em formato JSON para a função "index"

@myapp.get('/blog')   
def index(limit=10, published: bool = True, sort: Optional[str] = None):                           
    # only get 10 published blogs

    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:    
        return {'data': f'{limit} blogs from the db'} 

@myapp.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}

@myapp.get('/blog/{blog_id}')
def show(blog_id: int):               #A função show recebe blog_id como um inteiro
    # fetch blog with id = id
    return {'data': blog_id}

@myapp.get('/blog/{blog_id}/comments')
def comments(blog_id):
    # fetch comments of blog with id = blog_id
    return {'data' : {'1','2'}}

class Blog(BaseModel):
    title: str
    body:str
    published: Optional[bool]
    pass

@myapp.post('/blog')
def create_blog(blog: Blog):
    return {'data': f"Blog is created with title as {blog.title}"}