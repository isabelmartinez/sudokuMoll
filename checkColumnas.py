def checkColumnas(sudoku):

    # precondiciones

    # postcondiciones
    indexFila = 0
    for fila1 in sudoku:
        fila1 = sudoku[indexFila]
        indexElemento = 0
        for elemento in fila1:
            elemento = fila1[indexElemento]
            for fila in sudoku:
                if fila!=fila1 and fila[indexElemento]==elemento:
                    return False
            
            indexElemento+=1
        indexFila+=1
    return True

### CASOS TEST ###

if __name__ == '__main__':
    
    import casosTestSudoku
    
correcto = [[1, 2, 3],
            [2, 3, 1],
            [3, 1, 2]]
print checkColumnas(sudoku)
#>>>True
incorrecto1 = [[1, 2, 3, 4],
               [2, 3, 1, 3],
               [3, 1, 2, 3],
               [4, 4, 4, 4]]
print checkColumnas(sudoku)
#>>>False
incorrecto2 = [[1, 2, 3, 4],
               [2, 3, 1, 4],
               [4, 1, 2, 3],
               [3, 4, 1, 2]]
print checkColumnas(sudoku)
#>>>False
