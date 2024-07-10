# SystemMetricsMonitor

## Instalação
Para instalar as dependências necessárias, execute o seguinte comando:

Para executar este projeto, você precisará instalar as seguintes bibliotecas Python:

- **psutil**:
  ```bash
  pip install psutil
- **psycopg2-binary**:
  ```bash
  pip install psycopg2-binary
- **Matplotlib**:
  ```bash
  pip install matplotlib

- **Pandas**:
  ```bash
  pip install pandas

### Configuração com o banco de dados
Lembre-se de preencher corretamento os parâmetros para conexão com o banco

- **Nesse projeto foi usado Postgres**:
  ```bash
  connection = psycopg2.connect(
            user="seu user",
            password="sua senha",
            host="seu host",
            port="sua porta",
            database="seu database")
