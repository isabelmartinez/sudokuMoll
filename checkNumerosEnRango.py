
def checkNumerosEnRango(sudoku):

    # precondiciones
    for fila in sudoku:
        for elemento in fila:
            if isinstance(elemento, int):
                if elemento < 1 or elemento > len(fila):
                    return False
                else:
                    pass
            else:
                return False
    return True

    # postcondiciones


### CASOS TEST ###

if __name__ == '__main__':

    from casosTestSudoku import *

    if checkNumerosEnRango(correct):
        print("OK")
    else:
        print("FAIL")
    if checkNumerosEnRango(incorrect):
        print("OK")
    else:
        print("FAIL")
    if checkNumerosEnRango(incorrect2):
        print("OK")
    else:
        print("FAIL")
    if checkNumerosEnRango(incorrect3):
        print("OK")
    else:
        print("FAIL")
    if checkNumerosEnRango(incorrect4):
        print("OK")
    else:
        print("FAIL")
    if checkNumerosEnRango(incorrect5):
        print("OK")
    else:
        print("FAIL")
    if checkNumerosEnRango(irregular):
        print("OK")
    else:
        print("FAIL")
    if checkNumerosEnRango(irregular2):
        print("OK")
    else:
        print("FAIL")
