const log = window.document.getElementById('inpt-for-login')
const caixalogin = window.document.getElementById('login')

const reg = window.document.getElementById('inpt-for-registro')
const caixaregistrar = window.document.getElementById('registro')

caixaregistrar.style.display = 'none'
caixalogin.style.display = 'block'
log.addEventListener('click',entrar)
reg.addEventListener('click',registrar)

function entrar(){
    if (caixalogin.style.display == 'none' && caixaregistrar.style.display == 'block') {
        caixalogin.style.display = 'block'
        caixaregistrar.style.display = 'none'
    }
}

function registrar(){
    if (caixaregistrar.style.display == 'none' && caixalogin.style.display == 'block') {
        caixaregistrar.style.display = 'block'
        caixalogin.style.display = 'none'}
}

// -------------------------------- Botão playlist

  // Pega os elementos pelo ID
  const addPlaylistForm = document.getElementById('playlistforumadd');
  const playlistForum = document.getElementById('playlistforum');

  // Alterna a exibição das classes
  function toggleAddPlaylistForm() {
      if (addPlaylistForm.style.display === 'none') {
          addPlaylistForm.style.display = 'block';
          playlistForum.style.display = 'none';
      } else {
          addPlaylistForm.style.display = 'none';
          playlistForum.style.display = 'block';
      }
  }

  // Executa a função toggleAddPlaylistForm quando o botão for clicado
  document.getElementById('inpt-for-login').addEventListener('click', toggleAddPlaylistForm);

// -------------------------------- Flash alert

const mostrarAlertaBotao = document.getElementById('mostrarAlerta');
const flashAlertDiv = document.querySelector('.flashAlertDiv');

mostrarAlertaBotao.addEventListener('click', function() {
  flashAlertDiv.style.display = 'block';
});

// -------------------------------- Botões

// Event listeners
const playlistButton = document.getElementById('inpt-for-playlist');
const addPlaylistButton = document.getElementById('inpt-for-addplaylist');

playlistButton.addEventListener('click', () => {
    window.location.href = forumURL;
});

addPlaylistButton.addEventListener('click', () => {
    window.location.href = formURL;
});
