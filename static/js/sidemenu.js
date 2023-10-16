var menuItem = document.querySelectorAll('.item-menu')

function selectLink(){
    menuItem.forEach((item)=>
        item.classList.remove('ativo')
    )

    this.classList.add('ativo')
}

menuItem.forEach((item)=>
    item.addEventListener('click', selectLink)
)

//Expandir Menu

var btnExp = document.querySelector('#btn-exp')
var sideMenu = document.querySelector('.menu_lateral')

btnExp.addEventListener('click', function(){
    sideMenu.classList.toggle('expandir')
})