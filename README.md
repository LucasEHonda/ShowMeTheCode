# ShowMeTheCode 

## TELZIR

Este repositório representa o desafio "TELZIR" da vizir.

### Pré-requisitos
Caso você tenha `DOCKER` instalado você so precisa rodar o comando `docker-compose up --build` na raiz do projeto.

<br>

Front-end:
- Você pode rodar `npm install` ou seu gerenciador de pacotes favorito.

Back-end:
- Você pode instalar a partir do arquivo `requirements.txt` na pasta `backend/`.

<br>

Em todos os casos você pode ler o `README.md` dentro dos seus respectivos diretórios para mais informações.

<br>

### Back-end

O backend roda na porta 8000 por padrão.

Você pode procurar pelos endpoints:

- /admin
- /calls [ POST/GET ]
- /me [ GET ]
- /create [ POST ]
- /token [ POST ]

<br>

Para rodar os tests você pode utilizar o comando `python manage.py test` dentro do container docker ou no diretorio /backend.

<br>

### Front-end
O front-end roda na porta 4200 por padrão.

Ao rodar o projeto você sera redirecionado para a pagina de login. Você pode clicar em `cadastre-se` e depois logar.
