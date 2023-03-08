import  random, string

def CrearPassword(n):
    todas=list(string.acsii_letters)+list(string.digits)+list(string.punctuation)
    Password= []

    for i in range(n):
        tmp =random.choice(todas)
        Password.append(tmp)
    res = "".join(Password)
    return res

n = int(input("Introduce la longitud de tu Contraseña: "))
test = CrearPassword(n)
print(test)