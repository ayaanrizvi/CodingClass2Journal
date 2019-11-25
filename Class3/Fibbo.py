# Fibbo.py
A = 1
B = 2
Next = 0
C = 0
D = 20
# print('First number:' ,A,'.')
# print('Second number:' ,B,'.')
while C<D:
    C=C+1
    Next=A+B
    A=B
    B=Next
print(D+2, ':number in sequence:' ,Next,'.')
input()
