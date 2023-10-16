var expandirGado = document.querySelector('#sub-gado')
var containers = document.querySelectorAll('.container_indicadores')

containers.forEach(function(container) {
    container.addEventListener('click', function(){
        container.classList.toggle('expandir');
    })
})
