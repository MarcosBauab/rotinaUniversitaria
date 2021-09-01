import random
import time
import re

"""save = 0
j = open("salvar.txt","r")
teste = j.readline()
if teste == "1\n":
    save = 1
elif teste == '2\n':
    save = 2
"""

habilidades = {'alegria': 5, 'energia': 5, 'esportes': 5, 'amizades': 5, 'organizacao': 5, 'saude': 5}
inventario = {'Dinheiro': 15, 'Itens': [], 'Comidas': []}
lista = ['Bola - 20 reais', 'Halter - 20 reais','Hot Pocket - 20 reais', 'Miojo - 15 reais', 'Espaghetti pupunha ao molho pesto - 60 reais', 'Tilápia, arroz e brócolis - 50 reais']
ifood = ['Pizza', 'Hamburgão', 'Caldinho', 'Poke']


#Game Over
def gameOver():
    print('Poxa, você não conseguiu concluir sua Rotina Universitária, que pena 😓')
    decisao = input("Tá afim de começar de novo (S/N)? ")
    while decisao.lower() != 's' and decisao.lower() != 'n':
        decisao = input("Tá afim de começar de novo (S/N)? ")
    if decisao.lower() == 's':
        manha()
    elif decisao.lower() == 'n':
        print('Poxa, que triste que você não quer jogar mais!\n'
              'Mas infelizmente, não ligamos, e você continuará a jogar...')
        print()
        print("\033[1;97;40mR O T I N A :\033[97;40;0m")
        print()
        print("Manhã : \n"
              "Café da manhã com a família - 7h \n"
              "Aula de cálculo - 8h até 10h \n"
              "Freela blogueiro - 10h até 11h \n"
              "Ir no mercado - 11h \n"
              "Almoço - 12h \n"
              "Adiantar os quizzes")
        time.sleep(4)
        print('------------------------------------------------------------------------')
        print("KKKKK, brincadeira, tchau!")
        print('------------------------------------------------------------------------')
        print("Obrigado por jogar nosso joguinho! ❤")
        print('🌟 Créditos 🌟 : ')
        time.sleep(2)
        print("Ieda Cruz da Silva")
        time.sleep(2)
        print("João Victor Neves Alves")
        time.sleep(2)
        print("Marcos Vinicius Gasparoto Bauab")
        print('------------------------------------------------------------------------')
#Venceu
def venceu():
    print("PARABÉNS, você conseguiu sobreviver à uma Rotina Universitária®!\n"
          "✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨")
    input("Agora, como você venceu o dia, bora planejar o dia seguinte (pressione ENTER para continuar): ")
    print("\033[1;97;40mR O T I N A :\033[97;40;0m")
    linhas = input("Quantas linhas de rotina serão ? ")
    while re.match('^\d+$', linhas) == None:
        linhas = input("Quantas linhas de rotina serão ? ")
    rotina = []
    for i in range(int(linhas)):
        rotina.append(input("Insira a {}º linha: ".format(i+1)))
    print("\033[1;97;40mR O T I N A :\033[97;40;0m")
    for tarefa in rotina:
        time.sleep(2)
        print(tarefa)
    print()
    print("E bora pro próximo dia... 💤")
    print('------------------------------------------------------------------------')
    print("Obrigado por jogar nosso joguinho! ❤")
    print('🌟 Créditos 🌟 : ')
    time.sleep(2)
    print("Ieda Cruz da Silva")
    time.sleep(2)
    print("João Victor Neves Alves")
    time.sleep(2)
    print("Marcos Vinicius Gasparoto Bauab")
    print('------------------------------------------------------------------------')
    decisao = input("Tá afim de começar de novo (S/N)? ")
    while decisao.lower() != 's' and decisao.lower() != 'n':
        decisao = input("Tá afim de começar de novo (S/N)? ")
    if decisao.lower() == 's':
        manha()
    elif decisao.lower() == 'n':
        print('Poxa, que triste que você não quer jogar mais!\n'
              'Mas infelizmente, não ligamos, e você continuará a jogar...')
        print()
        print("\033[1;97;40mR O T I N A :\033[97;40;0m")
        print()
        print("Manhã : \n"
              "Café da manhã com a família - 7h \n"
              "Aula de cálculo - 8h até 10h \n"
              "Freela blogueiro - 10h até 11h \n"
              "Ir no mercado - 11h \n"
              "Almoço - 12h \n"
              "Adiantar os quizzes")
        time.sleep(4)
        print('------------------------------------------------------------------------')
        print("KKKKK, brincadeira, tchau!")

