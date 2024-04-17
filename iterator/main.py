from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any

class Produto:
    def __init__(self, nome: str, categoria: str, valor: float) -> None:
        self.nome = nome
        self.categoria = categoria
        self.valor = valor

class ProdutoIterator(Iterator):
    def __init__(self, collection: ProdutosCollection) -> None:
        self._collection = collection
        self._categoria_index = 0
        self._valor_index = 0

    def __next__(self) -> Produto:
        try:
            category = self._collection.categories[self._categoria_index]
            products_in_category = self._collection.products_by_category[category]

            if self._valor_index >= len(products_in_category):
                self._valor_index = 0
                self._categoria_index += 1
                return next(self)

            sorted_products = sorted(products_in_category, key=lambda x: x.valor)
            product = sorted_products[self._valor_index]
            self._valor_index += 1
            return product
        except IndexError:
            raise StopIteration()

class ProdutosCollection(Iterable):
    def __init__(self) -> None:
        self.products_by_category = {}
        self.categories = []

    def add_product(self, produto: Produto) -> None:
        if produto.categoria not in self.products_by_category:
            self.products_by_category[produto.categoria] = []
            self.categories.append(produto.categoria)
        self.products_by_category[produto.categoria].append(produto)

    def __iter__(self) -> ProdutoIterator:
        return ProdutoIterator(self)

if __name__ == "__main__":
    # Criando alguns produtos
    produto1 = Produto("A Morte de Ivan Ilitch - Liev Tolstói", "literatura russa", 10.00)
    produto2 = Produto("Dom Casmurro - Machado de Assis", "literatura brasileira", 20.00)
    produto3 = Produto("Almas Mortas - Nikolai Gogol", "literatura russa", 20.00)
    produto4 = Produto("Sonho de Uma Noite de Verão - William Shakespeare", "literatura britânica", 5.00)
    produto5 = Produto("Irmãos Karamázov - Fiódor Dostoiévski", "literatura russa", 25.00)
    produto6 = Produto("Seminário dos Ratos - Lygia Fagundes Teles", "literatura brasileira", 15.00)
    produto7 = Produto("Paraíso Perdido - John Milton", "literatura britânica", 30.00)
    produto8 = Produto("A Dama de Espadas - Aleksandr Púshkin", "literatura russa", 10.00)
    produto9 = Produto("Sobre o Que Não Falamos - Ana Cristina Braga Martes", "literatura brasileira", 15.00)
    produto10 = Produto("Frankenstein - Mary Shelley", "literatura britânica", 10.00)

    # Criando a coleção de produtos
    colecao_produtos = ProdutosCollection()
    colecao_produtos.add_product(produto1)
    colecao_produtos.add_product(produto2)
    colecao_produtos.add_product(produto3)
    colecao_produtos.add_product(produto4)
    colecao_produtos.add_product(produto5)
    colecao_produtos.add_product(produto6)
    colecao_produtos.add_product(produto7)
    colecao_produtos.add_product(produto8)
    colecao_produtos.add_product(produto9)
    colecao_produtos.add_product(produto10)

    a = True

    print("="*60)
    print("Boas vindas ao sebo da melhor literatura da cidade!\nHoje trago esses livros para você:")
    print("="*60)

    for produto in colecao_produtos:
        print(f"\033[33mLivro\033[m: {produto.nome}, \033[34mCategoria\033[m: {produto.categoria}, \033[35mValor\033[m: R${produto.valor}\n")
