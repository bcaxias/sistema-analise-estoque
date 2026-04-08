# 📦 Sistema de Análise de Estoque

Projeto integrado desenvolvido para praticar conceitos de Banco de Dados, Python e Business Intelligence.

## 🛠️ Tecnologias Utilizadas

- **SQL Server** — Modelagem e armazenamento dos dados
- **Python** — Análise de dados e geração de relatórios
- **Pandas** — Manipulação dos dados
- **openpyxl** — Geração do relatório em Excel
- **Power BI** — Dashboard visual interativo

## 📁 Estrutura do Projeto
sistema-analise-estoque/
│
├── estoque.py        # Conexão com banco e análise de dados
├── relatorio.py      # Geração automática do relatório Excel
├── README.md         # Documentação do projeto

## 🗄️ Banco de Dados

O banco foi modelado no SQL Server com as seguintes tabelas:

- **Categorias** — Categorias dos produtos
- **Fornecedores** — Cadastro de fornecedores
- **Produtos** — Cadastro de produtos com estoque mínimo
- **Movimentações** — Entradas e saídas do estoque

## ⚙️ Como Executar

1. Clone o repositório
2. Instale as dependências:
```bash
pip install pyodbc pandas sqlalchemy openpyxl
```
3. Configure a conexão no `estoque.py` com o nome do seu servidor SQL Server
4. Execute o script de análise:
```bash
python estoque.py
```
5. Para gerar o relatório Excel:
```bash
python relatorio.py
```

## 📊 Funcionalidades

- ✅ Listagem completa de produtos com categoria e fornecedor
- ✅ Alerta automático de produtos abaixo do estoque mínimo
- ✅ Relatório Excel gerado automaticamente com formatação colorida
- ✅ Dashboard no Power BI com gráficos de estoque por produto e categoria

## 📈 Dashboard Power BI

O dashboard contém:
- Gráfico de barras — Estoque por Produto
- Gráfico de pizza — Estoque por Categoria
- Tabela de alertas — Produtos que precisam de reposição

## 👨‍💻 Autor

**Bruno Caxias**
Estudante de Sistemas de Informação — Unifafibe
[LinkedIn](https://www.linkedin.com/in/bruno-caxias-a68552258)