#Funções gerais
def status():
    print("Estes são seus pontos de habilidade (se algum deles zerou é GAME OVER): \n"
          "Energia: {} | Alegria: {} | Esportes: {} | Amizades: {} | Organização: {} | Saúde: {}".format(habilidades['energia'],habilidades['alegria'],
                                                                                                         habilidades['esportes'],habilidades['amizades'],habilidades['organizacao'],habilidades['saude']))
    print("E este é seu inventário: {}".format(inventario))
    print("-------------------------------------------------------------------------------")

def rotina():

      print()
      print("\033[1;97;40mR O T I N A :\033[97;40;0m")
      print()
      print("Manhã : \n"
            "Café da manhã com a família - 7h \n"
            "Aula de cálculo - 8h até 10h \n"
            "Freelance blogueiro - 10h até 11h \n"
            "Ir no mercado - 11h \n"
            "Almoço - 12h \n"
            "Adiantar os quizzes")
      time.sleep(4)
      print()
      print("Tarde : \n"
            "Aula de química - 14h até 15h \n"
            "Ir no dentista - 16h \n"
            "Praticar esportes - 17h")
      time.sleep(4)
      print()
      print("Noite : \n"
            "Fazer os quizzes - 18h \n"
            "Jantar - 19h \n"
            "Google Meet com os amigos - 20h \n"
            "Planejar o dia seguinte - 22h")
      time.sleep(4)
      print()

def pularLinhas(parm):
    for i in range(parm):
        print()

def relogio(hora, min):
    pularLinhas(5)
    print("{}h{}...".format(hora,min))
    time.sleep(4)
    pularLinhas(5)

def espaco():
    print('------------------------------------------------------------------------')

#Manhã
def dirigindo():
    pularLinhas(4)
    print("Dirigindo...")
    time.sleep(4)
    pularLinhas(4)

def freela(param):
    print('')
    if param == '':
        decisao = input("NOSSA, agora que eu me toquei, são 10h e seu trabalho de freelancer já vai começar! \n"
              "Tá afim de trabalhar hoje ? (S/N): ")
        while decisao.lower() != 'n' and decisao.lower() != 's':
            decisao = input("Responda com (S/N): ")
        if decisao.lower() == 'n':
            print("Ai que delícia, um dia de folga pro estudante cansado né ?! (Energia +1, Organização -2, Alegria +1)\n"
                  "Bom, como seu dinheiro viria do freela, me parece que você vai passar uns apuros durante o dia em...")
            habilidades['energia'] += 1
            habilidades['alegria'] += 1
            habilidades['organizacao'] -= 2
            trab = False
        elif decisao.lower() == 's':
            print("Digite a maior quantidade de S que conseguir, esse é seu trabalho, vai! Digite ENTER quando acabar 😆")
            input()
            print()
            print("Brincadeira, a gente nem contou a quantidade de S hehehe!\n"
                  "Aí sim, jovem trabalhador, orgulho desse Brasil! (Energia -1, Organização +2)\n"
                  "Com esse dinheiro em mãos (+100), te garanto que seu dia vai ficar mais fácil...")
            habilidades['energia'] -= 1
            habilidades['organizacao'] += 2
            inventario['Dinheiro'] += 100
            trab = True
        time.sleep(3)
    else:
        print("\nRespeita o aluno aplicado passando! Seu chefe viu seu esforço na facul, \n"
              "e decidiu te dar um dia de folga, mas VAI TE PAGAR DO MESMO JEITO, quem pode pode em! (+100 reais)")
        time.sleep(2)
        inventario['Dinheiro'] += 100
        trab = True
    return trab

def jogodobicho():
    bichos = ['Cavalo','Porco','Galinha','Orangotango','Boto-cor-de-rosa','Tiranossauro Rex']
    random.shuffle(bichos)
    grana = random.randint(10, 50)
    inventario['Dinheiro'] += grana
    print("Como sua grana tá baixa, você lembrou que apostou no jogo do bicho ontem e hoje sai o resultado! \n"
          "Esse foi o animal e o valor que você ganhou: {} - R${}".format(bichos[0], grana))

def calcularValor(parm):
    item = lista[parm].split('-')
    item2 = []
    bre = False
    for i in range(len(item)):
        item2.append(item[i].split())
    item3 = int(item2[1][0])
    if inventario['Dinheiro'] >= item3:
        inventario['Dinheiro'] -= item3
    else:
        print("Vish, não vai rolar comprar esse, porque seu dinheiro não compra: {}".format(lista[parm]))
        bre = True
    return bre

