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

