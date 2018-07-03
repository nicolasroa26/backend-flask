from post import postfb, ite_groups
from flask import request, redirect, render_template, Flask
from app import app
from db import insert, formulario, convert

def users(tokens):
	usuarios={}
	usuario = 0
	tokens = tokens.split(',')
	for user in tokens:
		if user!= "" :
			usuario = usuario+1
			usuarios["usuario"+ str(usuario)] ={"token": user ,"numeropost":0}
	return usuarios

def IDgroups(grupos):
    groups = []
    lis_grupos = grupos.split(',')
    for group in lis_grupos:
        if group != '':
            groups.append(group)    
    return groups

@app.route('/publications')
def publications():
    valor = convert()
    return render_template('datos.html',valor=valor)