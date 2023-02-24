##Program ini ditulis oleh
##Nama: Mohammad Hatta
##NPM: 2006470685
##Soal Nomor 6

#mengimpor library python yang digunakan, yaitu matplotlib dan numpy

import matplotlib.pyplot as plt
import numpy as np

# Mendefinisikan range nilai x yang ingin dimasukkan oleh pengguna
x_min=input('Masukkan nilai x minimum: ')
x_max=input('Masukkan nilai x maksimum: ') 

#Memberikan input jumlah titik pada interval x_min dan x_max yang diinginkan oleh pengguna
print("Berapa banyak jumlah titik yang anda inginkan dalam interval " +"("+x_min + "," + x_max+")"+"?")
jumlah_titik=input('Masukkan jumlah titik yang diinginkan: ')
x = np.linspace(int(x_min), int(x_max), int(jumlah_titik))

# Mendefinisikan fungsi yang diberikan oleh soal sebagai variabel a, b, c
a = 3*x+4
b = 2 * x ** 2 + 1
c = x ** 3 + 3

# Membuat plot grafik fungsi yang diberikan dari soal sesuai dengan nilai range yang dimasukan oleh pengguna dan memberikannya judul 
plt.plot(x, a, label=' Grafik Fungsi y = 3x + 4')
plt.plot(x, b, label='Grafik Fungsi y = 2x\u00B2 + 1')
plt.plot(x, c, label='Grafik Fungsi y = x\u00B3 + 3')

# Memberi judul dan menambahkan garis horizontal dan vertikal pada titik origin (0,0)
plt.axhline(color='black',alpha=0.60)
plt.axvline(color='black',alpha=0.60)
plt.title('Grafik fungsi y=3x+4 , y= 2x\u00B2+1, dan y= x\u00B3+3')

# Menamakan label sumbu-x dan sumbu-y
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')

# Menampilkan keterangan grafik fungsi yang diberikan soal sebagai legenda dan menambahkan grid pada tampilan grafik
plt.legend()
plt.grid()

# Menampilkan grafik hasil plotting
plt.show()