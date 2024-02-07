from datetime import date

class Usuario:
    usuarios = []

    def __init__(self, nome: str, email: str, dataNascimento: date, quantidadePontos: int):
        self.nome = nome
        self.__email = email
        self.__dataNascimento = dataNascimento
        self.__quantidadePontos = quantidadePontos
        Usuario.usuarios.append(self)

    @property
    def email(self):
        return self.__email

    @property
    def dataNascimento(self):
        return self.__dataNascimento

    @property
    def quantidadePontos(self):
        return self.__quantidadePontos

    def __str__(self):
        return f"Nome: {self.nome}, Email: {self.__email}, Data de Nascimento: {self.__dataNascimento}, Pontos: {self.__quantidadePontos}"

    def adicionarPontos(self, pontos):
        self.__quantidadePontos += pontos

    def retirarPontos(self, pontos):
        self.__quantidadePontos -= pontos

    def adicionar_avaliacao(self, avaliacoes_obj, usuario_negocio, nota: int, texto: str):
        avaliacoes_obj.adicionar_avaliacao(self.nome, usuario_negocio, nota, texto)


class Avaliacoes:
    avaliacoes = []

    def adicionar_avaliacao(self, usuario_nome, usuario_negocio, nota: int, texto: str):
        avaliacao = {
            'Usuário': usuario_nome,
            'Negócio': usuario_negocio._nomeFantasia,
            'Nota': nota,
            'Avaliação': texto
        }
        self.avaliacoes.append(avaliacao)

    def mostrar_avaliacao(self, usuario_nome):
        avaliacoes_usuario = [avaliacao for avaliacao in self.avaliacoes if avaliacao['Usuário'] == usuario_nome]
        if not avaliacoes_usuario:
            print(f"O usuário {usuario_nome} não tem avaliações.")
        else:
            print(f"Avaliações do usuário {usuario_nome}:")
            for avaliacao in avaliacoes_usuario:
                print(f"Negócio: {avaliacao['Negócio']}")
                print(f"Nota: {avaliacao['Nota']}\nAvaliação: {avaliacao['Avaliação']}")

class Usuario_negocio:
    negocios = []

    def __init__(self, nomeFantasia: str, endereco: str, areaAtuacao: str, telefone: int,
                 site: str, horarioFuncionamento: int, faixaPreco: float, imagem: str):
        self._nomeFantasia = nomeFantasia
        self._endereco = endereco
        self._areaAtuacao = areaAtuacao
        self._telefone = telefone
        self._site = site
        self._horarioFuncionamento = horarioFuncionamento
        self._faixaPreco = faixaPreco
        self.imagem = imagem
        self.promocoes = []
        self.avaliacoes_negocio = Avaliacoes()
        Usuario_negocio.negocios.append(self)

    def set_nomeFantasia(self, nomeFantasia):
        self._nomeFantasia = nomeFantasia

    def set_endereco(self, endereco):
        self._endereco = endereco

    def set_quantidadeNegocio(self, quantidadeNegocio):
        self._quantidadeNegocio = quantidadeNegocio

    def set_areaAtuacao(self, areaAtuacao):
        self._areaAtuacao = areaAtuacao

    def set_telefone(self, telefone):
        self._telefone = telefone

    def set_site(self, site):
        self._site = site

    def set_horarioFuncionamento(self, horarioFuncionamento):
        self._horarioFuncionamento = horarioFuncionamento

    def set_faixaPreco(self, faixaPreco):
        self._faixaPreco = faixaPreco

    def set_imagem(self, imagem):
        self._imagem = imagem

    def criar_promocao(self):
        promocao = Promocoes()
        desconto = float(input("Informe o desconto da promoção: "))
        produto = input("Informe o produto da promoção: ")
        descricao = input("Informe a descrição da promoção: ")
        dataInicio = input("Informe a data de início da promoção (no formato YYYY-MM-DD): ")
        dataFim = input("Informe a data de término da promoção (no formato YYYY-MM-DD): ")

        promocao.entrarDesconto(desconto)
        promocao.entrarProduto(produto)
        promocao.entrarDescricao(descricao)
        promocao.entrarDataInicio(date.fromisoformat(dataInicio))
        promocao.entrarDataFim(date.fromisoformat(dataFim))

        self.promocoes.append(promocao)
        print("Promoção criada com sucesso!")

    def mostrar_promocoes(self):
        if not self.promocoes:
            print("Este negócio não possui promoções.")
        else:
            print("Promoções deste negócio:")
            for i, promocao in enumerate(self.promocoes, 1):
                print(f"Promoção {i}:")
                print(f"Desconto: {promocao.desconto}%")
                print(f"Produto: {promocao.produto}")
                print(f"Descrição: {promocao.descricao}")
                print(f"Data de Início: {promocao.dataInicio}")
                print(f"Data de Término: {promocao.dataFim}")
                print("\n")

class Promocoes:
    def __init__(self):
        self.promocoes = []

    def entrarDesconto(self, desconto):
        self.desconto = desconto

    def entrarProduto(self, produto):
        self.produto = produto

    def entrarDescricao(self, descricao):
        self.descricao = descricao

    def entrarDataInicio(self, dataInicio):
        self.dataInicio = dataInicio

    def entrarDataFim(self, dataFim):
        self.dataFim = dataFim

