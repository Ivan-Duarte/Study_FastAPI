from fastapi import FastAPI #Aqui estamos importando o framework FastAPI para nosso arquivo main.py

app = FastAPI() #Aqui eu estou atribuindo a função "FastAPI()" para uma variavel que chamei de "app"

@app.get('/')   #Aqui eu uso um "decorador" que é uma caracteristica que o Python tem de poder usar 
                #funções ou métodos existentes sem modificar diretamente o código fonte das mesmas

def index():                                        #Aqui defini uma função que chamei de "index" para testa o JSON que estou passando no "return".
    i = 1+1                                         #Aqui criei uma variável para ver como outros tipos de código podem ser retornados
    return {'data': {'name': 'Ivan', 'number': i}}  #Neste return eu estou returnando um dicionario em formato JSON para a função "index"

@app.get('/about')
def about():
    return {'data':'about page - pagina sobre'}