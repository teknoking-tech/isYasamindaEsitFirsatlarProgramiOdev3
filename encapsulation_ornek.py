# Banka Hesabı Örneği
class BankaHesabi:
    def __init__(self, hesap_sahibi, bakiye=0):
        self.__hesap_sahibi = hesap_sahibi  # Private değişken
        self.__bakiye = bakiye
    
    def para_yatir(self, miktar):
        if miktar > 0:
            self.__bakiye += miktar
            print(f"Yeni bakiye: {self.__bakiye}")
        else:
            print("Geçersiz miktar!")
    
    def bakiye_goster(self):
        return self.__bakiye

# Kullanım
hesap = BankaHesabi("Ahmet Yılmaz", 1000)
hesap.para_yatir(500)
print("Güncel Bakiye:", hesap.bakiye_goster())