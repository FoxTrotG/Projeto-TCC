# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1994@localhost/biblioteca'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class Livros(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(30)) 
    valor = db.Column(db.Integer)
    autor = db.Column(db.String(20))
    editora = db.Column(db.String(20))
    quantidade = db.Column(db.Integer)

    def __init__(self, nome, valor, autor, editora, quantidade):
        self.nome = nome
        self.valor = valor
        self.autor = autor
        self.editora = editora
        self.quantidade = quantidade

class Comprador(db.Model):
    id_comprador = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(60)) 
    cpf = db.Column(db.String(14))
    telefone = db.Column(db.db.String(14))
    email = db.Column(db.String(60)) 
    livro_id = db.Column(db.Integer, db.ForeignKey('livros.id'))

    def __init__(self,nome,cpf,telefone,email,livro_id):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.livro_id = livro_id


with app.app_context():
    db.create_all()

