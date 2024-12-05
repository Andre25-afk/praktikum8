class DaftarNilaiMahasiswa:
    def __init__(self):
        self.data_mahasiswa = []

    def tambah(self, nama, nim, nilai_uts, nilai_uas, nilai_tugas):
        mahasiswa = {
            "nama": nama,
            "nim": nim,
            "nilai_uts": nilai_uts,
            "nilai_uas": nilai_uas,
            "nilai_tugas": nilai_tugas,
            "rata_rata": (nilai_uts + nilai_uas + nilai_tugas) / 3  # Menghitung rata-rata
        }
        self.data_mahasiswa.append(mahasiswa)
        print(f"Data {nama} berhasil ditambahkan.")

    def tampilkan(self):
        if not self.data_mahasiswa:
            print("Belum ada data mahasiswa.")
            return

        print("\nDaftar Nilai Mahasiswa:")
        print(f"{'No':<3} {'Nama':<15} {'NIM':<10} {'UTS':<5} {'UAS':<5} {'Tugas':<6} {'Rata-rata':<10}")
        print("-" * 60)
        for i, mhs in enumerate(self.data_mahasiswa, start=1):
            print(f"{i:<3} {mhs['nama']:<15} {mhs['nim']:<10} {mhs['nilai_uts']:<5} {mhs['nilai_uas']:<5} {mhs['nilai_tugas']:<6} {mhs['rata_rata']:<10.2f}")

    def hapus(self, nama):
        for mhs in self.data_mahasiswa:
            if mhs["nama"] == nama:
                self.data_mahasiswa.remove(mhs)
                print(f"Data {nama} berhasil dihapus.")
                return
        print(f"Data dengan nama {nama} tidak ditemukan.")

    def ubah(self, nama):
        for mhs in self.data_mahasiswa:
            if mhs["nama"] == nama:
                print(f"Data saat ini untuk {nama}:")
                print(f"NIM: {mhs['nim']}, UTS: {mhs['nilai_uts']}, UAS: {mhs['nilai_uas']}, Tugas: {mhs['nilai_tugas']}")
                mhs["nim"] = input("Masukkan NIM baru: ")
                mhs["nilai_uts"] = float(input("Masukkan nilai UTS baru: "))
                mhs["nilai_uas"] = float(input("Masukkan nilai UAS baru: "))
                mhs["nilai_tugas"] = float(input("Masukkan nilai Tugas baru: "))
                mhs["rata_rata"] = (mhs["nilai_uts"] + mhs["nilai_uas"] + mhs["nilai_tugas"]) / 3  # Mengupdate rata-rata
                print(f"Data {nama} berhasil diubah.")
                return
        print(f"Data dengan nama {nama} tidak ditemukan.")


# Contoh penggunaan program
daftar_nilai = DaftarNilaiMahasiswa()

while True:
    print("\nMenu:")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Ubah Data")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")
    
    if pilihan == "1":
        nama = input("Masukkan nama: ")
        nim = input("Masukkan NIM: ")
        nilai_uts = float(input("Masukkan nilai UTS: "))
        nilai_uas = float(input("Masukkan nilai UAS: "))
        nilai_tugas = float(input("Masukkan nilai Tugas: "))
        daftar_nilai.tambah(nama, nim, nilai_uts, nilai_uas, nilai_tugas)
    elif pilihan == "2":
        daftar_nilai.tampilkan()
    elif pilihan == "3":
        nama = input("Masukkan nama mahasiswa yang akan dihapus: ")
        daftar_nilai.hapus(nama)
    elif pilihan == "4":
        nama = input("Masukkan nama mahasiswa yang akan diubah: ")
        daftar_nilai.ubah(nama)
    elif pilihan == "5":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")