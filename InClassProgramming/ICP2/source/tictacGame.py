def board_draw(h,w): #3*3
    for temp in range(h):  #range function
        print(" --- " * w)
        print("|    " * w, end="")
        print("|")
    print(" --- " * w)

heightinp= int(input("Enter the height of the board: "))
widthinp= int(input("Enter the width of the board: "))
board_draw(heightinp,widthinp)