def calculo():
    conta = input("1º Questão: Quanto é 1+1 ? ")
    while re.match('^\d+$', conta) == None:
        conta = input("Digite um número: ")
    if conta == '2':
        nome = input("2º Questão: Qual o nome da sua professora preferida ? ")
        if nome.lower() == 'denise':
            input("3º Questão: A integral de (x^3+x^2+1)/x^2-2 é :")
            print("Parabéns, você é SUPER NERD!")
        else:
            print("Acho que você não me entendeu direito...")
    else:
        print("Pô meu/minha amigo(a), errar essa conta aí é meio tenso...")

def manha():
    espaco()
    print("Bom dia! O sol já nasceu lá na fazendinha! 7h da manhã agora em! \n"
          "(a) Apertar o botão soneca do alarme ou (b) Acordar para tomar café da manhã em família ?")
    decisao = input()
    while decisao.lower() != 'a' and decisao.lower() != 'b':
        decisao = input("Responda com (A/B): ")
    if decisao.lower() == 'a':
        espaco()
        print("Vish, passou UM MONTÃO DE TEMPO, agora já é 10h, e infelizmente você PERDEU SUA AULA DE CÁLCULO :( \n"
              "E de quebra, perdeu seu café com a família (Organização -2, Alegria -1, Amizades -3)")
        time.sleep(3)
        habilidades['alegria'] -= 1
        habilidades['organizacao'] -= 2
        trab = freela('')
        relogio(11,'00')
        if inventario['Dinheiro'] < 20:
            jogodobicho()
            time.sleep(4)
        print("Bom, como já são 11 horas, está na hora de você ir no mercado, partiu!")
        time.sleep(1)
        dirigindo()
        print("Chegamos no mercado! Aqui estão suas opções de compra, reflita bem sobre elas, \n"
              "cada uma delas terá efeitos diferentes na sua jornada: ")
        for i in range(len(lista)):
            print("({}) - {}".format(i + 1, lista[i]))
        quant = input("Quantos você vai levar ? ")
        #checando se é número:
        while re.match('^\d+$', quant) == None:
            quant = input("Digite um número: ")
        for i in range(int(quant)):
            decisao = int(input("Qual você vai levar pra casa (digite UM número) ? \n"
                            "Lembra do seu dinheiro em: "))
            item = []
            bre = calcularValor(decisao - 1)
            if bre == True:
                break
            if decisao > 2:
                item.append(lista[decisao - 1])
                inventario['Comidas'].append(item)
            else:
                item.append(lista[decisao - 1])
                inventario['Itens'].append(item)
        input("Ufa, agora é só voltar pra casa! (Pressione ENTER para continuar)")


    elif decisao.lower() == 'b':
        print("Hmmmmmmmmmmmmm, acordar cedo é bom demais! Ou não... Mas de qualquer forma,\n"
              "está na hora de tomar aquele café em família. {Amizades +2, Alegria +2, Organização +1}")
        time.sleep(2)
        habilidades['amizades'] += 2
        habilidades['alegria'] += 2
        habilidades['organizacao'] += 1
        relogio(8,'00')
        print("8h, é hora da aula de cálculo: ")
        calculo()
        relogio(10,'00')
        print("Você assistiu sua aula de cálculo, parabéns! "
              "(Energia -1, Organização +1, Alegria -1)")
        habilidades['energia'] -= 1
        habilidades['alegria'] -= 1
        habilidades['organizacao'] += 1
        print("Bom, como você foi organizado, assistiu sua aula e tomou café com a família,\n"
              "sua mãe te deu 20tão pra comprar aquela bola no mercado que tanto queria, IHA!\n")
        time.sleep(2)
        inventario['Dinheiro'] += 20
        trab = freela('mod')
        relogio(11, '00')
        print("Bom, como já são 11 horas, está na hora de você ir no mercado, partiu!")
        time.sleep(1)
        dirigindo()
        print("Chegamos no mercado! Aqui estão suas opções de compra, reflita bem sobre elas, \n"
              "cada uma delas terá efeitos diferentes na sua jornada: ")
        for i in range(len(lista)):
            print("({}) - {}".format(i + 1, lista[i]))
        quant = input("Quantos você vai levar ? ")
        # checando se é número:
        while re.match('^\d+$', quant) == None:
            quant = input("Digite um número: ")
        for i in range(int(quant)):
            decisao = int(input("Qual você vai levar pra casa (digite UM número) ? \n"
                                "Lembra do seu dinheiro em: "))
            item = []
            bre = calcularValor(decisao - 1)
            if bre == True:
                break
            if decisao > 2:
                item.append(lista[decisao - 1])
                inventario['Comidas'].append(item)
            else:
                item.append(lista[decisao - 1])
                inventario['Itens'].append(item)
        input("Ufa, agora é só voltar pra casa! (Pressione ENTER para continuar)")
    espaco()
    print("Essas são suas habilidades até aqui: ")
    status()
    """
    f = open("salvar.txt", "w")
    a = open("salvar.txt", "a")
    f.write("1\n")
    a.write(str(inventario))
    a.write("\n")
    a.write(str(habilidades))
    f.close()
    a.close()
    """

