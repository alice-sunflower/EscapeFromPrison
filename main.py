#Importar "LEIAINT" para ler um número inteiro dentro das condições específicas
from modulos.funçoes import *

#Espaço das variáveis
escolhas = []

#Introdução ao jogo
introducao_1()

#Dia 31/12/2021 - analisar a situação e decidir o melhor plano para fugir
introducao_2()

#Primeira escolha - analisar o local desejado
escolhendo = True
while escolhendo:
    #Encontrar as ferramentas necessárias para a fuga
    escolha_1 = leiaInt('''[1] Olhar atrás do pôster
[2] Olhar dentro da privada
    --> ''')
    if escolha_1 == 1:
        while escolhendo:
            input('''Se aproximando da parede você puxa suavemente o pôster da parede e percebe que atrás dele tem um buraco profundo que leva aos
poucos ao subterrâneo. Dentro dele você consegue ver a picareta que você usou para escavar esse buraco por meses. ''')
            escolha_1_2 = leiaInt('''[1] Pegar picareta
[2] Voltar para a cela
    --> ''')
            #Escolha do GAME OVER 1
            if escolha_1_2 == 1:
                gameover1()
                escolhendo = False
            #Escolha da continuidade
            elif escolha_1_2 == 2:
                input('Você escolhe deixar a picareta pesada por ali até a hora planejada... ')
                escolhas.append('1')
                break
    elif escolha_1 == 2:
        input('''Colocando a mão na privada você sente que ao fundo dela existe um objeto metálico que você imediatamente reconhece como sendo a 
chave de fenda que você deixou ali para escapar pela tubulação, caso fosse necessário. ''')
        while escolhendo:
            escolha_1_2 = leiaInt('''[1] Pegar a chave de fenda
[2] Deixar ela ali
    --> ''')
            #ESCOLHA DO GAME OVER 2
            if escolha_1_2 == 1:
                gameover2()
                escolhendo = False
            #ESCOLHA DA CONTINUIDADE
            elif escolha_1_2 == 2:
                input('Você escolhe deixar a chave de fenda por ali até a hora planejada... ')
                escolhas.append('2')
                break
    #Condição de que se as 2 escolhas já tiverem sido feitas ele vai avançar na história
    if len(escolhas) == 2:
        input('Após esperar por algumas horas você se encontra na madrugada, pronto para fugir. ')
        escolhas_2 = leiaInt('''Por onde deseja fugir?
[1] Buraco atrás do pôster
[2] Tubulação da cela 
    --> ''')
        #Escolha do BURACO
        if escolhas_2 == 1:
            input('Você retira o pôster lentamente da parede com cautela para não deixar claro sua passagem... ')
            input('Na sua frente se encontra o profundo buraco e a picareta.')
            #LOOP DA ESCOLHA
            escolhendo = True
            while escolhendo:
                escolhas_2_1 = leiaInt('''[1] Pegar picareta
[2] Deixar ela ali
    --> ''')
                #ESCOLHA DA VITÓRIA
                if escolhas_2_1 == 1:
                    vitoria1()
                    escolhendo = False
                #ESCOLHA DO GAME OVER 3
                elif escolhas_2_1 == 2:
                    gameover3()
                    escolhendo = False
        #Escolha da TUBULAÇÃO
        elif escolhas_2 == 2:
            escolha_2()       
            #LOOP DA ESCOLHA
            escolhendo = True
            while escolhendo:
                escolhas_2_1 = leiaInt('''[1] Ir pela esquerda
[2] Ir pela direita
    --> ''')
                #IR PELA ESQUERDA
                if escolhas_2_1 == 1:
                    vitoria2()
                    escolhendo = False
                #IR PELA DIREITA
                elif escolhas_2_1 == 2:
                    gameover4()
                    escolhendo = False
