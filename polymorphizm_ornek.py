# Geometrik Şekiller
class Sekil:
    def alan_hesapla(self):
        pass

class Kare(Sekil):
    def __init__(self, kenar):
        self.kenar = kenar
    
    def alan_hesapla(self):
        return self.kenar ** 2

class Daire(Sekil):
    def __init__(self, yaricap):
        self.yaricap = yaricap
    
    def alan_hesapla(self):
        return 3.14 * self.yaricap ** 2

# Kullanım
sekil1 = Kare(5)
sekil2 = Daire(3)

for sekil in [sekil1, sekil2]:
    print(f"Alan: {sekil.alan_hesapla()}")