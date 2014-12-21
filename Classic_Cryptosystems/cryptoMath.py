"""
"Problem Solving with Algorithims and data structures unsing python"
    - modexp : Modular Exponentiation 
    - gcd : Greatest common divisor
    - ext_gcd : extended euclidian algorithm
        - (used to find multiplicable inverse)
"""

def modexp(x, n, p):
    """
    Recursive definition for x^n (mod p)
    """
    if n == 0:
        return 1
    t = (x*x)%p
    tmp = modexp(t, n//2, p)
    if n%2 !=0:
        tmp = (tmp*x)%p
    return tmp

def gcd(a,b):
    """
    Greastest common divisor
    """
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def ext_gcd(x,y):
    """
    Extended Eucild's Algorithm:
        - Used to find the multiplicative inverse
        - Deriving the equation:
            - d = ay + b(x mod y)
            - d = ay + b(x - (x//y)y)
            - d = ay + bx - (x//y)by
            - d = bx + ay - (x//y)by
            - d = bx + (a - (x//y)b)y
    """
    if y == 0:
        return (x, 1, 0)
    else:
        (d, a, b) = ext_gcd(y, x%y)
        return (d, b, a-(x//y)*b)

if __name__ == "__main__":
    print("gcd(5,19): ", gcd(5,19))
    print("gcd(20, 100): ", gcd(20, 100))
    print("ext_gcd(5,19): ", ext_gcd(5,19))
    print("modexp(5,8,7): ", modexp(5, 8, 7))
