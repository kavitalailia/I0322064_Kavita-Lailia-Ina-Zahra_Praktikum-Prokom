mata_uang = {
    'IDR' : 1,
    'USD' : 0.000071,
}
uang = input("masukkan mata uang yang ingin dikonversi (IDR, USD): ")
nilai = int(input("masukan nilai uang: "))
print(mata_uang[uang]*nilai) 
