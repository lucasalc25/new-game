const editor = ace.edit("editor");
editor.setTheme("ace/theme/monokai");
editor.session.setMode("ace/mode/python");

document.getElementById("runCode").addEventListener("click", function () {
    const code = editor.getValue();

    fetch('http://127.0.0.1:5000/run', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ code: code })
    })
        .then(response => {
            console.log("Resposta do servidor:", response); // Adicione esta linha para debug
            return response.json(); // Tente converter a resposta em JSON
        })
        .then(data => {
            document.getElementById("output").innerText = data.output;
        })
        .catch(error => {
            console.error('Erro:', error);
        });
});