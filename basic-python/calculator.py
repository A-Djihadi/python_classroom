def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division par zero n'est pas permise"
      
def modulus(a, b):
    return a % b   

def exponent(a, b):
    return a ** b

def floor_division(a, b):
    return a // b   

def calculator():
    print("Bonjour chez le calculateur !")
    print("Selection de l'operation :")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulo")
    print("6. Exponentiel")
    print("7. Division entière")

    choice = input("Entrer votre choix (1-7): ")

    if choice in ['1', '2', '3', '4', '5', '6', '7']:
        num1 = float(input("Entrez le premier nombre: "))
        num2 = float(input("Entrez le deuxième nombre: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            print(f"{num1} % {num2} = {modulus(num1, num2)}")
        elif choice == '6':
            print(f"{num1} ** {num2} = {exponent(num1, num2)}")
        elif choice == '7':
            print(f"{num1} // {num2} = {floor_division(num1, num2)}")
    else:
        print("Entrée invalide")
        
        
if __name__ == "__main__":
    calculator()