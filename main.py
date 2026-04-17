class Talaba:
    def __init__(self, ism, talaba_id, kurs):
        self.ism = ism
        self.talaba_id = talaba_id
        self.kurs = kurs
    
    def __str__(self):
        return f"{self.ism} (ID: {self.talaba_id}, {self.kurs}-kurs)"

class Universitet:
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar = []
    
    def talaba_qosh(self, talaba):
        self.talabalar.append(talaba)
        print(f"✅ {talaba.ism} universitetga qo‘shildi.")
    
    def kurs_talabalari(self, kurs):
        result = [t for t in self.talabalar if t.kurs == kurs]
        print(f"\n📚 {kurs}-kurs talabalari:")
        for talaba in result:
            print(talaba)
        return result

# Test
uni = Universitet("Toshkent Davlat Universiteti")

t1 = Talaba("Azizbek", "TDU001", 2)
t2 = Talaba("Madina", "TDU002", 2)
t3 = Talaba("Sardor", "TDU003", 3)

uni.talaba_qosh(t1)
uni.talaba_qosh(t2)
uni.talaba_qosh(t3)

uni.kurs_talabalari(2)
