print("Welcome to the tic tac toe! You know the rules (and so do I...)\nYou will be playing against my codes ;D (bet you won't win) \nYou will be going first, represented by 'X'.")
name = str(input("Now, player, what is your name? \n"))

board = {1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9"}
valid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
auth = 0 
initial = "initial"
comp1 = "null"
second = "second"
comp2 = "null"
third = "third"
comp3 = "null"
fourth = "fourth"
comp4 = "null"
final = "final"
case = "undefined"

def win():
    print("HA you've been beaten ;) goodbye!")
    exit()

def  printboard(): 
    ln1 = [board[1], board[2], board[3]]
    ln2 = [board[4], board[5], board[6]]
    ln3 = [board[7], board[8], board[9]]
    print("\n", ln1, "\n", ln2, "\n", ln3, "\n") 

def playerturn(turn):
    global valid, board, auth, initial, second, third, fourth, final
    auth = 0 
    while auth == 0:  
        print("Now,", name,", let the challenge carry on.")
        take = str(input("Which spot would you like to place your 'X'?"))
        if  not take in valid: 
            print("invalid choice; input a number from 1 to 9 that is available on the board.")
            auth = 0
        else: 
            valid.remove(take)
            board[int(take)] = "X"
            if turn == "initial":
                initial = take
            elif turn == "second":
                second = take
            elif third == "third":
                third = take
            elif fourth == "fourth":
                fourth = take
            else: 
                final = take 
            auth = 1

def initialcheck():
    global valid, board, comp1, initial
    if initial == "5": 
        comp1 = "9"
    else:
        comp1 = "5"
    valid.remove(comp1)
    board[int(comp1)] = "O"

def secondcheck():
    global valid, board, comp2, case, initial, second
    #bC1
    if initial == "1" and second == "2" or initial == "2" and second == "1": 
        comp2  = "3"
        case = "bC1"
    #bC2
    if initial == "1" and second == "4" or initial == "4" and second == "1": 
        comp2  = "7"
        case = "bC2"
    #bC3
    if initial == "3" and second == "2" or initial == "2" and second == "3": 
        comp2  = "1"
        case = "bC3"
    #bC4
    if initial == "3" and second == "6" or initial == "6" and second == "3": 
        comp2  = "9"
        case = "bC4"
    #bC5
    if initial == "7" and second == "8" or initial == "8" and second == "7": 
        comp2  = "9"
        case = "bC5"
    #bC6
    if initial == "7" and second == "4" or initial == "4" and second == "7": 
        comp2  = "1"
        case = "bC6"
    #bC7
    if initial == "9" and second == "8" or initial == "8" and second == "9": 
        comp2  = "7"
        case = "bC7"
    #bC8
    if initial == "9" and second == "6" or initial == "6" and second == "9": 
        comp2  = "37"
        case = "bC8"
    #dC1
    if initial == "1" and second == "9" or initial == "9" and second == "1": 
        comp2  = "2"
        case = "dC1"
    #dC2
    if initial == "3" and second == "7" or initial == "7" and second == "3": 
        comp2  = "2"
        case = "dC2"
    #iC1
    if initial == "1" and second == "3" or initial == "3" and second == "1": 
        comp2  = "2"
        case = "iC1"
    #iC2
    if initial == "1" and second == "7" or initial == "7" and second == "1": 
        comp2  = "4"
        case = "iC2"
    #iC3
    if initial == "3" and second == "9" or initial == "9" and second == "3": 
        comp2  = "6"
        case = "iC3"
    #iC4
    if initial == "7" and second == "9" or initial == "9" and second == "7": 
        comp2  = "8"
        case = "iC4"
    #nbC1
    if initial == "1" and second == "6" or initial == "6" and second == "1": 
        comp2  = "3"
        case = "nbC1"
    #nbC2
    if initial == "1" and second == "8" or initial == "8" and second == "1": 
        comp2  = "7"
        case = "nbC2"
    #nbC3
    if initial == "3" and second == "4" or initial == "4" and second == "3": 
        comp2  = "1"
        case = "nbC3"
    #nbC4
    if initial == "3" and second == "8" or initial == "8" and second == "3": 
        comp2  = "9"
        case = "nbC4"
    #nbC5
    if initial == "7" and second == "2" or initial == "2" and second == "7": 
        comp2  = "1"
        case = "nbC5"
    #nbC6
    if initial == "7" and second == "6" or initial == "6" and second == "7": 
        comp2  = "9"
        case = "nbC6"
    #nbC7
    if initial == "9" and second == "2" or initial == "2" and second == "9": 
        comp2  = "3"
        case = "nbC7"
    #nbC8
    if initial == "9" and second == "4" or initial == "4" and second == "9": 
        comp2  = "7"
        case = "nbC8"
    #oC1
    if initial == "2" and second == "8" or initial == "8" and second == "2": 
        comp2  = "1"
        case = "oC1"
    #oC2
    if initial == "4" and second == "6" or initial == "6" and second == "4": 
        comp2  = "1"
        case = "oC2"
    #teC1
    if initial == "2" and second == "4" or initial == "4" and second == "2": 
        comp2  = "1"
        case = "teC1"
    #teC2
    if initial == "4" and second == "8" or initial == "8" and second == "4": 
        comp2  = "7"
        case = "teC2"
    #teC3
    if initial == "8" and second == "6" or initial == "6" and second == "8": 
        comp2  = "9"
        case = "teC3"
    #teC4
    if initial == "6" and second == "2" or initial == "2" and second == "6": 
        comp2  = "3"
        case = "teC4"
    #cC1
    if initial == "5" and second == "1":
        comp2 = "6"
        case = "cC1"
    #cC2
    if initial == "5" and second == "2":
        comp2 = "8"
        case = "cC2"
    #cC3
    if initial == "5" and second == "3":
        comp2 = "7"
        case = "cC3"
    #cC4
    if initial == "5" and second == "4":
        comp2 = "6"
        case = "cC4"
    #cC5
    if initial == "5" and second == "6":
        comp2 = "4"
        case = "cC5"
    #cC6
    if initial == "5" and second == "7":
        comp2 = "3"
        case = "cC6"
    #cC7
    if initial == "5" and second == "8":
        comp2 = "2"
        case = "cC7"
    valid.remove(comp2)
    board[int(comp2)] = 'O'

def check():
    global case
    if case == "bC1":
        bC1()
    if case == "bC2":
        bC2()
    if case == "bC3":
        bC3()
    if case == "bC4":
        bC4()
    if case == "bC5":
        bC5()
    if case == "bC6":
        bC6()
    if case == "bC7":
        bC7()
    if case == "bC8":
        bC8()
    if case == "dC1":
        dC1()
    if case == "dC2":
        dC2()
    if case == "iC1":
        iC1()
    if case == "iC2":
        iC2()
    if case == "iC3":
        iC3()
    if case == "iC4":
        iC4()
    if case == "nbC1":
        nbC1()
    if case == "nbC2":
        nbC2()
    if case == "nbC3":
        nbC3()
    if case == "nbC4":
        nbC4()
    if case == "nbC5":
        nbC5()
    if case == "nbC6":
        nbC6()
    if case == "nbC7":
        nbC7()
    if case == "nbC8":
        nbC8()
    if case == "oC1":
        oC1()
    if case == "oC2":
        oC2()
    if case == "teC1":
        teC1()
    if case == "teC2":
        teC2()
    if case == "teC3":
        teC3()
    if case == "teC4":
        teC4()
    if case == "cC1":
        cC1()
    if case == "cC2":
        cC2()
    if case == "cC3":
        cC3()
    if case == "cC4":
        cC4()
    if case == "cC5":
        cC5()
    if case == "cC6":
        cC6()
    if case == "cC7":
        cC7()

def bC1():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "7":
            comp3 = "4"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "4" or third == "6" or third == "8" or third == "9":
            comp3 = "7"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "6":
            comp4 = "9"
            valid.remove(comp4)
            board[int(comp4)] = "O"
        elif fourth == "9" or fourth == "8":
            comp4 = "6"
            board[int(comp4)] = "O"
            printboard()
            win()
    
def bC2():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "3":
            comp3 = "2"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "2" or third == "6" or third == "8" or third == "9":
            comp3 = "3"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "8":
            comp4 = "9"
            valid.remove(comp4)
            board[int(comp4)] = "O"
        elif fourth == "6" or fourth == "9":
            comp4 = "8"
            board[int(comp4)] = "O"
            printboard()
            win()

def bC3():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "9":
            comp3 = "6"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "4" or third == "6" or third == "7" or third == "8":
            comp3 = "3"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "4":
            comp4 = "7"
            valid.remove(comp4)
            board[int(comp4)] = "O"
        elif fourth == "7" or fourth == "8":
            comp4 = "4"
            board[int(comp4)] = "O"
            printboard()
            win()

def bC4():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "1":
            comp3 = "2"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "2" or third == "4" or third == "7" or third == "8":
            comp3 = "1"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null":
        if fourth == "8":
            comp4 = "7"
            valid.remove(comp4)
            board[int(comp4)] = "O"
        elif fourth == "4" or fourth == "7":
            comp4 = "8"
            board[int(comp4)] = "O"
            printboard()
            win()

def bC5():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "1":
            comp3 = "4"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "2" or third == "3" or third == "4" or third == "6":
            comp3 = "1"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "6":
            comp4 = "3"
            valid.remove(comp4)
            board[int(comp4)] = "O"
        elif fourth == "2" or fourth == "3":
            comp4 = "6"
            board[int(comp4)] = "O"
            printboard()
            win()

def bC6():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "9":
            comp3 = "8"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "2" or third == "3" or third == "6" or third == "8":
            comp3 = "9"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "2":
            comp4 = "3"
            valid.remove(comp4)
            board[int(comp4)] = "O"
        elif fourth == "3" or fourth == "4":
            comp4 = "2"
            board[int(comp4)] = "O"
            printboard()
            win()

def bC7():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "3":
            comp3 = "6"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "1" or third == "2" or third == "4" or third == "6":
            comp3 = "3"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "4":
            comp4 = "1"
            valid.remove(comp4)
            board[int(comp4)] = "O"
        elif fourth == "1" or fourth == "2":
            comp4 = "4"
            board[int(comp4)] = "O"
            printboard()
            win()

def bC8():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "7":
            comp3 = "8"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "1" or third == "2" or third == "4" or third == "8":
            comp3 = "7"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "2":
            comp4 = "1"
            valid.remove(comp4)
            board[int(comp4)] = "O"
        elif fourth == "1" or fourth == "4":
            comp4 = "2"
            board[int(comp4)] = "O"
            printboard()
            win()

def dC1():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "8":
            comp3 = "7"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "3" or third == "4" or third == "6" or third == "7":
            comp3 = "8"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "3":
            comp4 = "6"
            valid.remove(comp4)
            board[int(comp4)] = "O"
        elif fourth == "4" or fourth == "6":
            comp4 = "3"
            board[int(comp4)] = "O"
            printboard()
            win()

def dC2():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "8":
            comp3 = "9"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "1" or third == "4" or third == "6" or third == "9":
            comp3 = "8"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "1":
            comp4 = "4"
            valid.remove(comp4)
            board[int(comp4)] = "O"
        elif fourth == "4" or fourth == "6":
            comp4 = "1"
            board[int(comp4)] = "O"
            printboard()
            win()

def iC1():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "8":
            comp3 = "4"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "4" or third == "6" or third == "7" or third == "9":
            comp3 = "8"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "6":
            comp4 = "9"
            valid.remove(comp4)
            board[int(comp4)] = "O"
        elif fourth == "7" or fourth == "9":
            comp4 = "6"
            board[int(comp4)] = "O"
            printboard()
            win()

def iC2():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "6":
            comp3 = "2"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "2" or third == "3" or third == "8" or third == "9":
            comp3 = "6"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "8":
            comp4 = "9"
            valid.remove(comp4)
            board[int(comp4)] = "O"
        elif fourth == "3" or fourth == "9":
            comp4 = "8"
            board[int(comp4)] = "O"
            printboard()
            win()

def iC3(): 
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "4":
            comp3 = "2"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "1" or third == "2" or third == "7" or third == "8":
            comp3 = "4"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "8":
            comp4 = "7"
            valid.remove(comp4)
            board[int(comp4)] = "O"
        elif fourth == "1" or fourth == "7":
            comp4 = "8"
            board[int(comp4)] = "O"
            printboard()
            win()

def iC4():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "7":
            comp3 = "8"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "1" or third == "2" or third == "4" or third == "8":
            comp3 = "7"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "2":
            comp4 = "1"
            valid.remove(comp4)
            board[int(comp4)] = "O"
        elif fourth == "1" or fourth == "4":
            comp4 = "2"
            board[int(comp4)] = "O"
            printboard()
            win()

def nbC1():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "7":
            comp3 = "4"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "2" or third == "4" or third == "8" or third == "9":
            comp3 = "7"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "9":
            comp4 = "8"
            valid.remove(comp4)
            board[int(comp4)] = "O"
        elif fourth == "2" or fourth == "8":
            comp4 = "9"
            valid.remove(comp4)
            board[int(comp4)] = "O"
 
def nbC2():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "3":
            comp3 = "2"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "2" or third == "4" or third == "6" or third == "9":
            comp3 = "3"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "9":
            comp4 = "6"
            valid.remove(comp4)
            board[int(comp4)] = "O"
        elif fourth == "4" or fourth == "6":
            comp4 = "9"
            valid.remove(comp4)
            board[int(comp4)] = "O"

def nbC3():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "9":
            comp3 = "6"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "2" or third == "6" or third == "7" or third == "8":
            comp3 = "9"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "7":
            comp4 = "8"
            valid.remove(comp4)
            board[int(comp4)] = "O"
        elif fourth == "2" or fourth == "8":
            comp4 = "7"
            valid.remove(comp4)
            board[int(comp4)] = "O"

def nbC4():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "1":
            comp3 = "2"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "2" or third == "4" or third == "6" or third == "7":
            comp3 = "1"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "7":
            comp4 = "6"
            valid.remove(comp4)
            board[int(comp4)] = "O"
        elif fourth == "4" or fourth == "6":
            comp4 = "7"
            valid.remove(comp4)
            board[int(comp4)] = "O"

def nbC5():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "9":
            comp3 = "8"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "3" or third == "4" or third == "6" or third == "8":
            comp3 = "9"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "3":
            comp4 = "6"
            valid.remove(comp4)
            board[int(comp4)] = "O"
        elif fourth == "4" or fourth == "6":
            comp4 = "3"
            valid.remove(comp4)
            board[int(comp4)] = "O"

def nbC6():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "1":
            comp3 = "4"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "2" or third == "3" or third == "4" or third == "6":
            comp3 = "1"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "3":
            comp4 = "2"
            valid.remove(comp4)
            board[int(comp4)] = "O"
        elif fourth == "2" or fourth == "8":
            comp4 = "3"
            valid.remove(comp4)
            board[int(comp4)] = "O"

def nbC7():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "7":
            comp3 = "8"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "1" or third == "4" or third == "6" or third == "8":
            comp3 = "7"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "1":
            comp4 = "4"
            valid.remove(comp4)
            board[int(comp4)] = "O"
        elif fourth == "4" or fourth == "6":
            comp4 = "1"
            valid.remove(comp4)
            board[int(comp4)] = "O"

def nbC8():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "3":
            comp3 = "6"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "1" or third == "2" or third == "6" or third == "8":
            comp3 = "3"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "1":
            comp4 = "2"
            valid.remove(comp4)
            board[int(comp4)] = "O"
        elif fourth == "2" or fourth == "8":
            comp4 = "1"
            valid.remove(comp4)
            board[int(comp4)] = "O" 

def oC1():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "9":
            comp3 = "7"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "3" or third == "4" or third == "6" or third == "7":
            comp3 = "9"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "4":
            comp4 = "3"
            board[int(comp4)] = "O"
            printboard()
            win()
        if fourth == "6":
            comp4 = "4"
            board[int(comp4)] = "O"
            printboard()
            win()
        if fourth == "3":
            comp4 = "4"
            board[int(comp4)] = "O"
            printboard()
            win()
    
def oC2():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "9":
            comp3 = "3"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "2" or third == "3" or third == "7" or third == "8":
            comp3 = "9"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "2":
            comp4 = "7"
            board[int(comp4)] = "O"
            printboard()
            win()
        if fourth == "7":
            comp4 = "2"
            board[int(comp4)] = "O"
            printboard()
            win()
        if fourth == "8":
            comp4 = "2"
            board[int(comp4)] = "O"
            printboard()
            win()

def teC1():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "9":
            comp3 = "3"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "3" or third == "6" or third == "7" or third == "8":
            comp3 = "9"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "7":
            comp4 = "8"
            valid.remove(comp4)
            board[int(comp4)] = "O"
        elif fourth == "6" or fourth == "8":
            comp4 = "7"
            board[int(comp4)] = "O"
            printboard()
            win()

def teC2():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "3":
            comp3 = "9"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "1" or third == "2" or third == "6" or third == "9":
            comp3 = "3"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "1":
            comp4 = "2"
            valid.remove(comp4)
            board[int(comp4)] = "O"
        elif fourth == "2" or fourth == "6":
            comp4 = "1"
            board[int(comp4)] = "O"
            printboard()
            win()

def teC3():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "1":
            comp3 = "3"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "2" or third == "3" or third == "4" or third == "7":
            comp3 = "1"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "7":
            comp4 = "4"
            valid.remove(comp4)
            board[int(comp4)] = "O"
        elif fourth == "2" or fourth == "4":
            comp4 = "7"
            board[int(comp4)] = "O"
            printboard()
            win()

def teC4():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "7":
            comp3 = "1"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "1" or third == "4" or third == "8" or third == "9":
            comp3 = "1"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "9":
            comp4 = "8"
            valid.remove(comp4)
            board[int(comp4)] = "O"
        elif fourth == "4" or fourth == "8":
            comp4 = "9"
            board[int(comp4)] = "O"
            printboard()
            win()

def cC1():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "7":
            comp3 = "2"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "2" or third == "3" or third == "4" or third == "6":
            comp3 = "7"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "4":
            comp4 = "6"
            valid.remove(comp4)
            board[int(comp4)] = "O"
        elif fourth == "6" or fourth == "3":
            comp4 = "4"
            valid.remove(comp4)
            board[int(comp4)] = "O"

def cC2():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "7":
            comp3 = "3"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "1" or third == "3" or third == "4" or third == "6":
            comp3 = "7"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "6":
            comp4 = "4"
            valid.remove(comp4)
            board[int(comp4)] = "O"
        elif fourth == "1" or fourth == "4":
            comp4 = "6"
            board[int(comp4)] = "O"
            printboard()
            win()

def cC3():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "8":
            comp3 = "2"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "1" or third == "2" or third == "4" or third == "6":
            comp3 = "8"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "4":
            comp4 = "6"
            valid.remove(comp4)
            board[int(comp4)] = "O"
        elif fourth == "6" or fourth == "3":
            comp4 = "4"
            valid.remove(comp4)
            board[int(comp4)] = "O"

def cC4():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "3":
            comp3 = "7"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "1" or third == "2" or third == "7" or third == "8":
            comp3 = "3"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "8":
            comp4 = "2"
            valid.remove(comp4)
            board[int(comp4)] = "O"
        elif fourth == "1" or fourth == "2":
            comp4 = "8"
            board[int(comp4)] = "O"
            printboard()
            win()

def cC5():
    global comp3, third, board, valid
    if third == "1":
        comp3 = "2"
        cC5C1()
    if third == "7":
        comp3 = "3"
        cC5C2()
    if third == "3":
        comp3 = "7"
        cC5U()
    if third == "2":
        comp3 = "8"
        cC5E1()
    if third == "8":
        comp3 = "2"
        cC5E2()
    if comp3 != "null" and fourth == "fourth":
        valid.remove(comp3)
        board[int(comp3)] = 'O'

def cC5C1():
    global comp4, fourth, board, valid
    if fourth == "3" or fourth == "4":
        comp4 = "7"
    if fourth == "7":
        comp4 = "3"
    valid.remove(comp4)
    board[int(comp4)] = 'O'
    
def cC5C2():
    global comp4, fourth, board, valid
    if fourth == "1" or fourth == "2":
        comp4 = "8"
    if fourth == "8":
        comp4 = "2"
    valid.remove(comp4)
    board[int(comp4)] = 'O'

def cC5U():
    global comp4, fourth, board
    if fourth == "1" or fourth == "2":
        comp4 = "8"
    if fourth == "8":
        comp4 = "1"
    board[int(comp4)] = "O"
    printboard()
    win() 

def cC5E1():
    global comp4, fourth, board, valid
    if fourth == "1" or fourth == "3":
        comp4 = "7"
        board[int(comp4)] = "O"
        printboard()
        win()
    if fourth == "7":
        comp4 = "3"
        valid.remove(comp4)
        board[int(comp4)] = 'O'

def cC5E2():
    global comp4, fourth, board, valid
    if fourth == "1" or fourth == "7":
        comp4 = "3"
    if fourth == "3":
        comp4 = "7"
    valid.remove(comp4)
    board[int(comp4)] = 'O'

def cC6():
    global comp3, third, comp4, fourth, board, valid, final
    if comp3 == "null":
        if third == "6":
            comp3 = "4"
            valid.remove(comp3)
            board[int(comp3)] = "O"
        elif third == "1" or third == "2" or third == "4" or third == "8":
            comp3 = "6"
            board[int(comp3)] = "O"
            printboard()
            win()
    if comp3 != "null" and comp4 == "null": 
        if fourth == "8":
            comp4 = "2"
            valid.remove(comp4)
            board[int(comp4)] = "O"
        elif fourth == "1" or fourth == "2":
            comp4 = "8"
            valid.remove(comp4)
            board[int(comp4)] = "O"
#there's something wrong with cC5 and cC7
def cC7():
    global comp3, third, board, valid
    if third == "1":
        comp3 = "4"
        cC7C1()
    if third == "3":
        comp3 = "7"
        cC7C2()
    if third == "7":
        comp3 = "3"
        cC7U()
    if third == "4":
        comp3 = "6"
        cC7E1()
    if third == "6":
        comp3 = "4"
        cC7E2()
    if comp3 != "null" and fourth == "fourth":
        valid.remove(comp3)
        board[int(comp3)] = 'O'

def cC7C1():
    global comp4, fourth, board, valid
    if fourth == "7" or fourth == "6":
        comp4 = "3"
    if fourth == "3":
        comp4 = "7"
    valid.remove(comp4)
    board[int(comp4)] = 'O'
    
def cC7C2():
    global comp4, fourth, board, valid
    if fourth == "1" or fourth == "4":
        comp4 = "6"
    if fourth == "6":
        comp4 = "4"
    valid.remove(comp4)
    board[int(comp4)] = 'O'

def cC7U():
    global comp4, fourth, board
    if fourth == "1" or fourth == "4":
        comp4 = "6"
    if fourth == "6":
        comp4 = "1"
    board[int(comp4)] = "O"
    printboard()
    win() 

def cC7E1():
    global comp4, fourth, board, valid
    if fourth == "1" or fourth == "7":
        comp4 = "3"
        board[int(comp4)] = "O"
        printboard()
        win()
    if fourth == "3":
        comp4 = "7"
        valid.remove(comp4)
        board[int(comp4)] = 'O'

def cC7E2():
    global comp4, fourth, board, valid
    if fourth == "1" or fourth == "7":
        comp4 = "3"
    if fourth == "3":
        comp4 = "7"
    valid.remove(comp4)
    board[int(comp4)] = 'O'

printboard()
playerturn(initial) #- player
printboard()
initialcheck() #- computer
print("computer turn...")
printboard()
playerturn(second) #- player
printboard()
secondcheck() #- computer
print("computer turn...")
printboard()
playerturn(third) #-player
printboard()
check() #-computer
print("computer turn...")
printboard()
playerturn(fourth) #- player
printboard()
check() #- computer
print("computer turn...")
printboard()
playerturn(final) #- player
printboard()
print("computer.. wait.\nTIE! You can't beat me. Have a nice day..")
#exit()