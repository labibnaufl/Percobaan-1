print ('\nKelompok : 10')
print ('Sabtu, shift kedua')
print ('\nAnggota Kelompok :')
print ('1. Ahmad Aldani Herlangga (21120120140168)')
print ('2. Enrico Gathan Agung (21120123140127)')
print ('3. Naufal Labib Nugroho (21120123130109)')
print ('4. Rafi Rai Pasha Afandi (21120123100073)\n')
print('Shit got me tweakin')

print (100*('*'))
txt = 'HALLO BANK:D'
x = txt.center (100)
print (x)
print (100*('*'))

#LOOP 1
while True:
   pin = int(input('Silahkan masukan PIN Anda: '))
   if(pin == 888777):
      print('Selamat Datang Nasabah yang terhormat')
      break
   else:
      print('Invalid Option')

saldo = 100000

print('Menu: \n')
print('1. Cek saldo')
print('2. Tarik Tunai')
print('3. Keluar')

#LOOP 2
while True:
   pilihanNasabah = int(input('\nSilahkan masukkan pilihan Anda: '))
   print()

   if pilihanNasabah == 1:
      print (100*('*'))
      print(f'Saldo yang Tersisa saat ini adalah : Rp{saldo:}'.center(80))
      print (100*('*'))
      pilihanNasabah1 = input('\nApakah Anda ingin melanjutkan transaksi? (Yes/No): ')
      print()
      if pilihanNasabah1 != 'Yes':
         print (100*('*'))
         print('Terima kasih sudah bertransaksi dengan kami^^'.center(80))
         print (100*('*'))
         break

   elif pilihanNasabah == 2:
      jumlahTarik = int(input('Masukkan nominal yang anda inginkan: '))
      print()
      if saldo < jumlahTarik:
          print (100*('*'))
          print('Saldo Anda tidak mencukupi.'.center(80))
          print (100*('*'))
      else:
         saldo = saldo - jumlahTarik
         print (100*('*'))
         print(f'Silahkan ambil uang anda.\nSisa salso anda saat ini adalah : Rp{saldo:}')
         print (100*('*'))
      pilihanNasabah2 = input('\nApakah Anda ingin melanjutkan transaksi? (Yes/No): ')
      print()
      if pilihanNasabah2 != 'Yes':
         print (100*('*'))
         print('Terima kasih sudah bertransaksi dengan kami^^'.center(80))
         print (100*('*'))
         break
   
   elif pilihanNasabah == 3:
      pilihanNasabah = input("Apakah Anda yakin untuk keluar dari proses transaksi?. (Yes/No): ")
      if pilihanNasabah != 'No':
         print (100*('*'))
         print('Terima kasih sudah bertransaksi dengan kami^^'.center(80))
         print (100*('*'))
         break
   else:
      print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")



