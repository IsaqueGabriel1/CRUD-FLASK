from flask import Flask,render_template,request,redirect,url_for,flash
from db.conexao import conectadb


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


@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    if request.method == 'GET':  
        return render_template("form.html")
    else:
        try:
            con = conectadb()
            cur = con.cursor()
            
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
           
        


app.run(debug=True)