# Este é um aplicativo de lista de tarefas (TODO list) desenvolvido usando FastAPI em Python.

## Funcionalidades

- [ x ] **Criação de Tarefas:** Implementa um endpoint para criar novas tarefas, fornecendo um título e um status.
- [ x ] **Listagem de Tarefas:** Oferece um endpoint para listar todas as tarefas existentes.
- [ x ] **Atualização de Tarefas:** Permite atualizar uma tarefa existente, fornecendo o ID da tarefa a ser atualizada e os novos dados.
- [ x ] **Exclusão de Tarefas:** Permite excluir uma tarefa com base no seu ID.
- [ x ] **Campos Requeridos:** As tarefas devem conter pelo menos um título e um status, que podem ser "pendente", "em andamento" ou "concluída".
- [ x ] **Armazenamento Local:** Utiliza um banco de dados local para armazenar as tarefas de forma persistente.

## Dependencias
- **fastAPI**
- **sqlalchemy**

## Comandos
- **Inicializar Projeto:** python -m uvicorn main:app --reload 
