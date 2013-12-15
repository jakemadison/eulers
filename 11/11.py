#!/usr/bin/python2
# -*- coding: utf-8
#stub for #11

# In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
#
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
#
# What is the greatest product of four adjacent numbers in the same direction
# (up, down, left, right, or diagonally) in the 20×20 grid?

grid = [
    [8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
    [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
    [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
    [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
    [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
    [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
    [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
    [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
    [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
    [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
    [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
    [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
    [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
    [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
    [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
    [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
    [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
    [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
    [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
    [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]
]


#give me a list, i'll give you the product:
def return_total(n):
    tot = 1
    for x in n:
        tot *= x

    return tot


#no real reason to have a left, this should get all of them
def right(r, n):
    if (len(grid[r]) - n) >= 5:
        return grid[r][n:n+5]
    else:
        return False


#ugly, but it works:
def down(r, n):
    ar = []  # holds our down slice
    for each in grid:
        ar.append(each[n])

    if len(ar[r:r+5]) >= 5:
        return ar[r:r+5]
    else:
        return False


def diagonal(r, n):
    print grid[r+1][n+1]
    print grid[r+2][r+2]


def testing():
    mx = 0
    mx_arr = []

    for yind, y in enumerate(grid):
        for xind, y in enumerate(y):
            temp = down(xind, yind)
            if temp and len(temp) >= 5:
                final = return_total(temp)

            if final and final > mx:
                mx = final
                mx_arr = temp

            temp = right(xind, yind)

            if temp and len(temp) >= 5:
                final2 = return_total(temp)

            if final2 and final2 > mx:
                mx = final
                mx_arr = temp

    print mx, mx_arr


# given a set of coordinates, who are my neighbours?
def find_neighbours(r, n):
    rts = []
    dns = []
    lefs = []
    ups = []

    #i bet i can replace this for loop with slices

    if (len(grid[r]) - n) >= 5:
        rts.append(grid[r][n:n+5])  # find ns to the right of me


    lefs.append(grid[r][n:n-5:-1])

    #yeah, this ain't workin '
    if (len(grid) - r) >= 5:
        dns.append(grid[r:r+5][n])  # find ns below me

    #gets tricky here:


    #ah fuck. you can't slice UP stupid. This is not a matrix, but a list of lists
    # wait, then why does down work?
    #ups.append(grid[r:r-5:-1][n])

    print rts
    print dns
    print lefs
    print ups


find_neighbours(0, 0)


print 'done!'

crap = [0,1,2,3,4,5]

#start at 5, go backwards to 0, do it in steps of -1
# for mine it will be start at position n within grid r, go back.. crap how many, it's relative to n

a = 1
print crap[a:a+2]

# okay, wait.  should i be considering this as iterating through the types
# of possible lines that can be formed from the grid,
# or, from each point's point of view.
# eg, I am a point, who are my neighbours? out of those neighbours,
# can I create a row of 5? or better, what's my highest row of five that I can generate??
# since it's just the answer they're are looking for, multiple positives are OK.