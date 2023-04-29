from app import *

@app.route('/') 
def index():

    livros = Livros.query.all()

    return render_template('home.html', livros=livros)

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():

    if request.method == "POST":
        nome = request.form.get("nome")
        valor = request.form.get("valor")
        autor = request.form.get("autor")
        editora = request.form.get("editora")
        quantidade = request.form.get("quantidade")

        if nome and valor and autor and editora and quantidade:
            L = Livros(nome, valor, autor, editora, quantidade)
            db.session.add(L)
            db.session.commit()

        return redirect(url_for('index'))
    
    return render_template('lista.html')

@app.route("/excluir/<int:id>", methods=['GET', 'DELETE'])
def excluir(id):
    livros = Livros.query.filter_by(id=id).first()

    db.session.delete(livros)
    db.session.commit()

    livros = Livros.query.all()
    return render_template('home.html', livros=livros)

@app.route("/atualizar/<int:id>", methods=['GET','POST'])
def atualizar(id):
    livro = Livros.query.filter_by(id=id).first()
    
    if request.method == "POST":
        nome = request.form.get("nome")
        valor = request.form.get("valor")
        autor = request.form.get("autor")
        editora = request.form.get("editora")
        quantidade = request.form.get("quantidade")

        if nome and valor and autor and editora and quantidade:
            livro.nome = nome
            livro.valor = valor
            livro.autor = autor
            livro.editora = editora
            livro.quantidade = quantidade

            db.session.commit()

            return redirect(url_for("index"))
        
    return render_template("atualizar.html", livro=livro)
            


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
