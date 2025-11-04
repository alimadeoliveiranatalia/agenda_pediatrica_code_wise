### Rest API Agenda Pediatrica
Uma API no padrão REST utilizando o [FastAPI](https://fastapi.tiangolo.com/pt/) framework.

## Demonstração

Insira um gif ou um link de alguma demonstração
## Início Rápido

#### 1. clone este repositório

```git
  git clone https://github.com/alimadeoliveiranatalia/agenda_pediatrica_code_wise
```
#### 2. acesse o diretório /back_end
```bash
  cd back_end
```
#### 3. instale as dependências

```bash
  pip install -r requirements.txt
```
#### 4. Para conectar o banco de dados
1. Renomei o arquivo `.env.example` para `.env`
2. Adicione a seguinte variável de ambiente `DATABASE_URL` no seu arquivo `.env`, onde:
   - `DATABASE_URL`: Obrigatório, string de conexão com o banco de dados
 ```bash
  DATABASE_URL="mysql+mysqlconnector://usuario:senha@localhost:3306/nome_database"
```

#### 5. execute o servidor

```bash
  uvicorn app.main:app --reload
```
#### 6. Acesse o endereço em http://127.0.0.1:8000/docs no navegador

## 🛠 Habilidades
Javascript, HTML, CSS...

