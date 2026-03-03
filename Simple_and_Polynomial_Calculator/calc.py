class Simplemath:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def addition(self):
        return self.a+self.b+self.c

    def substraction(self):
        return self.a-self.b-self.c

    def multiplication(self):
        return self.a*self.b*self.c

    def division(self):
        try:
            result = self.a/self.b/self.c
            return result
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."

class Polycalc:
    def __init__(self, a, b, c):
        if a == 0:
            print("no solution as coefficient 'a' is 0")
        self.a=a
        self.b=b
        self.c=c

    def roots(self):
        a=self.a
        b=self.b
        c=self.c
        ac=a*c
        
        pairs=False
        for m in range(-abs(ac),abs(ac)+1):
            if m!=0 and ac%m==0:
                n=ac//m
                if m+n==b:
                    pairs=True
                    print(f"pairs: ({a}x+({m}))(x+{int(n/a)})")
                    break
        if not pairs:
            print("no roots")
            return

        d=-m/a
        e=-n/a
        print("roots",d,",",e)





