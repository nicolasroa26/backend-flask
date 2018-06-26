from post import postfb, ite_groups
from flask import request, redirect, render_template
from app import app
from db import insert, formulario, table

def users(tokens):
	usuarios={}
	usuario = 0
	tokens = tokens.split(',')
	for user in tokens:
		if user!= '' :
			usuario = usuario+1
			usuarios['usuario'+ str(usuario)] ={'token': user ,'numeropost':0}
	return usuarios

def IDgroups(grupos):
    groups = []
    lis_grupos = grupos.split(',')
    for group in lis_grupos:
        if group != '':
            groups.append(group)    
    return groups

@app.route('/', methods=['POST'])
def params():   
    message = request.form['post']
    tokens = request.form['token']
    grupos = request.form['grupos']
    usuarios = users(tokens)
    groups = IDgroups(grupos)
    result = table()
    if len(groups) >= 1 and len(usuarios) >= 1 and len(message) != 0:
        ite_groups(groups,message,usuarios)
        insert(groups, usuarios, message)
        valor1 = 'parametros enviados'
    else:
        valor1 = 'faltan parametros'
    return render_template('index.html', valor1 = valor1, result = result, formulario = formulario)