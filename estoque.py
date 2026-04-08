import pyodbc
import pandas as pd

# Conexão com o SQL Server
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=BRUNO\\SQLEXPRESS;'
    'DATABASE=Bd_ESTOQUE;'
    'Trusted_Connection=yes;'
)

print("Conexão realizada com sucesso! ✅")

# Lendo os produtos do banco
query = """
    SELECT 
        p.nome AS Produto,
        c.nome AS Categoria,
        f.nome AS Fornecedor,
        p.preco_unitario AS Preco,
        p.quantidade_estoque AS Estoque,
        p.estoque_minimo AS Minimo
    FROM Produtos p
    INNER JOIN Categorias c ON p.id_categoria = c.id_categoria
    INNER JOIN Fornecedores f ON p.id_fornecedor = f.id_fornecedor
"""

df = pd.read_sql(query, conn)

print("\n📦 Todos os Produtos:")
print(df.to_string(index=False))

print("\n⚠️ Produtos com Estoque Abaixo do Mínimo:")
abaixo = df[df['Estoque'] <= df['Minimo']]
print(abaixo.to_string(index=False))

conn.close()