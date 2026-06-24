import random  # usado pra gerar itens aleatorios


# classe do item


class Item:
    def __init__(self, nome, tipo, raridade):
        self.nome = nome        # nome do item
        self.tipo = tipo        # tipo do item
        self.raridade = raridade  # chave da arvore



# no da arvore


class No:
    def __init__(self, item):
        self.item = item
        self.esq = None
        self.dir = None



# arvore binaria de busca


class ArvoreBST:
    def __init__(self):
        self.raiz = None

    # inserir item
    def inserir(self, raiz, item):
        if raiz is None:
            return No(item)

        if item.raridade < raiz.item.raridade:
            raiz.esq = self.inserir(raiz.esq, item)
        else:
            raiz.dir = self.inserir(raiz.dir, item)

        return raiz

    # buscar item
    def buscar(self, raiz, raridade):
        if raiz is None or raiz.item.raridade == raridade:
            return raiz

        if raridade < raiz.item.raridade:
            return self.buscar(raiz.esq, raridade)
        else:
            return self.buscar(raiz.dir, raridade)

    # pegar menor valor (pra remoção)
    def menor_valor(self, no):
        atual = no
        while atual.esq is not None:
            atual = atual.esq
        return atual

    # remover item
    def remover(self, raiz, raridade):
        if raiz is None:
            return raiz

        if raridade < raiz.item.raridade:
            raiz.esq = self.remover(raiz.esq, raridade)

        elif raridade > raiz.item.raridade:
            raiz.dir = self.remover(raiz.dir, raridade)

        else:
            # achou o item

            # sem filhos
            if raiz.esq is None and raiz.dir is None:
                return None

            # um filho
            if raiz.esq is None:
                return raiz.dir
            elif raiz.dir is None:
                return raiz.esq

            # dois filhos
            temp = self.menor_valor(raiz.dir)
            raiz.item = temp.item
            raiz.dir = self.remover(raiz.dir, temp.item.raridade)

        return raiz

    # mostrar inventario em ordem
    def em_ordem(self, raiz):
        if raiz:
            self.em_ordem(raiz.esq)
            print(f"{raiz.item.nome} ({raiz.item.tipo}) - raridade {raiz.item.raridade}")
            self.em_ordem(raiz.dir)

    # maior item
    def maior(self, raiz):
        atual = raiz
        while atual and atual.dir:
            atual = atual.dir
        return atual

    # menor item
    def menor(self, raiz):
        atual = raiz
        while atual and atual.esq:
            atual = atual.esq
        return atual



# gerador de item


def gerar_item():
    # aqui cada tipo tem seus itens certos
    itens = {
        "Arma": ["Espada", "Arco", "Machado"],
        "Poção": ["Poção de Cura", "Poção de Mana"],
        "Equipamento": ["Escudo", "Armadura"]
    }

    # escolhe o tipo primeiro
    tipo = random.choice(list(itens.keys()))

    # depois escolhe um item daquele tipo
    nome = random.choice(itens[tipo])

    # raridade aleatoria
    raridade = random.randint(1, 100)

    return Item(nome, tipo, raridade)



# menu do jogo


def menu():
    print("\n---- MINI RPG ----")
    print("1 - Explorar (achar item)")
    print("2 - Usar item")
    print("3 - Buscar item")
    print("4 - Mostrar inventario")
    print("5 - Item mais raro")
    print("6 - Item mais fraco")
    print("0 - Sair")



# programa principal


arvore = ArvoreBST()

while True:
    menu()
    op = input("Escolha: ")

    # explorar
    if op == "1":
        item = gerar_item()

        arvore.raiz = arvore.inserir(arvore.raiz, item)

        print("\n voce encontrou um item!")
        print(f"{item.nome} ({item.tipo}) - raridade {item.raridade}")

    # remover
    elif op == "2":
        raridade = int(input("Raridade do item: "))

        arvore.raiz = arvore.remover(arvore.raiz, raridade)

        print("item usado e removido")

    # buscar
    elif op == "3":
        raridade = int(input("Raridade: "))

        resultado = arvore.buscar(arvore.raiz, raridade)

        if resultado:
            print("item encontrado:", resultado.item.nome)
        else:
            print("nao achei o item")

    # inventario
    elif op == "4":
        print("\ninventario:")
        arvore.em_ordem(arvore.raiz)

    # mais raro
    elif op == "5":
        maior = arvore.maior(arvore.raiz)
        if maior:
            print("mais raro:", maior.item.nome)

    # mais fraco
    elif op == "6":
        menor = arvore.menor(arvore.raiz)
        if menor:
            print("mais fraco:", menor.item.nome)

    # sair
    elif op == "0":
        print("saindo do jogo...")
        break

    else:
        print("opcao invalida")