#Tarde
def almoco():
    relogio(12, '00')
    print('Hmm...hora do almoço, 12h já!! Melhor correr para não se atrasar com os compromissos da tarde, certo? \n'
          'Para ajudar você a lembrar do que precisa fazer nessa tarde, aqui está: ')
    time.sleep(6)
    rotina()
    print('---------------------------------------------------------------------------------------------------------')
    print('E aí, bora preparar o almoço? Responda com S se quiser preparar ou N para não preparar:')
    decisao = input()
    while decisao.lower() != 's' and decisao.lower() != 'n':
      decisao = input('Escolha "S" ou "N": ')
    if decisao.lower() == 's':
        print('BOAA!! Decidiu seguir de acordo com sua rotina, né? Arrasou!!\n'
              'Bom, com base no que você comprou no mercado, vamos para a cozinha preparar sua refeição 😊')
        for i in range(len(inventario['Comidas'])):
            separados = inventario['Comidas'][i][0].split("-")
            print(separados[0])
        comida = input("Escolha sua comida: ")
        print('')
        while comida.lower() != "hot pocket" and comida.lower() != "miojo" and comida.lower() != "espaghetti pupunha ao molho pesto" and comida.lower() != "tilápia, arroz e brócolis":
            comida = input("Escolha sua comida: ")
        for i in range(len(inventario['Comidas'])):
            separados = inventario['Comidas'][i][0].split("-")
            if comida.lower()+" " == separados[0].lower():
                if comida.lower() == 'tilápia, arroz e brócolis':
                    inventario['Comidas'].pop(i)
                    print('UAAU, que prato saudável!! Aí sim emm :) {Saúde +2}')
                    habilidades['saude'] += 2
                    input("Primeiramente, pegue uma panela para fazer o arroz, outra para grelhar a tilápia e outra para cozinhar o brócolis.\n" 
                          "Pressione ENTER para ligar o fogo para fazer o arroz e cozinhar o brócolis")
                    time.sleep(2)
                    print('')
                    print('Esquentando...')
                    print('')
                    time.sleep(2)
                    input('Arroz e brócolis prontos!! Agora, pegue uma panela para grelhar a tilápia. Pressione ENTER para ligar o fogo')
                    print('')
                    time.sleep(2)
                    print('Grelhando...')
                    print('')
                    time.sleep(2)
                    print('Et voilà, sua comida ficou pronta ;) Bom almoço!!')
                    print('---------------------------------------------------------------------------------------------------------')
                    time.sleep(3)
                    break
                elif comida.lower() == 'hot pocket':
                    inventario['Comidas'].pop(i)
                    input('Hmm, você preferiu um lanchinho prático e nada saudável :( mas tudo bem, o dia está corrido hoje, né? \n♥ É sobre isso ♥ {Saúde -3}\n'
                          'Agora, vá até seu freezer, coloque o lanche no prato e esquente-o no microondas. Aperte ENTER para ligar o microondas')
                    print('')
                    habilidades['saude'] -= 3
                    time.sleep(1.5)
                    print('Esquentando...')
                    print('')
                    time.sleep(3)
                    print('Oba!! Ficou pronto, yumyyy! Bom almoço')
                    print('---------------------------------------------------------------------------------------------------------')
                    time.sleep(3)
                    break
                elif comida.lower() == 'espaghetti pupunha ao molho pesto':
                    inventario['Comidas'].pop(i)
                    input('Hmm, que escolha chiq e saudável!! Arrasou na escolha!! {Saúde +2}\n'
                          'Agora, pegue uma panela para cozinhar o macarrão e coloque a água para ferver.\n'
                          'Aperte ENTER para ligar o fogo')
                    habilidades['saude'] += 2
                    print('')
                    print('Esquentando a água...')
                    print('')
                    time.sleep(3.5)
                    input('Água fervendo! Agora, coloque sal na água até que ela fique salgada igual a água do mar e coloque o macarrão.\n' 
                          'Pressione ENTER para colocar o macarrão na água.')
                    print('')
                    time.sleep(2)
                    print('Cozinhando...')
                    print('')
                    time.sleep(2)
                    print('Macarrão pronto!! Agora, escorra o macarrão e depois misture ele com o molho pesto.\n'
                          'ATENÇÃO: não coloque no fogo o pesto, pois se não ele pode ficar amargo! Bom apetite 😊')
                    print('---------------------------------------------------------------------------------------------------------')
                    time.sleep(3)
                    break
                elif comida.lower() == 'miojo':
                    inventario['Comidas'].pop(i)
                    input('Você escolheu o clássico miojão, rápido e fácil, mas nada saudável 😔 mas ok ok! {Saúde -3}\n'
                          'Agora, coloque a água para ferver. Pressione ENTER para ligar o fogo.')
                    habilidades['saude'] -= 3
                    print('')
                    time.sleep(2)
                    print('Esquentando a água...')
                    print('')
                    time.sleep(2)
                    print('Água fervendo! Agora, coloque o macarrão instantâneo nessa água e espere até que ele fique al dente.')
                    print('')
                    time.sleep(2)
                    print('Miojo pronto. Coloque o temperinho que vem junto, se quiser, e misture. Almoço pronto!! Bom apetite 😊')
                    print('---------------------------------------------------------------------------------------------------------')
                    time.sleep(3)
                    break

    elif decisao.lower() == 'n':
      print('OK, a preguiça bateu e você não vai querer fazer almoço hoje. Tudo bem!\n'
             'Bom, o que te resta é: (A)Comer o que tem na geladeira ou (B)Pedir iFood\n' 
             'P.S.: lembre-se que você possui {} reais'.format(inventario['Dinheiro']))
      decisao = input('Escolha A ou B: ')
      while decisao.lower() != 'a' and decisao.lower() != 'b':
        print('Escolha "A" ou "B"')
        decisao = input()
      if decisao.lower() == 'a':
        print('Vejo que você decidiu economizar, boaa!!\n'
              'Então, vá até a geladeira, pegue o que restou para você almoçar hoje e coloque no microondas, rápido e prático! Bom almoço 😉')
        print('---------------------------------------------------------------------------------------------------------')
        time.sleep(3)
      elif decisao.lower() == 'b':
        print('Pedir comida é tão gostoso, né? Só ir lá no iFood e pedir, praticidade é tudo!! O que vai querer almoçar?'
              'As opções que estão no iFood hoje são essas: ')
        for comida in ifood:
            print(comida)
        print("Qual você pedirá? OBS: LEMBRE-SE DO SEU $$$")
        decisao = input('Digite aqui qual opção você vai querer: ')
        while decisao.lower() != 'pizza' and decisao.lower() != 'hamburgão' and decisao.lower() != 'caldinho' and decisao.lower() != 'poke':
          decisao = input('Digite aqui qual opção você vai querer: ')
        if inventario['Dinheiro'] < 15:
            print("Vish, não vai rolar, melhor preparar alguma coisa...")
            almoco()
        else:
            print('Yummy!! Boa pedidaa, você escolheu {}, que delícia! Tenha um bom almoço, você gastará 15 reais ;)'.format(decisao))
            inventario['Dinheiro'] -= 15
        print('---------------------------------------------------------------------------------------------------------')
        time.sleep(3)

