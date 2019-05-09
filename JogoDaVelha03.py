jogando = True  #torna a condição verdadeira, enquanto a condição for verdadeira, a função jogo sera executada
vez = 'X' #define a varia
import random # importa a funcao random(sorteio)
sorteio = ('1','2','3','4', '5', '6', '7', '8', '9') #variavel que tem como funcao informar a casa aleatoria na qual o computador ira joga 
qtd_jogadas = 0 #qtd_jogadas, sera utilizada para contabilizar o numero de jogadas(pois caso o jogo ultrapasse 8, sera encerrado)
#atribui uma string a cada variavel de casa
p1="1"
p2="2"
p3="3"
p4="4"
p5="5"
p6="6"
p7="7"
p8="8"
p9="9"

def reset_tab(): #reset_tab caso a funçao para continuar seja verdadeira, 'zera' o tabuleiro ou seja, reatribui numeros as variaveis de casa sendo possivel jogar novamente, assim como redefine a variavel do simbolo('x' ou 'o') e a quantidade de jogadas
    global p1, p2, p3, p4, p5, p6, p7, p8, p9,vez, qtd_jogadas, convidado  #chama as variaveis das casas, com a funcao global nao é necessaria defini-las novamente dentro da funcao
    p1="1"
    p2="2"
    p3="3"
    p4="4"
    p5="5"
    p6="6"
    p7="7"                                                     
    p8="8"
    p9="9"
    vez = 'X'
    qts_jogadas = 0
    convidado = ''

def show_tab():  #nos mostra o tabuleiro, assim como suas seguintes atualizacoes
    global p1, p2, p3, p4, p5, p6, p7, p8, p9  #chama as variaveis das casas, com a funcao global nao é necessaria defini-las novamente dentro da funcao
    hor=" | "               #'hor' e 'ver' mostram as repartiçoes esteticas do tabuleiro
    ver="\n---------"
    linha1=p1+hor+p2+hor+p3+ver                 #linha1, linha2 e linha3, mostram no tabuleiro as linhas com as suas respectivas posiçoes
    linha2=p4+hor+p5+hor+p6+ver
    linha3=p7+hor+p8+hor+p9
    print((linha1) + '\n' + (linha2) + '\n' + (linha3))

def valida_casa(c):                 #confere se a casa escolhida pode ser ocupada, nos retornando true or false.
    if c == '1':
        if p1 == '1':
            return True
    elif c=='2':
        if p2 == '2':
            return True
    elif c == '3':
        if p3 =='3':
            return True
    elif c =='4':
        if p4=='4':
            return True
    elif c == '5':
        if p5 == '5' :
            return True
    elif c=='6':
        if p6 == '6':
            return True
    elif c == '7':
        if p7 == '7':
            return True
    elif c == '8':
        if p8 == '8':
            return True
    elif c == '9':
        if p9 == '9':
            return True
    return False

def marca_casa(c):                   #substitui o valor numerico por um simbolo
    global p1, p2, p3, p4, p5, p6, p7, p8, p9, vez                #com a funcao global, nao é preciso redefinir as variaveis de casa
    if c == "1":
        p1 = vez                      # se c(que é a casa escolhida for igual ao numero(ou seja, nao foi preenchida por 'x' ou 'o',a respectiva casa sera marcada com o simbolo da 'vez', ou seja, de quem é a jogada
         
    elif c == "2":
        p2 = vez
         
    elif c =='3':
        p3 = vez
         
    elif c =='4':
        p4 = vez
        
    elif c == '5':
        p5 = vez
        
    elif c == '6':
        p6 = vez
         
    elif c =='7':
        p7 = vez
        
    elif c == '8':
        p8 = vez
        
    elif c =='9':
        p9= vez
        
    if vez == 'X':
        vez = 'O'
    else:
        vez = 'X' 


def teve_ganhador():  # a funcao verifica se houve um ganhador, ou seja, se a trilha perfeita foi formada
    global p1, p2, p3, p4, p5, p6, p7, p8, p9
    if p1==p2==p3 or p4==p5==p6 or p7==p8==p9 or p1==p4==p7 or p2==p5==p8 or p3==p6==p9 or p1==p5==p9 or p3==p5==p7:
            return True
    

