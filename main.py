from flask import Flask, render_template, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey  
from datetime import datetime
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SECRET_KEY'] = 'GoodLink'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:4467@localhost/GoodLink'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.route('/')
def home(): 
    return render_template('/index.html')

class Usuario(UserMixin, db.Model):
    __tablename__ = 'Usuarios'
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    NomeUsuario = db.Column(db.String(255), nullable=False)
    Email = db.Column(db.String(255), nullable=False, unique=True)
    Senha = db.Column(db.String(255), nullable=False)
    
    def get_id(self):
        return str(self.ID)

class PlaylistCategoria(db.Model):
    __tablename__ = 'PlaylistCategoria'
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    NomeCategoria = db.Column(db.String(255), nullable=False)

class Playlist(db.Model):
    __tablename__ = 'Playlists'
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    TituloPlaylist = db.Column(db.String(255), nullable=False)
    DescricaoPlaylist = db.Column(db.Text)
    URLPlaylistYouTube = db.Column(db.String(2000), nullable=False)
    URLCanal = db.Column(db.String(255), nullable=False)
    nomeDoCanal = db.Column(db.String(255), nullable=False)
    IDCategoria = db.Column(db.Integer, db.ForeignKey('PlaylistCategoria.ID'))
    IDUsuarioCriador = db.Column(db.Integer, db.ForeignKey('Usuarios.ID'))
    DataPublicacao = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

    IDUsuarioCriador = db.Column(db.Integer, db.ForeignKey('Usuarios.ID'))
    usuario_criador = db.relationship('Usuario', foreign_keys=[IDUsuarioCriador])


@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

@app.route('/registro', methods=["POST"])
def registro():
    nameRegister = request.form.get('name_register')
    emailRegister = request.form.get('email_register')
    passRegister = request.form.get('password_register') 

    # Verifica se o e-mail já está cadastrado
    if Usuario.query.filter_by(Email=emailRegister).first():
        flash('Email já cadastrado. Escolha outro.')
        return redirect("/")
    
    novo_usuario = Usuario(NomeUsuario=nameRegister, Email=emailRegister, Senha=passRegister)

    # Adiciona o novo usuário ao banco de dados
    db.session.add(novo_usuario)
    db.session.commit()

    flash('Cadastro realizado com sucesso!')
    return redirect("/")

# Rota para a página de login
@app.route('/login', methods=["POST"])
def login():
    emailLogin = request.form.get('email_login')
    passLogin = request.form.get('password_login')

    usuario = Usuario.query.filter_by(Email=emailLogin, Senha=passLogin).first()

    if usuario:
        flash('Login bem-sucedido!')
        login_user(usuario)
        return redirect("/_forum")
    else:
        flash('Usuário não encontrado ou senha incorreta.')
        return redirect("/")


@app.route('/adicionar_playlist', methods=["POST"])
@login_required
def adicionar_playlist():
    titulo = request.form.get('titulo')
    descricao = request.form.get('descricao')
    url_video = request.form.get('urlVideo')
    url_canal = request.form.get('urlCanal')
    nome_canal = request.form.get('nomeDoCanal')
    categoria_nome = request.form.get('categoria')  # Recebe o nome da categoria

    id_usuario = current_user.ID  # Utiliza o ID do usuário logado
    hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Verifica se a categoria já existe
    categoria = PlaylistCategoria.query.filter_by(NomeCategoria=categoria_nome).first()

    if not categoria:
        # Se a categoria não existe, cria uma nova
        categoria = PlaylistCategoria(NomeCategoria=categoria_nome)
        db.session.add(categoria)
        db.session.commit()

    # Cria a nova playlist associada à categoria encontrada ou criada
    nova_playlist = Playlist(
        TituloPlaylist=titulo,
        DescricaoPlaylist=descricao,
        URLPlaylistYouTube=url_video,
        IDCategoria=categoria.ID,  # Associa à categoria encontrada ou criada
        IDUsuarioCriador=id_usuario,
        DataPublicacao=hora_atual,
        URLCanal=url_canal,
        nomeDoCanal=nome_canal
    )

    db.session.add(nova_playlist)
    db.session.commit()

    flash('Nova playlist adicionada com sucesso!')
    return redirect('/_forum')


@app.route('/_forum')
@login_required
def forum():
    playlists = Playlist.query.all()
    categorias = PlaylistCategoria.query.all()
    return render_template("/forum.html", playlists=playlists, categorias=categorias)

@app.route('/_form')
@login_required
def form():
    playlists = Playlist.query.all()
    categorias = PlaylistCategoria.query.all()
    return render_template("/form.html", playlists=playlists, categorias=categorias)

@app.route('/detail/<playlist_id>')
@login_required
def detail(playlist_id):
    # Aqui você busca as informações da playlist com base no ID do banco de dados
    playlist = Playlist.query.get(playlist_id)

    # Verifica se a playlist existe
    if playlist is None:
        # Adicione o tratamento adequado caso a playlist não seja encontrada
        return render_template("404.html"), 404

    # Adicione o link da playlist ao objeto Playlist antes de passá-lo para o template
    playlist_embed_url = playlist.URLPlaylistYouTube
    
    # Aqui, estou passando a variável playlist para o template
    return render_template("detail.html", playlist=playlist, playlist_embed_url=playlist_embed_url)


@app.route('/termos')
def termos():
    return render_template('termos.html')

@app.route('/politica')
def politica():
    return render_template('politica.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

if __name__ in "__main__":
    app.run(debug=True)