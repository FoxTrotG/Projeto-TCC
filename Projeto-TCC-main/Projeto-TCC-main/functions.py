import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_email(comprador,cpf,telefone,email,titulo,autor,editora,valor):

        text_email='''

            <h2 style="text-align: center;">Recibo - Biblioteca ReadMe</h2>
            <hr>
            <table style="width: 100%; margin-bottom: 20px; border-collapse: collapse;">
                <tr>
                    <th colspan="2">Informações do Comprador</th>
                </tr>
                <tr>
                    <td>Nome:</td>
                    <td> '''+ str(comprador) +'''</td>
                </tr>
                <tr>
                    <td>CPF:</td>
                    <td>'''+ str(cpf) +'''</td>
                </tr>
                <tr>
                    <td>Telefone:</td>
                    <td>'''+ str(telefone) +'''</td>
                </tr>
                <tr>
                    <td>E-mail:</td>
                    <td>'''+ str(email) +'''</td>
                </tr>
            </table>
            <hr>
            <table style="width: 100%; margin-bottom: 20px; border-collapse: collapse;">
                <tr>
                    <th colspan="2">Livro Comprado</th>
                </tr>
                <tr>
                    <td>Título:</td>
                    <td>'''+ str(titulo) +'''</td>
                </tr>
                <tr>
                    <td>Autor:</td>
                    <td>'''+ str(autor) +'''</td>
                </tr>
                <tr>
                    <td>Editora:</td>
                    <td>'''+ str(editora) +'''</td>
                </tr>
            </table>
            <hr>
            <table style="width: 100%; margin-bottom: 20px; border-collapse: collapse;">
                <tr>
                    <th>Total:</th>
                    <td>R$ '''+ str(valor) +'''</td>
                </tr>
            </table>
            <hr>
            <br>
            <p><i>Agradecemos pela preferência!</i></p>
            <p><strong>Biblioteca ReadMe</strong></p>'''
    
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Recibo do livro Harry Potter"
        msg['From'] = 'bibliotecareadme@outlook.com'
        msg['To'] = 'bibliotecareadme@outlook.com'
        password = 'Foxtrot2023'
    
        part = MIMEText(text_email, 'html')
        msg.attach(part)
    
        s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
        s.starttls()
    
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string())
        s.quit()
    
def gerar_txt(comprador, cpf, telefone, email, titulo, autor, editora, valor):
    # Texto do recibo
    txt = f'''
        Recibo - Biblioteca ReadMe

        Comprador:
        Nome: {comprador}
        CPF: {cpf}
        Telefone: {telefone}
        E-mail: {email}

        Livro Comprado:
        Título: {titulo}
        Autor: {autor}
        Editora: {editora}

        Total: R$ {valor}

        Agradecemos pela compra!
        Biblioteca ReadMe
    '''

    # Gerar o arquivo TXT
    with open('static/recibo.txt', 'w') as file:
        file.write(txt)

    # Fechar o arquivo
    file.close()
        