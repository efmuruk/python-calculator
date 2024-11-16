class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        if b < 0 :
            for i in range(-b):
                result = self.subtract(result, a)
        else :
            for i in range(b):
                result = self.add(result, a)
        return result

    def divide(self, a, b):
        result = 0
        sign = (a < 0 and b > 0) or (a > 0 and b < 0)
        b = -b if b < 0 else b
        a = -a if a < 0 else a
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        if sign == 1 :
            return  -result
        else :
            return result

    def modulo(self, a, b):
        d = self.divide(a,b)
        d = d-1 if (a < 0 and b > 0) or (a > 0 and b < 0) else d
        result = a - self.multiply(d,b)
        return result

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))