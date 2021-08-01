question = int(input("Quel est votre nombre ? "))

#Crash de Py Charm

if question >=40:
    print("🛠🛠 LE SYSTEME PYCHARM NE REPONDS PLUS, VEUILLEZ RELANCER LE PROGRAMME. 🛠🛠")
    raise SystemExit

#Risque de gros lag

if question >=33:
    print("🛠🛠 ATTENTION, veuillez patienter, cela peut prendre quelques instants. 🛠🛠")

def Fibonacci (x):
    if (x == 0 or x == 1):
        return 1
    else:
        return Fibonacci(x-1) + Fibonacci(x-2)

print(Fibonacci(question))