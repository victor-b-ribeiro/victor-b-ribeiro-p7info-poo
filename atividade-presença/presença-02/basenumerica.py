
def printDecimal(num):
    return str(num)
def printOctal(num):
    return str(oct(num))[2:]
def printHexadecimal(num):
    return str(hex(num))[2:]
def printBinario(num):
    return str(bin(num))[2:]
def imprimirTabela():
    print("{:13s} {:7s} {:20s} {:13s}".format("Decimal","Octal", "Hexadecimal","Binário"))
    for i in range(226):
        print("{:13s} {:7s} {:20s} {:13s}".format("-"*13,"-"*7, "-"*20,"-"*13))
        print("{:13s} {:7s} {:20s} {:13s}".format(printDecimal(i),printOctal(i), printHexadecimal(i),printBinario(i)))



imprimirTabela()
