from random import randint #importando modulo e função para usar rando

board = []#lista vazia

for i in range(0, 5): #loop que imprime 5 listas de "O" para tabuleiro d jogo
    board.append(['O'] * 5)

def print_board(board):#função q imprime as listas alinhadas p jogo
    for i in board:
        print(" ".join(i))#usando .join para imprimir melhor tabuleiro

print_board(board) #chamando função

def random_row(board): #função q escolhe numero aleatoriamente
    return randint(0, len(board) -1)

def random_col(board): #função q escolhe numero aleatoriamente
    return randint(0, len(board[0]) -1)

ship_row = random_col(board)#armazemando numero aleatorio na variavel
ship_col = random_row(board)#armazemando numero aleatorio na variavel

for turn in range(4):
    print("turno:", turn + 1)
    guess_row = int(input("Digite a linha: "))#pedindo para usuario digitar as
    guess_col = int(input("Digite a coluna: "))#coordenadas

    if guess_row == ship_row and guess_col == ship_col:#se para se o usurio
        print("Parabens! Você afundou o navio!")#acertou
        break
    elif guess_row not in range(5) or guess_col not in range(5):
        print("Oops, fora do oceano")#se para usuario numero fora;
    elif board[guess_row][guess_col] == "X":
        print("Você já acertou este local.")
    else:
        print("Você errou o navio de guerra!")#usuario errou
        board[guess_row][guess_col] = "X"#marcar com um "X" o erro
        print_board(board)#imprimir o tabuleiro atualizado

if turn == 3:
    print("Game Over")