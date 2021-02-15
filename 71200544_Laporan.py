#IMMANUEL JOY PERKASA/71200544

'''
Pak Budi memperoleh gaji pertamanya sebesar Rp 2.000.000 perbulan. Apabila Pak Budi sudah bekerja dengan kurun
waktu satu tahun, maka penghasilannya akan meningkat 5% (dari gaji pertama) per tahunnya. Dari penghasilan Pak Budi, terdapat 
penghasilan yang tidak terkena pajak sebesar 40% dari gaji yang diperoleh. Jika pajak penghasilan diketahui 10%,
Berapakah besar gaji yang diterima Pak Budi per bulan pada tahun ke-3 beliau bekerja?

gaji=gaji pertama pak budi
naik=persentase kenaikan gaji tiap tahunnya
nonpajak=persentase penghasilan yang tidak terkena pajak
pph=pajak penghasilan
tahun=kurun waktu pak budi bekerja
'''
'''
input
gaji=Rp.2.000.000/bulan
naik=5%/tahun dari gaji pertama
nonpajak=40% dari gaji yang diperoleh
pph=10% dari gaji yang terkena pajak
tahun=ke-3 

proses
hasil kenaikan gaji pertahun(a)=(((tahun*naik)*gaji)+gaji)
besar penghasilan yang terkena pajak(b)=gaji-nonpajak
besar penghasilan pajak(c)=b*pph
gaji yang diperoleh setelah terkena pajak(d)=a-c

output
Besar gaji yang diterima Pak Budi pada tahun ke 3 beliau bekerja.
'''
gaji=int(input('Masukkan gaji pertama(Rp.): '))
naik=int(input('Masukkan persentase kenaikan gaji tiap tahunnya(%): '))
nonpajak=int(input('Masukkan persentase gaji yang tidak terkena pajak(%): '))
pph=int(input('Masukkan besar penghasilan pajak(%): '))
tahun=int(input('Masukkan lama kurun waktu bekerja(tahun): '))
a=((tahun*naik/100)*gaji)+gaji
b=a-(nonpajak/100*a)
c=b*pph/100
d=a-c

print('Besar gaji yang diterima Pak Budi pada tahun ke',tahun,'beliau bekerja adalah (Rp.):',d)




