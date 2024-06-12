from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = '1234'

class Jogos():
    def __init__(self,nome,tipo,console):
        self.nome = str(nome)
        self.tipo = str(tipo)
        self.console = str(console)



jogo1 = Jogos('CS','FPS','PC')
jogo2 = Jogos('Age of Mythology','RPG','PC')
lista = [jogo1,jogo2]

@app.route('/')
def index():
    return render_template('/lista.html', titulo='Jogos', jogos=lista)

@app.route('/newGame')
def newGame():
    if 'usuario_logado' not in session or session ['usuario_logado'] == None:
        return redirect('/login')
    return render_template('newGame.html', titulo='Novo Jogo')

@app.route('/criar', methods = ['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogos(nome,categoria,console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods = ['POST',])
def autenticar():
    if '1234' == request.form['senha']:
        session ['usuario_logado'] = request.form['usuario']
        flash(session ['usuario_logado'] + ' logado com sucesso!')
        return redirect('/newGame')
    else:
        flash('Usuario não logado!')
        return redirect('/login')
    
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash(' Usuario desconectado!')
    return redirect('/')









app.run(debug=True)