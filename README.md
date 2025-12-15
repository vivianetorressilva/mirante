# Repositório: Desafio Mirante

## Instalação:
    
    CrewAI, FastAPI, PostgreSQL

## Descrição da Solução:
### CrewAI
- Agente Analyzer (agents.yaml): analysa o código python recebido como entrada e sugere melhorias ou correções
- Tarefa Analyzer_task (task.yaml): tarefa realizada pelo agente Analyzer para sugerir melhorias ou correções

Para utilizar um LLM diferente ao usado no exemplo, alterar as seguintes linhas do código em main.py
- os.environ["HF_TOKEN"] = "KEY"
- os.environ["OPENAI_MODEL_NAME"] = "huggingface/meta-llama/Llama-3.1-8B-Instruct"

### FastAPI (main.py)
- /health/ serviço get que informa o status corrente do agente.
- /analyze-code/ serviço post que melhora ou corrige o código reebido como entrada.

### PostgreSQL (db_postgresql.py)
- open_connection() abre uma coneção para o DB
- create_table() cria a tabela, caso a tabela não exista
- insert_table(conn,code_snippet,suggestion) insere uma linha na tabela contendo o código original e a sugestão.

## Execução:
- Para testar a solução basta executar o comando uvicorn main:app --reload --port 8080
- Na sequencia, abra o browser no endereço http://localhost:8080/docs
- /health/ não possui parâmetro de entrada. 
- /analyze-code/ é experado que o código esteja dentro da uma célula chamada python_code em um dicionário, como a seguir:

    { "python_code":"x = [2, 8, 512]\n\n  for i  in x: \n\n print j" }

- Ao executar o analyze-code, o agente é invocado e, através do uso de LLM, sugere melhoria ou correção ao código fornecido como entrada.




