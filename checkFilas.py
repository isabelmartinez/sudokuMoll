# Esta funcion usa 2 for para recorrer la lista, la primera para sacar las
# filas y la segunda para sacar los numeros de cada fila. En cada fila cuenta
# las veces que se repite el numero, si se repite mas de 1 vez devuelve false.


def checkFilas(sudoku):
    for fila in sudoku:
        for numero in fila:
            repeticiones = fila.count(numero)
            if repeticiones > 1:
                return False
    return True


# ## CASOS TEST ###
if __name__ == '__main__':
    import casosTestSudoku
# Añadida la libreria de colores para ponerlo bonito. :>
    import class_bcolors_enum

    casosTest = [casosTestSudoku.correct,  casosTestSudoku.incorrect, casosTestSudoku.incorrect2, casosTestSudoku.incorrect3, casosTestSudoku.irregular, casosTestSudoku.irregular2]
    for (offset, test) in enumerate(casosTest):
        if (offset == 1 or offset == 2):
            if checkFilas(test):
                print("Caso %s => %s" % (offset, checkFilas(test)), class_bcolors_enum.Colors.FAIL + "FAIL" + class_bcolors_enum.Colors.ENDC)
            else:
                print("Caso %s => %s" % (offset, checkFilas(test)), class_bcolors_enum.Colors.OKGREEN + "OK" + class_bcolors_enum.Colors.ENDC)
        else:
            if checkFilas(test):
                print("Caso %s => %s" % (offset, checkFilas(test)), class_bcolors_enum.Colors.OKGREEN + "OK" + class_bcolors_enum.Colors.ENDC)
            else:
                print("Caso %s => %s" % (offset, checkFilas(test)), class_bcolors_enum.Colors.FAIL + "FAIL" + class_bcolors_enum.Colors.ENDC)
