from os import system, name 
def limpaTela(): 
    if name == 'nt': 
        system('cls') 
    else: 
        system('clear')

def separaCedulas(valor, quantidade):
    """
    Está função usará os valores obtidos das funções "imprimeNotas" e "imprimeMoedas" e substituirá o valor dado pela chamada
    da função dentro dessas funções, onde lá está o cálculo que o valor será substituido nessa variável "quantidade" 
    e, assim, se a sua condição não for aceita, a mesma refaz mais um calculo diminuindo o valor da quantidade por -1. 
    Quando o valor for 0, a função irá parar de separar e imprimir as cedulas.
    """
    if quantidade > 0 and quantidade >= 0.01:
        print(f'R${valor:.2f}')
        quantidade = quantidade - 1
        separaCedulas(valor, quantidade)

def proximaNota(maiorNota):
    """
    Está função pega o valor atribuido a variavel "maiorNota" que está presente na função "imprimeNotas(troco, maiorNota = 100)
    e executa as seguintes condições abaixo: (podemos dizer que essa função sempre atualizará o valor da maiorNota)
    """
    if maiorNota == 50:
        maiorNota = 20
    #Se sua primeira condição não for satisfeita, a mesma irá executar a segunda parte que pegará o valor da maior nota e 
    #irá obter sua parte inteira por 2 e, assim, retornará o valor atribuido para variável maiorNota, que por sua vez, chamará
    #novamente a função "imprimeNotas", onde será, novamente, feita o procedimento para alcançar o seu caso base.
    else:
        maiorNota = maiorNota // 2
        #O valor que for gerado nesse cálculo, será o novo valor atribuido a variavel "maiorNota" da função "imprimeNotas"
        #onde a mesma irá executar todo o procedimento novamente, até alcançar o seu caso base e, assim, parar a sua recursividade
    return maiorNota

