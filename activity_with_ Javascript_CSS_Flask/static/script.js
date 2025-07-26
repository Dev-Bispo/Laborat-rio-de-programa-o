let form = document.getElementById("formulario")
let mensagem = document.getElementById("mensagem")

form.addEventListener("submit", function(event){
   
   
    let name = document.getElementById("name").value.trim()
    let email = document.getElementById("email").value.trim()
    let password = document.getElementById("password").value.trim()

    if (name == ""|| email == "" || password == ""){
    event.preventDefault();  
    mensagem.style.color = "red"
    mensagem.textContent =  "Preencha  tudo!!"

   
  }
   
  })