class Atracoes:
    def __init__(self, descricao: str, dataInicio: date, dataFim: date, horarioFuncionamento: str, preco: float, classificacao: str, localizacao: str):
        self.descricao = descricao
        self.dataInicio = dataInicio
        self.dataFim = dataFim
        self.horarioFuncionamento = horarioFuncionamento
        self.preco = preco
        self.classificacao = classificacao
        self.localizacao = localizacao

class ItemCardapio:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getPreco(self):
        return self.preco

    def setPreco(self, preco):
        self.preco = preco

class Cardapio:
    def __init__(self):
        self.itens = []

    def adicionarItem(self, item):
        self.itens.append(item)

    def removerItem(self, item):
        if item in self.itens:
            self.itens.remove(item)
        else:
            print(f"{item.getNome()} não encontrado no cardápio.")

    def exibirCardapio(self):
        print("Cardápio:")
        for item in self.itens:
            print(f"{item.getNome()} - R${item.getPreco():.2f}")

class Cinema(Usuario_negocio):
    def __init__(self, idSessao: int, idSala: int, idFilme: str):
        self.idSessao = idSessao
        self.idSala = idSala
        self.idFilme = idFilme

class Sala(Cinema):
    salas = []

    def __init__(self, idSala, numero_nome: str, capacidade: int, doisD: bool, tresD: bool):
        self.__idSala = idSala
        self._numero_nome = numero_nome
        self._capacidade = capacidade
        self._doisD = doisD
        self._tresD = tresD
        Sala.salas.append(self)

    @property
    def idSala(self):
        return self.__idSala

    def set_numero_nome(self, numero_nome):
        self._numero_nome = numero_nome

    def set_capacidade(self, capacidade):
        self._capacidade = capacidade

    def set_doisD(self, doisD):
        self._doisD = doisD

    def set_tresD(self, tresD):
        self._tresD = tresD

    def __str__(self):
        return f"Sala {self._numero_nome} (ID: {self.idSala}) - Capacidade: {self._capacidade}, 2D: {self._doisD}, 3D: {self._tresD}"

class Sessao:
    def __init__(self, idSessao, data: date, horarioInicio: str, horarioFim: str, valor: float, dublado: bool, legendado: bool):
        self.idSessao = idSessao
        self.data = data
        self.horarioInicio = horarioInicio
        self.horarioFim = horarioFim
        self.valor = valor
        self.dublado = dublado
        self.legendado = legendado

class Filme:
    def __init__(self, nome: str, genero: str, diretor: str, estudio: str, faixaEtaria: str, duracao: str, sinopse: str, avaliacao: float):
        self.nome = nome
        self.genero = genero
        self.diretor = diretor
        self.estudio = estudio
        self.faixaEtaria = faixaEtaria
        self.duracao = duracao
        self.sinopse = sinopse
        self.avaliacao = avaliacao
        self.sala_associada = None

class Negocio_alimentacao(Usuario_negocio):
    def __init__(self, nomeFantasia: str, endereco: str, quantidadeNegocio: int, areaAtuacao: str, telefone: int, site: str, horarioFuncionamento: int, faixaPreco: float, avaliacao: float, imagem, tipo: str, estiloMusical: str, tipoCulinaria: str, valorEntrada: float):
        super().__init__(nomeFantasia, endereco, quantidadeNegocio, areaAtuacao, telefone, site, horarioFuncionamento, faixaPreco, avaliacao, imagem)
        self.tipo = tipo
        self.estiloMusical = estiloMusical
        self.tipoCulinaria = tipoCulinaria
        self.valorEntrada = valorEntrada

    def set_tipo(self, tipo):
        self.tipo = tipo

    def set_estiloMusical(self, estiloMusical):
        self.estiloMusical = estiloMusical

    def set_tipoCulinaria(self, tipoCulinaria):
        self.tipoCulinaria = tipoCulinaria

    def set_valorEntrada(self, valorEntrada):
        self.valorEntrada= valorEntrada

class Ponto_turistico(Usuario_negocio):
    def __init__(self, nomeFantasia: str, endereco: str, quantidadeNegocio: int, areaAtuacao: str, telefone: int, site: str, horarioFuncionamento: int, faixaPreco: float, avaliacao: float, imagem: str, tipo: str, descricao: str, valorIngresso: float):
        super().__init__(nomeFantasia, endereco, quantidadeNegocio, areaAtuacao, telefone, site, horarioFuncionamento, faixaPreco, avaliacao, imagem)
        self.tipo = tipo
        self.descricao = descricao
        self.valorIngresso = valorIngresso

    def set_tipo(self, tipo):
        self.tipo = tipo

    def set_descricao(self, descricao):
        self.descricao = descricao

    def set_valorIngresso(self, valorIngresso):
        self.valorIngresso = valorIngresso

class Loja(Usuario_negocio):
    def __init__(self, nomeFantasia: str, endereco: str, quantidadeNegocio: int, areaAtuacao: str, telefone: int, site: str, horarioFuncionamento: int, faixaPreco: float, avaliacao: float, imagem: str, categoria: str):
        super().__init__(nomeFantasia, endereco, quantidadeNegocio, areaAtuacao, telefone, site, horarioFuncionamento, faixaPreco, avaliacao, imagem)
        self.categoria = categoria

    def set_categoria(self, categoria):
        self.categoria = categoria