def quiz():
    print('Ahhh, depois do almoço dá aquela moleza, né? Mas bora lá, hoje você não tem tempo para descansar, é o meu conselho.\n'
          'Quer adiantar os quizes da facul dessa semana ou quer ignorá-los por enquanto?\n'
          'Responda com S para fazer e N para descansar:')
    decisao = input()
    while decisao.lower() != 's' and decisao.lower() != 'n':
      print('Escolha "S" ou "N"')
      decisao = input()
    if decisao.lower() == 's':
        print('Boa escolha, vejo que você quer se adiantar nas coisas 😉\n' 
              'Agora corre lá ligar seu computador para dar uma estudada!!{Organização +1, Energia -1}')
        habilidades['organizacao'] += 1
        habilidades['energia'] -= 1
        time.sleep(3)
    elif decisao.lower() == 'n':
        print('Você está com preguiça, te entendo. Descanse, guerreiro!! {Organização -2}')
        habilidades['organizacao'] -= 2
        time.sleep(3)

def aula_quimica():
    espaco()
    relogio(13, 50)
    print('NOSSA, 13:50h já!! Como o tempo voou 😱 \n'
          'de acordo com sua agenda, você tem aula de química às 15h! Você vai assisti-la(A) ou prefere dar uma descansada(B)?')
    decisao = input()
    while decisao.lower() != 'a' and decisao.lower() != 'b':
        print('Escolha "A" ou "B"')
        decisao = input()
    if decisao.lower() == 'a':
        print('Que orgulho! Então bora entrar no Google Classroom para pegar o link da aula no Meet para não atrasar!! '
              '{Energia -1, Organização +1}')
        habilidades['energia'] -= 1
        habilidades['organizacao'] += 1
        time.sleep(3)
    if decisao.lower() == 'b':
        print('Poxa, vai deixar de assistir a aula 😔\n'
              'Mas tudo bem, o estudante cansado que habita dentro de você precisa tirar um tempinho off... {Alegria +1, Organização -1}')
        habilidades['alegria'] += 1
        habilidades['organizacao'] -= 1
        time.sleep(3)

