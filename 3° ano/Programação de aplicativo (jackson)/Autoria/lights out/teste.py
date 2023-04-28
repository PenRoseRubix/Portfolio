import random
grid = []

def ramdom():
    if grid == []:
        print("grid does not exisist")
        return
    y = 0
    for i in grid:
        x = 0
        for j in i:
            grid[y][x] = False
            x +=1
        y += 1
   
    y = 0
    for row in grid:
        x = 0
        for col in row:
            if  random.choice([True, False]) == True:
                flip_switch(y,x)
            x +=1
        y += 1
            
def creat_grid():
    grid_h = int
    grid_l = int
    grid.clear()
    while grid_h == int or grid_l == int:
        try:
            grid_h = int(input("Enter grid high: "))
            grid_l = int(input("And lengh: "))
        except:
            print("unexpected value. enter a integer in both inputs")
    if grid_h > 26 or grid_h < 1:
        grid_h = 26
    if grid_l > 10 or grid_l < 1:
        grid_l = 10
    for i in range(grid_h):
        rowmaker = []
        for j in range(grid_l):
            rowmaker.append(True)
        grid.append(rowmaker)
    
def display():
    gridframe = "  "
    for i in range(len(grid[0])):
        gridframe = gridframe + str(i+1)+ " "
    print(gridframe)
    rowcount = 1
    for row in grid:
        rowdisplay = str(chr(rowcount+96)) + " "
        for col in row:
            if col == True:
                rowdisplay = rowdisplay + "▣ "
            elif col == False:
                rowdisplay = rowdisplay + "▢ "
            else:
                rowdisplay = rowdisplay + "? "
        print(rowdisplay)
        rowcount += 1
    return

def isdone():
    y = 0
    for row in grid:
        x = 0
        for col in row:
            if grid[y][x] == True:
                return False
            x +=1
        y += 1
    print("you win")
    return True

def next_command():
    comm = input("-> ")
    if comm[0] =="/":
        if comm[1:] == "shuf":
            ramdom()
            return

        elif comm[1:] == "size":
            creat_grid()
            return

        elif comm[1:] == "dis":
            display()
            return

        elif comm[1:] == "help":
            print("Swich tiles by typing a leter and a nunber(in that order) \nexemple 'a1' or 'b2' \ncommands are made with a / at the begging\nthe following commands are")
            print("/help to show commands\n/shuf to randomize the grid\n/size to rezise the grid(this will restart your game)\n/dis to display the grid")
            return
        

        elif comm[1:] == "quit":
            y = 0
            for i in grid:
                x = 0
                for j in i:
                    grid[y][x] = False
                    x +=1
                y += 1
            return
        else:
            print("invalid command")
            return
    if len(comm) < 2:
        print("invalid command")
        return
    if comm[0] not in "abcdefghijklmnopqrstuvwxyz":
        print("invalid command")
        return
    if comm[1:] not in "12345678910":
        print("invalid comand")
        return
    if comm[1] == "0":
        print("invalid comand")
        return
    
    
    flip_switch(int(ord(comm[0]) -96) -1, int(comm[1:]) -1)

def flip_switch(cord_h, cord_l):
    print(cord_h)
    print(cord_l)
    if cord_h > len(grid)-1 or cord_l > len(grid[0])-1:
        print("move is out of range of the grid")
        return

    grid[cord_h][cord_l] =  not grid[cord_h][cord_l]
    if not cord_h + 1 > len(grid) -1:
        grid[cord_h+1][cord_l] =  not grid[cord_h+1][cord_l]
    if not (cord_h - 1) < 0:
        grid[cord_h - 1][cord_l] =  not grid[cord_h - 1][cord_l]

    if not cord_l + 1 > len(grid[0]) - 1:
        grid[cord_h][cord_l + 1] =  not grid[cord_h][cord_l+1]
    if not (cord_l - 1) < 0:
        grid[cord_h][cord_l -1] =  not grid[cord_h][cord_l-1]

creat_grid()
ramdom()
display()
print("type '/help' to show commands and how to play")
while isdone() == False:
    next_command()
    display()