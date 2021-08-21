nome = input("Olá, bem-vindo(a) à UNIFESP! \n"
      "Como você se chama ? ")

habilidades = {'alegria': 5, 'energia': 5, 'esportes': 5, 'amizades': 5, 'organizacao': 5, 'saude': 5}
boletim = {'calculo': 0}
inventario = []

def status(parm):
      print("_{}º Dia_ \nEste são seus pontos de habilidade (se algum deles zerar é GAME OVER): \n"
            "Energia: {} | Alegria: {} | Esportes: {} | Amizades: {} | Organização: {} | Saúde: {}".format(parm, habilidades['energia'], habilidades['alegria'],
                                                                                                        habilidades['esportes'],
                                                                                                        habilidades['amizades'],
                                                                                                        habilidades['organizacao'],
                                                                                                        habilidades['saude']))
      print("E este é seu inventário: {}".format(inventario))
      print("-------------------------------------------------------------------------------")

print("Olá, {}, nesse cenário de pandemia, "
      "vamos ver como você está se saindo nos estudos à distância.".format(nome))
print()


#Primeiro dia:
def primeiroDia():
      print("Este é seu primeiro dia de aula!!! UUHUUULLL, eaí, animado?")
      decisao = input("A aula de Cálculo será às 8 da manhã \n(d) Dormir ou (a) Acordar pra aula ? ")
      print()
      if decisao.lower() == 'a':
            print("Você assistiu sua primeira aula de Cálculo, parabéns! "
                  "(Energia -1, Organização +1, Alegria -1, Cálculo +1)")
            habilidades['energia'] -= 1
            habilidades['alegria'] -= 1
            habilidades['organizacao'] += 1
            boletim['calculo'] += 1
            print("Sua aula de Cálculo acabou, foi suado!\n"
                  "Agora você vai : (a) Dormir (b) Cozinhar algo saudável "
                  "(c) Praticar esportes (d) Estudar a matéria do dia")
            decisao = input()
            if decisao.lower() == 'a':
                  print("NOSSA, SÃO 19h DA NOITE, VOCÊ DORMIU O DIA TODO! (Energia +1, Organização -1, Saúde -1)\n"
                        "E agora, (a) pedir fastfood ou (b) preparar sua comida ?")
                  habilidades['organizacao'] -= 1
                  habilidades['alegria'] += 1
                  habilidades['saude'] -= 1
                  habilidades['energia'] += 1
                  decisao = input()
                  if decisao.lower() == 'a':
                        print("Hamburgão tava brabo demais :S (Saúde -1, Alegria +1)\n"
                              "Agora, como você deve estar cheio, sua pressão começa a baixar e você fica sonolent.... zzzzz")
                        habilidades['saude'] -= 1
                        habilidades['alegria'] += 1
                        print()
                        print("-------------------------------------------------------------------------------")
                        status(1)
                  elif decisao.lower() == 'b':
                        print("Você venceu a preguiça (Alegria -1), parabéns, orgulho fitness! Aproveite sua janta muito bem preparada!\n"
                              "E como já está tarde, acho que está na hora de dormir né ? Boa noite!")
                        habilidades['alegria'] -= 1
                        print()
                        print("-------------------------------------------------------------------------------")
                        status(1)
            elif decisao.lower() == 'b':
                  print("")

      elif decisao.lower() == 'd':
            print("Você perdeu sua primeira aula de Cálculo, eita! (Energia +1, Organização -1, Alegria +1)")
            habilidades['organizacao'] -= 1
            habilidades['energia'] += 1
            habilidades['alegria'] += 1

while (habilidades['alegria'] > 0) and (habilidades['energia'] > 0) and \
      (habilidades['esportes'] > 0) and (habilidades['amizades'] > 0) and \
      (habilidades['organizacao'] > 0) and (habilidades['saude'] > 0):
      primeiroDia()


#Game Over
def gameOver():
      print()


if (habilidades['alegria'] == 0) or (habilidades['energia'] == 0) or \
      (habilidades['esportes'] == 0) or (habilidades['amizades'] == 0) or \
      (habilidades['organizacao'] == 0) or (habilidades['saude'] == 0):
      gameOver()
else:
      print()
