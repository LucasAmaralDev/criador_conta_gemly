import random

nome = ['Joao', 'Maria', 'Jose', 'Ana', 'Pedro', 'Paulo', 'Carlos', 'Lucas', 'Luiz', 'Luiza', 'Julia',  'Miguel', 'Mateus', 'Matheus', 'Gabriel', 'Gustavo', 'Guilherme', 'Rafael', 'Rafaele', 'Rafaela', 'Rafaeli', 'Rafaelly', 'Rafaelle']
sobrenome = ['Silva', 'Santos', 'Oliveira', 'Souza', 'Rodrigues', 'Alves', 'Lima', 'Gomes', 'Ferreira', 'Pereira', 'Ribeiro', 'Carvalho', 'Costa', 'Almeida', 'Martins', 'Araujo', 'Moura', 'Monteiro', 'Barros', 'Correia', 'Nascimento', 'Pinto', 'Cavalcanti', 'Dias', 'Castro', 'Campos', 'Cardoso', 'Melo', 'Brito', 'Nunes', 'Schmidt', 'Schmitz', 'Schmitt', 'Schmit', 'Schmiedt', 'Schmied', 'Schmiedz', 'Schmieds']
abreviacao_estado = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PR', 'PB', 'PA', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SE', 'SP', 'TO']


def gerarUserame():
    selecionarNome = random.choice(nome)
    selecionarSobrenome = random.choice(sobrenome)
    selecionarAbreviacaoEstado = random.choice(abreviacao_estado)
    numeroAleatorio = random.randint(100, 999)

    username = selecionarNome + selecionarSobrenome + selecionarAbreviacaoEstado + str(numeroAleatorio)

    return username.lower()