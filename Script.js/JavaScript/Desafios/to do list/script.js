document.addEventListener('DOMContentLoaded', carregarTarefas);

function adicionarTarefas(){
    let input = document.querySelector('#text');
    let lista = document.querySelector('.tarefas');

    if (input.value.trim() === '') return;

    let li = document.createElement('li');
    li.innerHTML = `${input.value} <button onclick="removerTarefa(this)">❌</button>`;

    li.addEventListener('click', function(){
        li.classList.toggle("completed");
        salvarTarefas();
    });

    lista.appendChild(li);
    
    salvarTarefas();

    input.value = '';
}

function removerTarefa(botao){  
    botao.parentElement.remove();
    salvarTarefas();
}

function salvarTarefas(){
    let tarefas = [];
    document.querySelectorAll('.tarefas li').forEach(li => {
        tarefas.push({
            texto: li.textContent.replace('❌', '').trim(),
            concluida: li.classList.contains("completed")
        });
    });
    localStorage.setItem("tarefas", JSON.stringify(tarefas));
}

function carregarTarefas() {
    let tarefas = JSON.parse(localStorage.getItem("tarefas")) || [];
    let lista = document.querySelector(".tarefas");

    tarefas.forEach(tarefa => {
        let li = document.createElement("li");
        li.innerHTML = `${tarefa.texto} <button onclick="removerTarefa(this)">❌</button>`;
        if (tarefa.concluida) li.classList.add("completed");

        li.addEventListener("click", function() {
            li.classList.toggle("completed");
            salvarTarefas();
        });

        lista.appendChild(li);
    });
}