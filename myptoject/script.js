async function enviarDados() {
    // Obter os valores do formulário
    const m2 = document.getElementById("m2").value;
    const quartos = document.getElementById("quartos").value;
    const banheiros = document.getElementById("banheiros").value;
    const idade = document.getElementById("idade").value;
    const distancia = document.getElementById("distancia").value;

    const garagem = document.querySelector('input[name="garagem"]:checked').value;

            // Criar o JSON com os dados do formulário
            const dadosImovel = {
                "m²": parseFloat(m2),
                "qnt Quartos": parseInt(quartos),
                "qnt Banheiros": parseInt(banheiros),
                "Idade": parseInt(idade),
                "Garagem": parseInt(garagem),
                "Distância centro": parseFloat(distancia)
            };

            try {
                // Enviar os dados para a API
                const response = await fetch('http://127.0.0.1:5000/predict', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(dadosImovel)
                });

                // Processar a resposta da API
                if (response.ok) {
                    const result = await response.json();
                    
                    // Armazenar o resultado na sessão do navegador
                    sessionStorage.setItem("preco_previsto", result.preço_previsto);
                    
                    // Redirecionar para a página de resultado em uma nova aba
                    window.open("resultado.html", "_blank");
                } else {
                    alert("Erro ao obter a previsão.");
                }
            } catch (error) {
                console.error("Erro ao enviar os dados:", error);
                alert("Erro de conexão com a API.");
            }
        }