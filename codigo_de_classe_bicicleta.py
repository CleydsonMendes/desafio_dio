# --- DEFINIÇÃO DA CLASSE ---
# Uma 'classe' é como um molde para criar objetos. 
# Ela define quais características (atributos) e ações (métodos) 
# os objetos terão.
class Bicicleta:
    # O método __init__ é o "construtor". Ele é chamado automaticamente
    # ao criar um novo objeto para definir seus atributos iniciais.
    def __init__(self, cor, modelo, ano, valor):
        # Atributos são as variáveis que pertencem a cada objeto (instância).
        self.cor = cor
        self.modelo = modelo
        self.ano = ano 
        self.valor = valor

    # --- MÉTODOS DE AÇÃO (COMPORTAMENTOS) ---
    # Métodos definem o que um objeto da classe pode fazer.

    def buzinar(self):
        """Simula a ação de buzinar."""
        print('Plim plim...')

    def parar(self):
        """Simula a ação de parar a bicicleta."""
        print('Parando bicicleta...')
        print('Bicicleta parada!')

    def correr(self):
        """Simula a ação de correr com a bicicleta."""
        print('Vrummmmm...')

    # --- MÉTODO DE REPRESENTAÇÃO EM STRING ---
    # O método especial __str__ define o que será exibido quando você
    # tenta "imprimir" o objeto (ex: usando print(b2)).
    # Ele deve retornar uma string.

    # Você definiu o método __str__ duas vezes. Em Python, a última
    # definição de uma função ou método é a que vale. Portanto, a primeira
    # será ignorada e a segunda será usada pelo programa.
    # Deixei as duas aqui para fins de estudo.

    # Primeira forma de fazer: Manual
    # Prós: Simples e direto de entender.
    # Contras: Se você adicionar ou remover um atributo da classe (no __init__),
    # você PRECISA lembrar de atualizar esta linha manualmente.
    # def __str__(self):
    #     return f'Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}'

    # Segunda forma de fazer: Dinâmica (esta é a que será usada)
    # Prós: É "à prova de futuro". Se você adicionar/remover atributos no __init__,
    # esta função se adapta automaticamente, sem precisar de manutenção.
    # Contras: Um pouco mais complexa de ler no início.
    def __str__(self):
        # self.__class__.__name__: Pega o nome da classe do objeto ("Bicicleta").
        # self.__dict__.items(): Pega todos os atributos do objeto e seus valores
        #                        e os transforma em uma lista de pares (chave, valor).
        # ", ".join([...]): Pega cada par (chave, valor) e formata como "chave = valor",
        #                    depois junta tudo em uma única string, separada por vírgula.
        return f'{self.__class__.__name__}: {", ".join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}'

# --- CRIAÇÃO E USO DOS OBJETOS (INSTÂNCIAS) ---

# Criando o primeiro objeto, 'b1'.
b1 = Bicicleta('vermelha', 'caloi', 2022, 600)
b1.buzinar()
b1.parar()
b1.correr()

# Criando o segundo objeto, 'b2'.
b2 = Bicicleta('verde', 'monark', 2000, 189)

# Ao usar print() em um objeto, o Python automaticamente chama o método __str__
# que você definiu para obter a representação em string do objeto.
print("\n--- Exibindo o objeto b2 usando print() ---")
print(b2) # Isso vai executar o segundo método __str__

print("\n--- Outras ações e acesso a atributos ---")
Bicicleta.buzinar(b2)
b2.buzinar()

# Acessando os atributos individuais de cada objeto.
print(b1.cor, b1.modelo, b1.ano, b1.valor)
print(b2.cor) # Isso acessa o atributo de instância 'cor' do objeto 'b2'.
