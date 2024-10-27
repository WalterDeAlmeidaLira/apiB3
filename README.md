
# API de Raspagem de Taxas de Referência da B3

## Descrição  
Esta API realiza a **raspagem de dados** da B3, retornando as **taxas de referência** em diferentes moedas ou índices.  
Foi construída utilizando **Django** e **Python**, com o objetivo de **automatizar a consulta** dessas informações de forma eficiente e acessível via endpoints HTTP.

### Motivação  
O projeto foi desenvolvido para facilitar o acesso automatizado às taxas de referência da B3, evitando consultas manuais e tornando o processo mais dinâmico para usuários e aplicações.

---

## Instruções de Instalação  

1. **Clone o repositório** e entre na pasta do projeto:  
   ```bash
   git clone https://github.com/WalterDeAlmeidaLira/apiB3.git
   cd apiB3
   ```

2. **Crie um ambiente virtual** em Python:  
   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual**:  
   - **Windows**:  
     ```bash
     venv\Scripts\activate
     ```
   - **Linux/Mac**:  
     ```bash
     source venv/bin/activate
     ```

4. **Instale as dependências** listadas no arquivo `requirements.txt`:  
   ```bash
   pip install -r requirements.txt
   ```

5. **Execute as migrações do Django**:  
   ```bash
   python manage.py migrate
   ```

6. **Inicie o servidor**:  
   ```bash
   python manage.py runserver
   ```

---

## Endpoints da API  

### 1. Buscar Taxas de Referência  
**Endpoint:**  
```
GET /dados?data=<YYYY-MM-DD>&slcTaxa=<moeda/índice>
```

**Exemplo:**  
```
localhost:8000/dados?data=2024-10-27&slcTaxa=EUR
```

**Parâmetros:**  
- **`data`**: Data desejada para a consulta das taxas (formato: `YYYY-MM-DD`).  
- **`slcTaxa`**: Moeda ou índice de referência, como `EUR` (Euro) ou outros índices disponíveis na B3.

---

## Observações  
- O ambiente virtual **não está incluído** no projeto. Certifique-se de criar o seu próprio.  
- Garanta que a API tenha acesso à internet, pois a raspagem depende de sites externos.  
