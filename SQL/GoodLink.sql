CREATE DATABASE GoodLink;
USE GoodLink;

CREATE TABLE Usuarios (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NomeUsuario VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE,
    Senha VARCHAR(255) NOT NULL
);

CREATE TABLE PlaylistCategoria (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NomeCategoria VARCHAR(255) NOT NULL
);

CREATE TABLE Playlists (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    TituloPlaylist VARCHAR(255) NOT NULL,
    DescricaoPlaylist TEXT,
    URLPlaylistYouTube VARCHAR(2000) NOT NULL,
    URLCanal VARCHAR(255) NOT NULL,
    nomeDoCanal VARCHAR(255) NOT NULL,
    IDCategoria INT,
    IDUsuarioCriador INT,
    DataPublicacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (IDUsuarioCriador) REFERENCES Usuarios(ID),
    FOREIGN KEY (IDCategoria) REFERENCES PlaylistCategoria(ID)
);
