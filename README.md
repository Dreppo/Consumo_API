# Busca de Universidades pelo Mundo

Este é um programa Python simples que permite aos usuários buscar informações sobre universidades em todo o mundo com base em critérios como país, sigla do país ou nome da universidade. O programa usa um conjunto de dados JSON(world_universities_and_domains.json)
contendo informações sobre universidades, como nome, país e sites.

## Requisitos

Python 3.x
Módulos: json, webbrowser, re (expressões regulares)


### Como Usar

-Executando o Programa

Certifique-se de que você possui Python instalado em seu sistema. Você pode executar o programa a partir de um terminal com o seguinte comando:

"python main.py"

-Opções de Pesquisa

O programa oferece três opções de pesquisa:

*Procurar por país: Digite o nome do país e selecione uma universidade pelo número.

*Procurar por sigla do país: Digite a sigla do país (por exemplo, BR para Brasil) e selecione uma universidade pelo número.

*Procurar por site da universidade: Digite o link do site da universidade (URL) e o programa abrirá a página no navegador.
Resultados da Pesquisa

-Resultados da Pesquisa

*Quando uma pesquisa por país ou sigla do país é feita, o programa exibirá informações sobre as universidades correspondentes, incluindo nome, país, sigla do país e sites.

*Se a pesquisa não retornar resultados, você verá uma mensagem indicando que a universidade não foi encontrada.
Abrindo Links no Navegador

-Abrindo Links no Navegador

Quando você escolher uma universidade para visualizar, o programa abrirá o link do site da universidade no navegador padrão do sistema.
