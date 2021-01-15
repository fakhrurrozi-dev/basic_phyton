Nama         = str(input("Nama :"))
nilaiTeori   = float(input("Nilai Teori :"))
nilaiPraktek = float(input("Nilai Praktek :"))
if nilaiPraktek and nilaiPraktek > 70:
    print("Selamat, Anda lulus!")
elif nilaiTeori > 70 and nilaiPraktek < 70:
    print("Anda harus mengulang ujian praktek")
elif nilaiTeori < 70 and nilaiPraktek > 70:
    print("Anda harus mengulang ujian teori")
else : 
    print("Anda harus mengulang ujian teori dan ujian praktek")