def dentista():
    relogio(15,30)
    print('UIA, 15:30h já!! Seu dentista é às 16h, tá lembrando, né? Prefere ir como?\n'
          '(A)dirigindo ou (B)chamar um Uber?\n'
          'Lembrando que você tem {} reais e a viagem de uber custa 15 reais o total da ida e volta'.format(inventario['Dinheiro']))
    decisao = input('Digite (A) ou (B): ')
    while decisao.lower() != 'a' and decisao.lower() != 'b':
        print('Escolha "A" ou "B"')
        decisao = input()
    if decisao.lower() == 'a':
        print('Avisa que o motorista tá ON, ihaa!! Mais rápido você dirigindo, né? Então partiu dentista!!')
        print('')
        time.sleep(3)
        print('OPA, temos um problema. O nível de combustível está muito baixo e talvez não dê para você chegar até o consultório 😨 e agora??')
        print('')
        time.sleep(2)
        print('Bom, restou a você essa quantidade de dinheiro: {} reais. Então...'.format(inventario['Dinheiro']))
        time.sleep(3)
        if inventario['Dinheiro'] >= 40:
            print('Com essa quantidade de dinheiro você pode abastecer o carro e dará para ir e voltar do dentista, yaaay!!\n'
                  'Melhor correr para dar tempo de você abastecer e chegar lá no consultório a tempo!!')
            inventario['Dinheiro'] -= 40
            relogio(15, 45)
            print('abastecendo...')
            relogio(16,'00')
            print('Você chegou ao seu destino. Encarnou Velozes e Furiosos, foi? {Saúde +1, Organização +1}')
            habilidades['saude'] += 1
            habilidades['organizacao'] += 1
            time.sleep(3)
        elif inventario['Dinheiro'] >= 15 and inventario['Dinheiro'] < 40:
            input('Acho melhor você chamar um uber, pois para abstecer você precisa de 40 reais :( Corre para não perder hora!!\n'
                   'Quando estiver pronto para ir pressione Enter para chamar um uber')
            inventario['Dinheiro'] -= 15
            print('')
            print('Uber a 5 minutos de distância!')
            time.sleep(3)
            print('')
            print('Et voilà, seu uber acabou de chegar! Tenha uma boa consulta 😉')
            time.sleep(2)
            relogio(16, 10)
            print('AI, O TRÂNSITO TÁ TENSO, será que vai dar tempo? 😨')
            relogio(16, 30)
            print('Pois é...acho melhor voltar para casa...que pena {Saúde -1, Organização -1}')
            habilidades['saude'] -= 1
            habilidades['organizacao'] -= 1
            time.sleep(3)
    elif decisao.lower() == 'b':
        if inventario['Dinheiro'] < 15:
            print("Poxa, não vai ser possível ir até o dentista, ta sem grana, que pena 😔\n"
                  "Você perdeu sua consulta...")
            time.sleep(3)
        else:
            input('Como é bom não ter que dirigir, ufa! Aperte Enter para chamar o Uber!')
            print('Boa! Uber a 10 minutos de distância!')
            relogio(15, 50)
            print('Uber chegou, boa viagem!')
            time.sleep(2)
            relogio(16, 10)
            print('AI, O TRÂNSITO TÁ TENSO, será que vai dar tempo? 😔')
            relogio(16, 30)
            print('Pois é...acho melhor voltar para casa...que pena {Saúde -1, Organização -1}')
            habilidades['saude'] -= 1
            habilidades['organizacao'] -= 1
            inventario['Dinheiro'] -= 15
            time.sleep(3)

