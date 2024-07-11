a = 'A'
b = 'B'
c = 1.1
string = 'b={nome2} a={0} a={0} a={0} c={nome3:.2f}'
formato = string.format(a, nome2=b, nome3=c)

print(formato)