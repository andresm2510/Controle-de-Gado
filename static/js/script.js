let subMenu = document.getElementById("subMenu");

        function toggleMenu() {
            subMenu.classList.toggle("open-menu");
        }

let read_button = document.querySelectorAll('.read_button');

for(let i = 0; i<read_button.length; i++){
    read_button[i].addEventListener('click', function(){
        read_button[i].parentNode.classList.toggle('active')
    })
}