def esporte():
    espaco()
    relogio(16,50)
    print('E aí, tudo certinho? Pronto para praticar esportes? 16:50h já!! (S/N): ')
    decisao = input()
    while decisao.lower() != 's' and decisao.lower() != 'n':
        print('Escolha "S" ou "N"')
        decisao = input()
    if decisao.lower() == 's':
        print('Bom, para praticar esportes, você precisa de um halter ou uma bola. Ou os dois, aí fica show!!')
        if len(inventario['Itens']) == 2:
            if (inventario['Itens'][0][0] == 'Bola - 20 reais' and inventario['Itens'][1][0] == 'Halter - 20 reais') \
                    or (inventario['Itens'][1][0] == 'Bola - 20 reais' and inventario['Itens'][0][0] == 'Halter - 20 reais'):
                print('Eba, você tem um halter e uma bola, aí já dá para você se endorfinizar em dobro 🤪 {Energia +2, Saúde +1, Esportes +4}')
                habilidades['energia'] += 2
                habilidades['saude'] += 1
                habilidades['esportes'] += 4
                time.sleep(3)
        if len(inventario['Itens']) == 1:
            if inventario['Itens'][0][0] == 'Bola - 20 reais':
                print('Eba, você tem uma bola, aí já dá para você se endorfinizar 🤪 {Energia +1, Saúde +1, Esportes +2}')
                habilidades['energia'] += 1
                habilidades['saude'] += 1
                habilidades['esportes'] += 2
                time.sleep(3)
            elif inventario['Itens'][0][0] == 'Halter - 20 reais':
                print('Eba, você tem um halter, aí já dá para você se endorfinizar 🤪 {Energia +1, Saúde +1, Esportes +2}')
                habilidades['energia'] += 1
                habilidades['saude'] += 1
                habilidades['esportes'] += 2
                time.sleep(3)
        else:
            if inventario['Itens'] == []:
                print('Poxa, não vai dar para você praticar esportes hoje 😔 {Saúde -2}')
                habilidades['saude'] -= 2
                time.sleep(3)
    elif decisao.lower() == 'n':
        print('Você está meio cansadinho, né? Percebe-se. Mas hoje passa ♥ é sobre isso ♥ {Saúde -2, Esportes -5}')
        habilidades['saude'] -= 2
        habilidades['esportes'] -= 5

def tarde():
    almoco()
    quiz()
    aula_quimica()
    dentista()
    esporte()
    espaco()
    status()

#Noite
def janta(decisao):
    while decisao.lower() != 'a' and decisao.lower() != 'b':
        print("Escolha 'a' ou 'b'!")
        decisao = input()
    if decisao.lower() == 'a':
        print("Essas são suas opções de comida :")

        for i in range(len(inventario['Comidas'])):
            separados = inventario['Comidas'][i][0].split("-")
            print(separados[0])
        comida = input("Escolha sua comida: ")
        while comida.lower() != "hot pocket" and comida.lower() != "miojo" and comida.lower() != "espaghetti pupunha ao molho pesto" and comida.lower() != "tilápia, arroz e brócolis":
            comida = input("Escolha sua comida: ")

        for i in range(len(inventario['Comidas'])):
            separados = inventario['Comidas'][i][0].split("-")
            if comida.lower()+" " == separados[0].lower():
                if comida.lower() == 'hot pocket':
                    print("Refeição prática e rápida, mas não tão saudável. {Saúde -3}")
                    habilidades['saude'] -= 3

                elif comida.lower() == 'miojo':
                    print("Um clássico, mas não muito saudável. {Saúde -3}")
                    habilidades['saude'] -= 3

                elif comida.lower() == 'espaghetti pupunha ao molho pesto':
                    print("Escolha de alta gastromia! Excelente! {Energia +1, Saúde +2}")
                    habilidades['energia'] += 1
                    habilidades['saude'] += 2

                elif comida.lower() == 'tilápia, arroz e brócolis':
                    print("Excelente escolha! {Energia +1, Saúde +2}")
                    habilidades['energia'] += 1
                    habilidades['saude'] += 2

    elif decisao.lower() == 'b':
        #Opções de comida saudável e não saudável baseado no dinheiro
        # 0 - pizza 1 - hamburgão 2 - caldinho 3 - poke
        if inventario['Dinheiro'] < 15:
            print("Você não tem dinheiro suficiente para isso! Agora terá que ir para a cozinha!")
            janta('a')
        else:
            for alimento in ifood:
                print(alimento)
            decisao = input("Qual vai ser : ")
            while decisao.lower() != 'pizza' and decisao.lower() != 'hamburgão' and decisao.lower() != 'caldinho' and decisao.lower() != 'poke':
                print("Escolha 'pizza', 'hamburgão', 'caldinho' ou 'poke'!")
                decisao = input()
            if decisao.lower() == ifood[0].lower():
                print("Uma pizza de calabresa vai bem demais! {Energia +1, Saúde -2}")

                inventario['Dinheiro'] -= 15
                habilidades['energia'] += 1
                habilidades['saude'] -= 2
                print("Pena que custou 15 reais do seu cofrinho.")

            elif decisao.lower() == ifood[1].lower():
                print("Um Hamburgão sempre vai bem! {Energia +1, Saúde -2}")
                inventario['Dinheiro'] -= 15
                habilidades['energia'] += 1
                habilidades['saude'] -= 2
                print("Foram 15 reais bem gastos.")

            elif decisao.lower() == ifood[2].lower():
                print("Excelente escolha! Um caldinho é muito bom para esquentar o corpo nesse friozinho. {Energia +2, Saúde +2}")
                inventario['Dinheiro'] -= 15
                habilidades['energia'] += 2
                habilidades['saude'] += 2
                print("O preço dessa escolha foi de 15 reais.")

            elif decisao.lower() == ifood[3].lower():
                print("Escolheu muito bem! Um Poke é uma ótima refeição. {Energia +2, Saúde +2}")
                inventario['Dinheiro'] -= 15
                habilidades['energia'] += 2
                habilidades['saude'] += 2
                print("Isso tirou 15 reais da sua conta.")

