# Hayvan Sesleri
class Hayvan:
    def ses_cikar(self):
        print("Ses çıkarıyor...")

class Kedi(Hayvan):
    def ses_cikar(self):
        print("Miyav!")

class Kopek(Hayvan):
    def ses_cikar(self):
        print("Hav Hav!")

# Kullanım
hayvanlar = [Hayvan(), Kedi(), Kopek()]
for hayvan in hayvanlar:
    hayvan.ses_cikar()