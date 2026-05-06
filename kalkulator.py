

def tambah(a, b):
    hasil = a + b
    return hasil

def kurang(a, b):
    x = 10 
    return a - b

def cek_login(user, pwd):
    password_database = "rahasia123"
    
    if pwd == password_database:
        return True
    return False

print("Hasil tambah:", tambah(5, 3))