def deu_velha(qtd_jogadas):         # verifica se deu velha, ou seja, se o numero de jogadas é superior a 8
    if qtd_jogadas>8:
        return True
        
def continuar():            
    jogando = input('Deseja continuar jogando"Y/N" ')
    if jogando == 'Y' or jogando == 'y':        #caso a resposta for sim(y) a condicao para jogar, ou seja, jogando == True, se tornara verdadeira, resetando assim o tabuleiro e o jogo
        jogador = ''
        reset_tab()
        return True
    if jogando == 'N' or jogando == 'n':                  #caso a resposta for nao (n), a condicao jogando sera falsa, ou seja, encera o jogo
        print ('Obrigado pela participação!!')
        return False
    else:                    #caso a informacao for invalida, chamara novamente a funçao, ate o valor inserido ser correto
        print ('Informação invalida!')
        return continuar()

jogando = True
def jogo():
    jogando = True
    global qtd_jogadas
    while jogando == True:
        show_tab()
        print ("Informe o nome do jogador")          
        convidado = input("Jogador: ")              #pega o nome dos jogadores
        computador = ''
        qtd_jogadas = 0
        
        while not deu_velha(qtd_jogadas) and not teve_ganhador():           #enquanto a definicao de deu_velha e teve_ganhador, executara a funcao do jogo
            
            j = ""          
            if vez == 'X':               #enquanto a vez for 'x', o jogador selecionado sera o primeiro
                j = convidado
            else:
                j = computador
                
            if j == convidado:
                c = input (convidado+ ', informe a casa a ser jogada: ')      # 3 - Pegar a casa que deseja jogar
                while not valida_casa(c):
                    c = input ('Informe a casa correta: ')
                              
            elif j == computador:
                import random
                c = random.choice(sorteio)
            
                
            if j == convidado:
                if valida_casa(c): #verifica se a casa jogada é valida, ou seja, se ainda nao esta ocupada
                    marca_casa(c)                       #marca a casa, ou seja, a impossibilita de ser jogada novamente
                    teve_ganhador()                     #verifica se ouve ganhador
                    qtd_jogadas = qtd_jogadas +1
                    show_tab()
                if valida_casa == False:
                    print ('Casa Invalida!!')           #caso contrario, informa que a casa selecionada é invalida, pedindo por outra
                    show_tab()              #etorna o tabuleiro pra uma melhor visualizacao das jogadas

            elif j == computador: 
                if valida_casa(c):          #caso a casa for valida, executa as seguintes funcoes:
                    marca_casa(c)               #marca a casa escolhida
                    teve_ganhador()             #verifica se houve um ganhador
                    qtd_jogadas = qtd_jogadas + 1           #contabiliza um no numero de jogadas
                    print ('O computador jogou na casa',c,':')          #nos informa a casa pela qual o computador optou
                    show_tab()      #nos informa o tabuleiro
                elif valida_casa == False:          #Caso a funcao for falsa, executa a seguinte funcao?
                    not show_tab()          #nao mostra o tabuleiro novamente
                    c = random.choice(sorteio)      #tenta mais uma vez achar uma casa valida na variavel 'sorteio' 
                    valida_casa(c)      #verifica se a casa é valida
                    marca_casa(c)           #marca a casa
                    teve_ganhador()         #verifica se teve ganhador
                    qtd_jogadas = qtd_jogadas +1                  #contabiliza mais uma jogada na variavel
            
            if teve_ganhador() == True:             #executa a funcao caso houver um ganhador
                if vez == 'X': 
                    j = computador      #retornara o computador como ganhador caso 
                    print ('    Lamentamos, mas o computador venceu!!')             #informa que o computador foi o vencedor
                else:
                    j = convidado #caso o 
                    print (convidado,",você ganhou!!")
                jogando = continuar()
                break 

                
            elif deu_velha(qtd_jogadas)== True:                 #executa a seguinte funcao, caso houver 'dado velha'
                show_tab()                              #nos mostra a tabela
                print ("Deu velha!")                    #informa a condição do jogo
                jogando = continuar()               #pede se quer prosseguir jogando

jogo()
