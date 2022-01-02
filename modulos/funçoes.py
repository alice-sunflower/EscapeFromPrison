def leiaInt(msg):
    while True:
        try:
            mensagem = int(input(msg))
        except:
            print('Erro. Digite um número INTEIRO entre 1 e 2.')
        if mensagem > 2:
            print('Erro. Digite um número que seja 1 ou 2 equivalente à opção desejada.')
        elif mensagem < 1:
            print('Erro. Digite um número que seja 1 ou 2 equivalente à opção desejada. ')    
        else:
            return mensagem


def introducao_1():
    input('''Você jogará como um prisioneiro que se chama Jack...''')

    input('Um prisioneiro que anda fazendo planos de fuga há alguns meses...')

    input('No dia 01/01/2022 você resolve colocar um desses planos em prática...')

    input('Portanto, terá que escolher bem qual será ele para que sua fuga seja um sucesso...')


def introducao_2():
    input('Agora são 20:00 horas de um dia antes da sua fuga e você ainda se encontra indeciso sobre qual plano usar para fugir...')

    input('''Atrás de você existe um pôster roxo de um show de um cantor chamado Enygma pregado na parede pálida e rígida da prisão.
Ao seu lado direito se encontra uma cama de metal com uma colcha fina e suja sem travesseiro e nem cobertor e no outro uma privada de metal vazia
ao lado de um pequeno banco de madeira.
Já do lado de fora da sua cela você consegue enxergar guardas deixando de patrulhar que comentam sobre irem num show que terá no final da noite até
o amanhecer.''')


def escolha_2():
    input('Você se dirige em direção da privada e pega a chave de fenda... ')
    input('Você pega ela juntamente do banco... ')
    input('Usando ele para subir na tubulação você usa a ferramenta com sucesso e se encontra dentro dela. ')
    input('Andando um pouco você se encontra numa situação delicada... ')
    input('Um lado para a direita e outro para a esquerda... ')


def gameover1():
    input('Você pega a picareta, apesar de pesada e volta para a cela.')
    input('Um guarda passa por ali, vê você com a picareta na mão e te manda para a solitária.')
    print('GAME OVER')


def gameover2():
    input('Você pega a chave de fenda e se levanta... ')
    input('Um guarda começa a passar por ali e te vê agindo de maneira suspeita...')
    input('Ele vê a chave de fenda na sua mão e você é levado para a solitária. ')
    print('GAME OVER')


def gameover3():
    input('Você começa a avançar em direção à profundidade do buraco... ')
    input('Chegando no final dele você se vê em um túnel largo com algumas lâmpadas roubadas de salas da prisão... ')
    input('Avançando ainda mais você encontra a região onde você poderá finalmente fugir... ')
    input('Mas... Espera! Você não consegue quebrar a região acima de você porque não possui as ferramentas necessárias!')
    input('Você então começa a voltar em direção onde deixou sua picareta... ')
    input('Agora você voltou para o túnel e está indo em direção ao mesmo local... ')
    input('Quebrando o teto acima de você, você está no lado de fora da prisão! ')
    input('Mas infelizmente haviam guardas fazendo a ronda por ali e você foi pego... ')
    print('GAME OVER')


def gameover4():
    input('Você continua a caminhar... ')
    input('Após cerca de 2 horas indo pela tubulação você não encontrada nada... ')
    input('Ao perceber isso você começa a voltar imediatamente para ir pelo lado esquerdo... ')
    input('Após mais 2 horas de caminhada você finalmente encontra uma saída... ')
    input('Ao chutar o ventilador você se encontra do lado de fora da prisão! ')
    input('Mas infelizmente haviam guardas fazendo a ronda por ali e você foi pego... ')
    print('GAME OVER')


def vitoria1():
    input('Você pega a picareta e começa a avançar em direção à profundidade do buraco... ')
    input('Chegando no final dele você se vê em um túnel largo com algumas lâmpadas roubadas de salas da prisão... ')
    input('Avançando ainda mais você encontra a região onde você poderá finalmente fugir... ')
    input('Quebrando o teto acima de você, você está no lado de fora da prisão! ')
    input('Parabéns!! Você finalizou o jogo com sucesso! ')


def vitoria2():
    input('Você continua a caminhar... ')
    input('Após cerca de 2 horas indo pela tubulação você finalmente encontra uma saída... ')
    input('Ao chegar lá você chuta o ventilador para abrir caminho e se encontra do lado de fora da prisão. ')
    input('Parabéns!! Você finalizou o jogo com sucesso! ')