#
# SE578-Assignment #1
# Abhilasha Jayaswal
# A51.py
#
#This code implements A51 cryptosystem
#
#Initializing the Registers
X=[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
Y=[1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1]
Z=[1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0]

#Calculating the key bit stream
def key_bit_stream(A, B, C):
    return str(A[18]^B[21]^C[22]);

#calculating the major amongst the given bits
def maj(A, B, C):
    sol = ((X[8]&Y[10]) ^ (X[8]&Z[10]) ^ (Y[10]&Z[10]));
    return sol;

#Implementing A51
def TestA51():
    print "Initially Registers:";
    print "\nX=", X;
    print "\nY=", Y;
    print "\nZ=", Z;
    x=len(X)-1;
    y=len(Y)-1;
    z=len(Z)-1;
    key_stream = "";
    for i in range(0,32,1):
        m=maj(X, Y, Z);
        if X[8] == m:
            t=X[13]^X[16]^X[17]^X[18];
            for index in range(x,0,-1):
                X[index] = X[index - 1];
            X[0]=t;
        if Y[10] == m:
            t=Y[20]^Y[21];
            for index in range(y,0,-1):
                Y[index] = Y[index - 1];
            Y[0]=t;
        if Z[10] == m:
            t=Z[7]^Z[20]^Z[21]^Z[22];
            for index in range(z,0,-1):
                Z[index] = Z[index - 1];
            Z[0]=t;
        key_stream=+key_stream+key_bit_stream(X, Y, Z);
    print "\n 32 bit keystream for the given A51 is: ", key_stream;
    print "Finally Registers:";
    print "\nX=", X;
    print "\nY=", Y;
    print "\nZ=", Z;

TestA51();

