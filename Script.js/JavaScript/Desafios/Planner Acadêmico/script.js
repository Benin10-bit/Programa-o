// Função para salvar as tarefas no localStorage
function salvarTarefas() {
    let tarefas = [];
    document.querySelectorAll('.tasklist li').forEach(li => {
        tarefas.push({
            texto: li.querySelector('.task-text').textContent,
            data: li.querySelector('.task-date').textContent,
            prioridade: li.querySelector('.task-priority').textContent,
            concluida: li.classList.contains("completed")
        });
    });
    localStorage.setItem("tarefas", JSON.stringify(tarefas));
}

// Função para carregar as tarefas do localStorage
function carregarTarefas() {
    let tarefas = JSON.parse(localStorage.getItem("tarefas")) || [];
    let lista = document.querySelector(".tasklist");

    tarefas.forEach(tarefa => {
        let li = document.createElement("li");
        li.classList.add("task");

        // Estrutura da tarefa com texto, data, prioridade e botão de remoção
        li.innerHTML = `
            <span class="task-text">${tarefa.texto}</span> - 
            <span class="task-date">${tarefa.data}</span> - 
            <span class="task-priority">${tarefa.prioridade}</span>
            <button onclick="removerTarefa(this)">❌</button>
        `;

        // Marcar como concluída, se necessário
        if (tarefa.concluida) li.classList.add("completed");

        // Adicionar funcionalidade de marcar como concluída
        li.addEventListener("click", function() {
            li.classList.toggle("completed");
            salvarTarefas();
        });

        // Adicionar a tarefa à lista
        lista.appendChild(li);
    });
}

// Função para remover uma tarefa
function removerTarefa(botao) {
    botao.parentElement.remove();
    salvarTarefas();
}

// Função para adicionar uma nova tarefa
function addTask() {
    let input = document.querySelector('#texttask');
    let date = document.querySelector('#datetask');
    let prioridade = document.querySelector('#priority').value;

    if (input.value === '' || date.value === '') {
        alert('Preencha os campos necessários');
        return;
    }

    // Formatar a data para o formato DD/MM/YYYY
    let formattedDate = formatDate(date.value);

    let lista = document.querySelector('.tasklist');
    let li = document.createElement('li');
    li.classList.add("task");

    li.innerHTML = `
        <span class="task-text">${input.value}</span> - 
        <span class="task-date">${formattedDate}</span> - 
        <span class="task-priority">${prioridade}</span>
        <button onclick="removerTarefa(this)">❌</button>
    `;

    lista.appendChild(li);

    // Limpa os campos corretamente
    document.querySelector('#texttask').value = '';
    document.querySelector('#datetask').value = '';

    // Salvar a tarefa após a adição
    salvarTarefas();
}

// Função para formatar a data no formato DD/MM/YYYY
function formatDate(dateString) {
    let date = new Date(dateString);
    let day = String(date.getDate()).padStart(2, '0'); // Garantir que o dia tenha 2 dígitos
    let month = String(date.getMonth() + 1).padStart(2, '0'); // Garantir que o mês tenha 2 dígitos
    let year = date.getFullYear();

    return `${day}/${month}/${year}`;
}

// Carregar tarefas ao iniciar a página
document.addEventListener("DOMContentLoaded", function() {
    carregarTarefas();
});
