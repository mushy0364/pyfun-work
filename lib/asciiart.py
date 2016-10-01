'''Utility library of ASCII art functions'''

def join(these,sep=""):
    joined = ""
    tjoin = [str(i).split("\n") for i in these]
    longest = 0
    for t in tjoin:
        l = len(t)
        if l > longest: longest = l
    for i in range(longest):
        for j in range(len(tjoin)):
            joined += tjoin[j][i] + sep
        joined += "\n"
    return joined
