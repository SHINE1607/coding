

paths = 0
g = [[False for i in range(7)] for j in range (7)]

def f(y, x, i, m):
    global paths
    if i == 48:
        paths += 1
        return
    if g[6][0] == True:
        return 

    if (m == 'L' and (x == 0 or g[y][x-1] == True) and y > 0 and y < 6 and g[y-1][x] == False and g[y+1][x] == False):
        return 
    if (m == 'R' and (x == 6 or g[y][x+1] == True) and y > 0 and y < 6 and g[y-1][x] == False and g[y+1][x] == False):
        return 
    if (m == 'U' and (y == 0 or g[y-1][x] == True) and x > 0 and x < 6 and g[y][x-1] == False and g[y][x+1] == False):
        return 
    if (m == 'D' and (y == 6 or g[y+1][x] == True) and x > 0 and x < 6 and g[y][x-1] == False and g[y][x+1] == False):
        return 


    if s[i] == '?':
        r = [-1, 0, 1, 0]
        c = [0, -1, 0, 1]
        for j in range(4):
            yy = y + r[j]
            xx = x + c[j]
            if yy < 0 or yy > 6:
                continue
            if xx < 0 or xx > 6:
                continue
            if g[yy][xx] == True:
                continue
            g[yy][xx] = True
            f(yy, xx, i+1, 'ULDR'[j])
            g[yy][xx] = False
        return 



    if s[i] == "L":
        x -= 1
    elif s[i] == 'R':
        x += 1
    elif s[i] == 'U':
        y -= 1
    elif s[i] == 'D':
        y += 1
    if x < 0 or x > 6:
        return 
    if y < 0 or y > 6:
        return 
    if g[y][x] == True:
        return 
    g[y][x] = True
    f(y, x, i+1, s[i])
    g[y][x] = False
    return 

s = input()
g[0][0] = True
f(0, 0, 0, 0)
print(paths)