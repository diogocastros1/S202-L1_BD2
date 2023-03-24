from database import Database
from writeAJson import writeAJson
from productAnalyzer import ProductAnalyzer
from database import Collection


db = Database(database="mercado", collection="compras")
pa = ProductAnalyzer(collection=db.collection)

# db.resetDatabase()

# 1.Média de gasto total:
# result = db.collection.aggregate([
#     {"$unwind": "$produtos"},
#     {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
#     {"$group": {"_id": None, "media": {"$avg": "$total"}}}
# ])

# # writeAJson(result, "Média de gasto total")

# # # Cliente que mais comprou em cada dia:
# result = db.collection.aggregate([
#     {"$unwind": "$produtos"},
#     {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
#     {"$sort": {"_id.data": 1, "total": -1}},
#     {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}}
# ])

# writeAJson(result, "Cliente que mais comprou em cada dia")

# # # Produto mais vendido:
# result = db.collection.aggregate([
#     {"$unwind": "$produtos"},
#     {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
#     {"$sort": {"total": -1}},
#     {"$limit": 1}
# ])

# writeAJson(result, "Produto mais vendido")

# # Retorna o produto mais vendido em todas as compras
# most_sold = pa.most_sold_product()
# print(most_sold)

# # Encontra o cliente que mais gastou em uma única compra
# max_purchase_customer = pa.customer_max_purchase()
# print(max_purchase_customer)

# # Lista todos os produtos que tiveram uma quantidade vendida acima de 1 unidades
# sold_above_one = pa.products_sold_above_one()
# print(sold_above_one)


tv = pa.total_vendas()
writeAJson(tv, "Total de Vendas")

pmv = pa.produto_mais_vendido()
writeAJson(pmv, "Produto Mais vendido 2")

cmg = pa.cliente_mais_gastou()
writeAJson(cmg, "Cliente que mais gastou")

padu = pa.produtos_acima_de_uma(1)
writeAJson(padu, "Produtos com ao menos uma venda")

