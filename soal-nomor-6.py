##Program ini ditulis oleh
##Nama: Mohammad Hatta
##NPM: 2006470685
##Soal Nomor 6

#mengimpor library python yang digunakan, yaitu matplotlib dan numpy

import matplotlib.pyplot as plt
import numpy as np

# Mendefinisikan range nilai x yang ingin dimasukkan oleh pengguna
x1=input('Masukkan nilai x minimum: ')
x2=input('Masukkan nilai x maksimum: ')
x3=input('Masukkan jumlah titik yang diinginkan: ')

x = np.linspace(int(x1),int(x2), int(x3))

# Mendefinisikan fungsi yang diberikan oleh soal sebagai variabel a, b, c
a = 3*x+4
b = 2 * x ** 2 + 1
c = x ** 3 + 3

# Membuat plot grafik fungsi yang diberikan dari soal dan memberikannya judul 
plt.plot(x, a, label=' Grafik Fungsi y = 3x + 4')
plt.plot(x, b, label='Grafik Fungsi y = 2x\u00B2 + 1')
plt.plot(x, c, label='Grafik Fungsi y = x\u00B3 + 3')
plt.title('Grafik fungsi y=3x+4 , y= 2x\u00B2+1, dan y= x\u00B3+3')

#Menamakan label sumbu-x dan sumbu-y, serta menampilkan keterangan setiap grafik fungsi sebagai legenda
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')
plt.legend()
plt.grid()

# Menampilkan grafik hasil plotting
plt.show()
