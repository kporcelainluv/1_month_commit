from functools import reduce
L = ['Floating-point', 'calculations', 'the', 'presence'+',','not', 'the', 'absence', 'of', 'bugs']
d = reduce(lambda x, y: x+" "+y, L)
print(d)
