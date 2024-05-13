import pandas as pd
def jawaban_no1():

# Baca file Excel
data = pd.read_excel("nama_file.xlsx")

# Ubah kolom tanggal menjadi tipe data datetime jika belum
data['tanggal'] = pd.to_datetime(data['tanggal'])

# Filter data untuk entri yang terjadi pada bulan Mei
data_mei = data[(data['tanggal'].dt.month == 5)]

# Hitung jumlah entri untuk setiap orang
jumlah_orang = data_mei['nama_pelanggan'].nunique()

# Tampilkan jumlah orang yang berbelanja pada bulan Mei
print("Jumlah orang yang berbelanja pada bulan Mei:", jumlah_orang)

    