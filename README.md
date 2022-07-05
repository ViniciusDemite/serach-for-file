# Sobre o projeto

Pesquisa no seu computador por arquivos com texto correspondente ao digitado.

## Executando o projeto

- `docker build -t search-for-file .` para construir a imagem que será utilizada
- `docker run -it --rm -v /home:/data search-for-file` para executar o programa
