from app import *
from functions import *

@app.route('/') 
def index():

    search = request.args.get('search')
    livros = Livros.query.filter(
        Livros.nome.like(f'%{search}%') | 
        Livros.editora.like(f'%{search}%') |
        Livros.autor.like(f'%{search}%')
    ).all() if search else Livros.query.all()

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
            
@app.route("/cadastro/<int:id>", methods=['GET', 'POST'])
def cadastro(id):

    if request.method == "POST":
        nome = request.form.get("comprador")
        cpf = request.form.get("cpf")
        telefone = request.form.get("telefone")
        email = request.form.get("email")

        if nome and cpf and telefone and email:
            C = Comprador(nome, cpf, telefone, email, livro_id=id)
            db.session.add(C)
            livro = Livros.query.filter_by(id=id).first()
            livro.quantidade -= 1 
            db.session.commit()

        # Buscar informações do livro
        livro_info = {
            'titulo': livro.nome,
            'autor': livro.autor,
            'editora': livro.editora,
            'valor': livro.valor
        }

        comprador = request.form.get("comprador")
        cpf = request.form.get("cpf")
        telefone = request.form.get("telefone")
        email = request.form.get("email")
        titulo = livro.nome
        autor = livro.autor
        editora = livro.editora
        valor = livro.valor
    
        gerar_txt(comprador, cpf, telefone, email, titulo, autor, editora, valor)

        return render_template("recibo.html", comprador=nome, cpf=cpf, telefone=telefone, email=email, **livro_info)

    return render_template("cadastro.html")

@app.route('/recibo', methods=['GET'])
def recibo():
    
    return render_template('recibo.html')

@app.route('/email', methods=['POST'])
def email():

    if 'btn_email' in request.form:
        comprador = request.form.get("comprador")
        cpf = request.form.get("cpf")
        telefone = request.form.get("telefone")
        email = request.form.get("email")
        titulo = request.form.get("titulo")
        autor = request.form.get("autor")
        editora = request.form.get("editora")
        valor = request.form.get("valor")
    

        enviar_email(comprador,cpf,telefone,email,titulo,autor,editora,valor)
    
    livros = Livros.query.all()
    return render_template('home.html', livros=livros)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
