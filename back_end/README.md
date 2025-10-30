### Rest API Agenda Pediatrica
Uma API no padrão REST utilizando o [FastAPI](https://fastapi.tiangolo.com/pt/) framework.

## Demonstração

Insira um gif ou um link de alguma demonstração
## Início Rápido

#### 1. clone este repositório

```git
  git clone http://seu_repositorio/rest_api_in_python_agendada_pediatrica.git
```
#### 2. instale o FastAPI

```bash
  pip install "fastapi[standard]"
```

#### 3. acesse o diretório /back_end
```bash
  cd back_end
```


#### 4. execute o servidor

```bash
  uvicorn app.main:app --reload
```
#### 5. Acesse o endereço em http://127.0.0.1:8000/docs no navegador

## Documentação da API

#### Retorna todos os itens

```http
  GET /api/items
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `api_key` | `string` | **Obrigatório**. A chave da sua API |

#### Retorna um item

```http
  GET /api/items/${id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. O ID do item que você quer |

#### add(num1, num2)

Recebe dois números e retorna a sua soma.


## 🛠 Habilidades
Javascript, HTML, CSS...