def noite():
    print("A noite começou. É bom dar uma revisada nos seus afazeres:")
    rotina()
    decisao = input("Comecinho da noite, mas a rotina ainda não acabou. São 18h e você ainda tem coisas a fazer \n"
                    "Faça sua escolha: (a)Fazer os Quizzes do dia ou (b)Escutar um podcast para relaxar? ")
    time.sleep(3)
    print('')
    while decisao.lower() != 'a' and decisao.lower() != 'b':
        print("Escolha 'a' ou 'b'!")
        decisao = input()
    if decisao.lower() == 'a':
        quizzes = True
        decisao = input("Boa! Acumular matéria nunca é legal. {Organização +1, Alegria +1, Energia -1} \n"
                        "Depois de estudar bastante, às 19h é hora de jantar. (a)Vá até a cozinha ou (b)Peça algo para comer: ")
        habilidades['organizacao'] += 1
        habilidades['alegria'] += 1
        habilidades['energia'] -= 1
        janta(decisao)


    elif decisao.lower() == 'b':
        quizzes = False
        print("Deu para relaxar legal, mas acho que não foi uma escolha inteligente. {Organização -1, Alegria +1}")
        relogio(19, '00')
        decisao = input("Já são 19h e é hora de jantar. (a)Vá até a cozinha ou (b)Peça algo para comer: ")
        habilidades['organizacao'] -= 1
        habilidades['alegria'] += 1
        janta(decisao)

    print('')
    print("De barriga cheia e depois de descansar um pouco, seus amigos da faculdade te chamaram para fofocar no Google Meet às 20h.")

    if quizzes == True:
        print("E já que você não tem mais Quizzes para fazer, é hora de se divertir com os amigos. {Amizades +1, Alegria +1}")
        habilidades['amizades'] += 1
        habilidades['alegria'] += 1

    elif quizzes == False:
        print("Mas infelizmente você não fez os quizzes da faculdade. \n"
              "Seus amigos sentirão sua falta enquanto você estuda. {Amizades -1, Alegria -1, Energia -1}")
        habilidades['energia'] -= 1
        habilidades['alegria'] -= 1
        habilidades['amizades'] -= 1

    espaco()
    print("Esse é o seu status final, será que conseguiu sobreviver à essa rotina ?")
    status()






nome = input("Olá, bem-vindo(a) ao nosso jogo! \n"
             "Como você se chama ? ")
while nome == '':
    nome = input("Olá, bem-vindo(a) ao nosso jogo! \n"
                 "Como você se chama ? ")
print()
print("Olá, {}, nesse cenário de pandemia, "
      "vamos ver se você aguenta uma rotina universitária em ADE.".format(nome))
time.sleep(2)
rotina()

print("Seu objetivo é não zerar nenhuma de suas habilidades até o final do dia, "
      "se você sobreviver até lá...")
print("-----------------------------------------------------------------------------------------------------------")
status()
print("Além de habilidades, você possui um inventário, e dependerá de certos itens para acessar locais especiais, "
      "manter sua saúde e praticar esportes!")
print("-----------------------------------------------------------------------------------------------------------")
decisao = 'N'
while decisao.lower() != "s":
      decisao = input("Pronto para começar ? (S/N): ")



manha()
if (habilidades['alegria'] <= 0) or (habilidades['energia'] <= 0) or \
        (habilidades['esportes'] <= 0) or (habilidades['amizades'] <= 0) or \
        (habilidades['organizacao'] <= 0) or (habilidades['saude'] <= 0):
    gameOver()
else:
    tarde()
    if (habilidades['alegria'] <= 0) or (habilidades['energia'] <= 0) or \
        (habilidades['esportes'] <= 0) or (habilidades['amizades'] <= 0) or \
        (habilidades['organizacao'] <= 0) or (habilidades['saude'] <= 0):
        gameOver()
    else:
        noite()
        if (habilidades['alegria'] <= 0) or (habilidades['energia'] <= 0) or \
           (habilidades['esportes'] <= 0) or (habilidades['amizades'] <= 0) or \
           (habilidades['organizacao'] <= 0) or (habilidades['saude'] <= 0):
            gameOver()
        else:
            venceu()







