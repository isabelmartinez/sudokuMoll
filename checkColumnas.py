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
    
correcto = [[1, 2, 3], #caso test 1
            [2, 3, 1], #el código pasa este caso test
            [3, 1, 2]] #>>>Correcto

incorrecto1 = [[1, 2, 3, 4], #caso test 2
               [2, 3, 1, 3],#el código pasa el caso test
               [3, 1, 2, 3],#>>>Inconrrecto
               [4, 4, 4, 4]]

incorrecto2 = [[1, 2, 3, 4],#caso test 3
               [2, 3, 1, 4],#el código pasa el caso test
               [4, 1, 2, 3],#>>>Incorrecto
               [3, 4, 1, 2]]

incorrecto3 = [[1,2,3,4],#caso test 4
            [2,3,1,3],#el código pasa este caso test
            [3,1,2,3],#>>>Incorrecto
            [4,4,4,2]]
