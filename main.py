from flask import Flask,render_template,request,redirect,url_for,flash
from db.conexao import conectadb
from werkzeug import security
from util.u import ler_xlsx_e_gerar_tuples, retornaDadoParaInsert
import os

app = Flask(__name__)
app.secret_key = "123123213555"

@app.route("/")
def home():
    dados=""
    query = "select * from USERS"
    con = conectadb()
    cur = con.cursor()
    dados = cur.execute(query).fetchall()
    return render_template("index.html",dados=dados)


@app.route("/arquivos", methods=['POST'])
def uparquivo():
    arquivo = request.files['meuarquivo']
    print(arquivo)
    #nome_arquivo = arquivo.filename
    nome_arquivo = arquivo.filename
    extensao = os.path.splitext(nome_arquivo)[1]
    #verifica extenção do arquivo
    #print(extensao)
    if extensao == ".xlsx":
        local = rf"C:\Users\Eler\Desktop\projetoflask\diretorio"
        arquivo.save(os.path.join(local,arquivo.filename))
        #converte arquivo xlsx em tuplas sql para inserção em massa no banco de dados
        dados = ler_xlsx_e_gerar_tuples("{}\{}".format(local,arquivo.filename), "{}\{}".format(local,"teste.txt"))
        query="""
            INSERT INTO USERS (
                        nome,
                        idade
                    )
                    VALUES 
                        {}
        """.format(dados)
        con = conectadb()
        cur = con.cursor()
        try:
            cur.execute(query)
            con.commit()
            flash("Dados inseridos com sucesso!")
        except:
            flash("Não foi possivel importar os dados, verifique o arquivo!")
    else:
        flash("Não é possivel importar dados de arquivos diferentes de .xlsx")
    
    return redirect(url_for('home'))


@app.route("/nav")
def navbar():
    return render_template("navbar.html")

@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    if request.method == 'GET':  
        return render_template("form.html")
    else:
        try:
            con = conectadb()
            cur = con.cursor()
            #adicionar os campos do forms aqui.
            nome = request.form['nome']
            idade = request.form['idade']
            
            dados = (nome, idade)
            
            sql = """
            INSERT INTO USERS (nome,idade) VALUES (?,?);
            """
            cur.execute(sql,dados)
            con.commit()
            flash("Dados cadastrados com sucesso!",'success')
            return redirect(url_for('home'))
        except:
            print("erro ao conectar com o banco")
            return redirect(url_for('home',resposta="Não foi possivel cadastrar o usuario!"))
        
        
@app.route("/editarRegistro/<string:id>", methods=['GET', 'post'])
def editar(id):
    if request.method == 'GET':  
        con = conectadb()
        cur = con.cursor()
        
        cur.execute("select * from USERS where id = ?", (id,))
        data=cur.fetchone()
        print(data)
        print("entrou no get")
        return render_template("form.html",dados=data)
        
    else:
        print("entrou no put")
        con = conectadb()
        cur = con.cursor()
        nome = request.form['nome']
        idade = request.form['idade']
        dados = (nome, idade,id)
        sql = """
        UPDATE USERS
        SET
            nome = ?,
            idade = ?
        WHERE id = ?; 
        
        """
        cur.execute(sql,dados)
        con.commit()
        flash("Dados Atualizados!", 'success')
        return redirect(url_for('home'))
    
            #print("erro ao conectar com o banco")
           #s return redirect(url_for('home'))
           

@app.route("/deletar<string:id>")
def deletar(id):
    query = "delete from USERS where id = ?"
    con =conectadb()
    cur = con.cursor()
    try:
        cur.execute(query, (id,))
        con.commit()
        flash("true")
        return redirect(url_for('home'))
    except:
        flash("false")
        print("Erro")
        return redirect(url_for('home'))



@app.route("/buscaProfissao", methods=["GET"])
def buscarProfissao():
    #obtem apenas a descricao da profissao
    query = "select descricao from PROFISSAO"
    con = conectadb()
    cur = con.cursor()
    
    try:
        #obtem os dados e coloca na variavel dados
        dados = cur.execute(query).fetchall()
        return dados
    except:
        print("Erro ao buscar no banco")
        return "erro"

app.run(debug=True)