def imprimeNotas(troco, maiorNota = 100):
    """
    Está função pega o valor atribuido a variavel trocoNotas (que sera designada pela chamada da função, na função principal)
    e avaliará as seguintes condições abaixo. 
    """
    if troco == 0:
        return troco
    elif troco >= maiorNota:
        separaCedulas(maiorNota, troco // maiorNota)#Parte da função que será atribuida ao valor da "quantidade" na função "separaCedulas".
        troco = troco % maiorNota #Parte da função que verifica se precisa fazer mais impressões de Notas.
    return imprimeNotas(troco,proximaNota(maiorNota)) 
    #Este return, chamará a função que mostra qual será o valor da próxima nota.

def proximaMoeda(maiorMoeda):
    """
    Está função pega o valor atribuido a variavel "maiorMoeda" que está presente na função "imprimeMoedas
    (troco, maiorMoeda = 50) e executa as seguintes condições abaixo: 
    (podemos dizer que essa função sempre atualizará o valor da maiorNota)

    """
    maiorMoeda = maiorMoeda / 2
    if maiorMoeda == 12.5:
        maiorMoeda = 10
    if maiorMoeda == 2.5:
        maiorMoeda = 1
    return maiorMoeda

def imprimeMoedas(troco, maiorMoeda = 50):
    """
    Está função é similar a função "imprimeNotas", ela irá pegar o valor atribuido a variavel "trocoMoedas" 
    (que será designada pela chamada da função, na função principal) e avaliará as seguintes condições abaixo.

    """
    if troco == 0:
        return troco
    elif troco >= maiorMoeda:
        separaCedulas(maiorMoeda/100, troco // maiorMoeda)#Parte da função que será atribuida ao valor da "quantidade" na função "separaCedulas".
        troco = troco % maiorMoeda
    return imprimeMoedas(troco,proximaMoeda(maiorMoeda))
    #Este return, chamará a função que mostra qual será o valor da próxima nota.

def entradaDinheiro(custoProduto, dinheiro = 0.0):
    """
    Essa função pega o valor do custoProduto e o substitui pelo valor do custoProdutoEscolhido e ,logo após, pega esse valor 
    e verifica as condições estabelecidas. Caso a primeira condição não seja agradada, ele mandará o usuário colocar o dinheiro,
    até que essa condição seja satisfeita (ou seja, nosso caso base). Quando esse caso base for satisfeito, ele substituirá
    o valor obtido na chamada de função, onde está localizada na: def maquina().
    """
    if dinheiro >= custoProduto:
        return dinheiro        
    valor = float(input('Coloque o dinheiro: '))
    if valor == 100:
        dinheiro += valor
    elif valor == 50:
        dinheiro += valor
    elif valor == 20:
        dinheiro += valor
    elif valor == 10:
        dinheiro += valor
    elif valor == 5:
        dinheiro += valor
    elif valor == 2:
        dinheiro += valor
    elif valor == 1:
        dinheiro += valor
    elif valor == 0.50:
        dinheiro += valor
    elif valor == 0.25:
        dinheiro += valor
    elif valor == 0.10:
        dinheiro += valor
    elif valor == 0.05:
        dinheiro += valor
    elif valor == 0.01:
        dinheiro += valor
    else:
        print('Valor invalido')
    return entradaDinheiro(custoProduto, dinheiro)

def maquina(itemA = 1, itemB = 1, itemC = 1, itemD = 1, itemE = 1):
    """
    Está é a função principal do programa, onde a mesma que irá fazer a chamada das outras funções para resolver o seu problema.
    A mesma, também, cuida do estoque de produtos na máquina, onde após a escolha de um produto, na condição da mesma tem uma
    fórmula de redução do estoque, onde que temos uma condição caso o estoque se esgote.
    """
    custoA = 5.50
    custoB = 2.20
    custoC = 1.75
    custoD = 1.00
    custoE = 3.00
    dinheiro = 0.0

    print('=' * 30)
    if itemA == 0:
        print('1 - Batata List      - Não está disponível')
    else:
        print('1 - Batata List      - R$ 5,50')
    if itemB == 0:
        print('2 - Suco de Laranja  - Não está disponível')
    else:
        print('2 - Suco de Laranja  - R$ 2,20')
    if itemC == 0:
        print('3 - Chocolate Lambda - Não está disponível')
    else:
        print('3 - Chocolate Lambda - R$ 1,75')
    if itemD == 0:
        print('4 - Chiclete         - Não está disponível')
    else:
        print('4 - Chiclete         - R$ 1,00')
    if itemE == 0:
        print('5 - Barra de cereal  - Não está disponível')
    else:
        print('5 - Barra de cereal  - R$ 3,00')
    print('=' * 30)
    x = int(input('Escolha seu produto:')) #Nesse input, podemos perceber que ele selecionará um produto e logo após irá
    #verificar suas condições, caso alguma seja atendida, o mesmo retornará uma resposta (no caso uma string).
    print('=' * 30)
    #Essas condições dos if's, elif's e elses, são as que dará continuidade para o programa, caso nenhum valor dele seja
    #obedecido, o programa pulará para a parte do else, onde o mesmo verifica se o usuário queira usar a maquina novamente,
    #caso ele não queira, o programa irá mostrar uma mensagem de agradecimento e, logo após, finalizará o programa.
    if x == 1 and itemA > 0:
        print('Você escolhe Batata List')
        custoProdutoEscolhido = custoA
        print(f'Preço: R${custoA:.2f}')
        itemA -= 1 and itemA != -1
    elif x == 2 and itemB > 0:
        print('Você escolheu Suco de Laranja')
        custoProdutoEscolhido = custoB
        print(f'Preço: R${custoB:.2f}')
        itemB -= 1 and itemB != -1
    elif x == 3 and itemC > 0:
        print('Você escolheu Chocolate Lambda')
        custoProdutoEscolhido = custoC
        print(f'Preço: R${custoC:.2f}')
        itemC -= 1 and itemC != -1
    elif x == 4 and itemD > 0:
        print('Você escolheu Chiclete')
        custoProdutoEscolhido = custoD
        print(f'Preço: R${custoD:.2f}')
        itemD -= 1 and itemD != -1
    elif x == 5 and itemE > 0:
        print('Você escolheu Barra de Cereal')
        custoProdutoEscolhido = custoE
        print(f'Preço: R${custoE:.2f}')
        itemE -= 1 and itemE != -1
    #Note que cada escolha tem uma condição dentro que faz com que o estoque mude e ele nunca ficará negativo, ou seja, sempre
    #terá seu valor maior ou igual a 0.
    else:
        print('Não possuímos essa opção.')
        print('=' * 30)
        resp = input("Deseja fazer escolher outro produto (S/N)? ")
        if resp == "S" or resp == "s":
            limpaTela()
            maquina(itemA, itemB, itemC, itemD, itemE)
        else: 
            print('Obrigado pela preferência.')
            print('Volte Sempre!!!')
            exit()
    #Após ele selecionar o produto, será feito uns pequenos cálculos para analisar se o valor necessita de troco ou não.
    #Assim, o produto que o usuário escolher, a função pegará o seu valor e jogará na função relacionada ao dinheiro,
    #coloquei então essa variável "dinheiroDepositado" para armazenar o valor que foi escolhido, assim, para podermos
    #usar nas outras funções e dá prosseguimento ao programa.
    dinheiroDepositado = entradaDinheiro(custoProdutoEscolhido)
    troco = dinheiroDepositado - custoProdutoEscolhido
    #Nessa parte do troco, é onde o programa pega a aquela variável que definimos (dinheiroDepositado)
    #e o diminui pelo preço do produto escolhido, assim, ele obtém o valor dessa variável que denominei de troco.
    trocoNotas = troco // 1
    #Nessa parte, o programa irá pegar o valor do troco e o transformará na sua parte inteira.
    trocoMoedas = (troco*100) - (trocoNotas*100)
    #Nessa parte, o programa faz uma subtração dos valores sem casas decimais para, assim, utilizarmos as nossas funções
    #que serão chamadas.
    print(f'Valor pago: R${dinheiroDepositado:.2f}')
    if troco <= 0:
        print('=' * 30)
        print('Sem troco!')
    else:
        print('=' * 30)
        print(f'Troco: R${troco:.2f}')
        print('=' * 30)
        print('Pegue seu troco:')  
    imprimeNotas(trocoNotas) #Iremos chamar a função "imprimeNotas" para analisarmos somente a variavel relacionada as notas.
    imprimeMoedas(trocoMoedas) #Iremos chamar a função "imprimeMoedas" para analisarmos somente a variavel relacionada com as moedas.
    print('=' * 30)
    resp = input("Deseja fazer escolher outro produto (S/N)? ")
    print('=' * 30)
    if resp == "S" or resp == "s":
        limpaTela()
        if itemA == 0 and itemB == 0 and itemC == 0 and itemD == 0 and itemE == 0:
        #Essa parte funcionará da seguinte forma: quando o estoque dos produtos se esgotarem (ou seja, estarem todos indisponiveis)
        #essa condição fará com que o programa exiba uma mensagem alertando o usuário e, logo após, irá finalizar o programa.
            print('Desculpe...')
            print('Mas não possuímos produtos para vender. Tente mais tarde!')
            exit()
        else:
            maquina(itemA, itemB, itemC, itemD, itemE)
            #Essa parte funcionará da seguinte forma: quando o usuario solicitar uma nova compra nesse intervalo de tempo que ele
            #não reiniciou a máquina, a mesma irá chamar novamente a função "def maquina" com as suas variaveis dentro dos seus
            #parenteses modificada de acordo com a escolha passada feita pelo o usuário. 
    else:
        #Essa parte funcionará da seguinte forma: caso o usuário não queira mais fazer uma compra de um produto, a máquina irá
        #exibir uma mensagem de agradecimento e, logo após, finalizará o programa.
        if resp != "S" or resp != "s":
            print('Obrigado pela preferência.')
            print('Volte Sempre!!!')
            exit()
def main():
    limpaTela()
    maquina()

main()
