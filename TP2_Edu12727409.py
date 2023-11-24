def LeiaMatrizLocal(NomeArquivo):
    # retorna a matriz lida ou [] se houver algum erro
    # abrir o arquivo para leitura
    try:
        arq = open(NomeArquivo, "r")
    except:
        return [] # retorna lista vazia se deu erro
    # inicia matriz Sudoku a ser lida: 9 linhas x 9 colunas
    mat = [9 * [0] for k in range(9)]
    # ler cada uma das linhas do arquivo
    for linha in arq:
        v = linha.split() # elementos separados por espaços
        # verifica se tem 9 elementos e se são todos entre '1' e '9'
        # . . .
        # transforma de string para int se achar conveniente
        # . . .
        # outras consistências:
        # se não tem repetição nas linhas, colunas ou quadrados
    # . . .
    # fechar arquivo e retorna a matriz lida e consistida
    arq.close()
    return mat
#def Sudoku(Mat, Lin, Col): – função principal que preenche a matriz Sudoku, verificando se chegou ao final
# de uma solução e retrocedendo sempre que necessário.
def Sudoku(Mat, Lin, Col):
    for i in range(0,9):
        for x in range(0,9):
            if Mat[i][x] == 0:
                for number in range(1,10):
                    if TestaMatrizPreenchida(Mat, number, i, x):

                        Mat[i][x] == number
                        TestaMatrizCompleta(Mat)
                        Sudoku(Mat, Lin, Col)
                        Mat[i][x] == 0

                return Mat    
def TestaMatrizPreenchida(Mat, num, lin, col):
    contador = 0
    for x in range(0, 9):
        if(Mat[x][col] == num):
            return False
    for x in range(0, 9):
        if(Mat[lin][x] == num):
            return False
    quadrado1 = (lin // 3) * 3
    quadrado2 = (col // 3) * 3
    for i in range (0, 3):
        for x in range (0, 3):
            if(Mat[quadrado1 + i] [quadrado2 + x] == num):
                return False
    return True

def TestaMatrizCompleta(Mat):
    for i in range (0, 9):
        for x in range (0, 9): 
            if(Mat[i][x] == 0):
                contador += 1
    
    if(contador == 0):
        print(Mat)
