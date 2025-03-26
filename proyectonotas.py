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

#history user 002

def login():
    user = input("Ingresa usuario")
    password = input("Crea una contraseña")
    if users.get(user) == password:
        print(f" Bienvenid, '{user}'")
        menu_principal(user)
    else:
        print ("Usuario o contraseña incorrectos")  

def menu_principal(user):
    while True:
        if user == "profesor":
            print("1. Ingrese Nota")
            print("2. Salir")
            option = input("Ingrese una opción:")
            if option == "1":
                register_notes()
            elif option == "2" :
                break
            else:
                print("Opción invalida") 
        else:
            print (" 1. Crear curso")
            print (" 2. Ver cursos")
            print ("3. Consultar Nota")
            print (" 4. Salir")
            option = input("Seleccione una opción:")
            if option == "1":
                crear_curso(user)
            elif option =="2":
                ver_cursos(user)
            elif option == "3":  
                consultar_nota(user)
            elif option == "4":
                break          
            else: print ("Opción invalida") 

#history user 003   

def crear_curso(user):
    name_subject = input("Escriba nombre Curso")
    if name_subject:
        if name_subject in subject[user]:
            print("Ya tiene el curso registrado")
        else:
            subject[user].append(name_subject)
            print(f"Curso registrado exitosamente '{name_subject}'")




  
