#history user 001

users = [] #save user
note =[] #save note
subject =[] #subject

def menu_inicio():
    while True:
        print("1. Registrar Usuario")
        print("2. Inicia Sesion")
        print("3. Salir")
        option = input("Selecciona una opción")
        if option =="1":
            register_user()
        elif option == "2":
            login()
        elif option == "3":
            print("Salir")
            break
        else:
            print("Ingrese opción 1 , 2 o 3") 

def register_user():
    user = input("Ingresa usuario")
    password = input("Crea una contraseña")
    if user and password:
        users[user] = password
        subject[user] = []
        print("Usuario registrado con exito")  

def login():
    user = input("Ingresa usuario")
    password = input("Crea una contraseña")
    if users.get(user) == password:
        print(f" Bienvenid, {user}")
        
    else:
        print ("Usuario o contraseña incorrectos")    
