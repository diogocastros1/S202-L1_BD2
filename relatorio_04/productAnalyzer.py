from pymongo import MongoClient
from database import Database

class ProductAnalyzer:
  
    def __init__(self, collection):
        self.collection = collection
        
    def total_vendas(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$data_compra",  "total_vendas": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"_id": 1}}
        ]
        return list(self.collection.aggregate(pipeline))
        
    def produto_mais_vendido(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "quantidade_vendida": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"quantidade_vendida": -1}}
        ]
        return list(self.collection.aggregate(pipeline))

    def cliente_mais_gastou(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total_gasto": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$lookup": {"from": "clientes", "localField": "_id", "foreignField": "cliente_id", "as": "cliente"}},
            {"$unwind": "$cliente"},
            {"$project": {"cliente_id": "$cliente.cliente_id", "nome": "$cliente.nome", "total_gasto": 1}},
            # {"$sort": {"total_gasto": -1}}
        ]
        return list(self.collection.aggregate(pipeline))
    
    def produtos_acima_de_uma(self, qtd):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$match": {"produtos.quantidade": {"$gt": qtd}}},
            {"$group": {"_id": "$produtos.descricao"}},
            {"$sort": {"_id": 1}}
        ]
        return list(self.collection.aggregate(pipeline))
     
