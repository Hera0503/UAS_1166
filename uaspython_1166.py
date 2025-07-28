import streamlit as st

# Kelas Mahasiswa
class Pasien:
    def __init__(self, id, nama, usia, diagnosa):
      self.id = id  
      self.nama = nama
      self.usia = usia
      self.diagnosa = diagnosa

    def __str__(self):
      return f"id: {self.id}, Nama: {self.nama}, Usia: {self.usia}, Diagnosa: {self.diagnosa}"

# Data disimpan di list session_state
if 'data_pasien' not in st.session_state:
    st.session_state.data_pasien = []

# Tampilan utama
#format berupa judul/bold
st.title("Manajemen Pasien Rumah Sakit")

#format peenulisan biasa
st.write("### Pilihan Menu:")
st.write("1. Lihat Data")
st.write("2. Tambah Data")
st.write("3. Ubah Data")
st.write("4. Hapus Data")

menu = st.text_input("Masukkan angka menu (1-4):")

# Fungsi menu
if menu == "1":
    st.subheader("📄 Daftar Pasien")
    if st.session_state.data_pasien:
        for i, psn in enumerate(st.session_state.data_pasien):
            st.write(f"{i+1}. {psn}")
    else:
        st.info("Belum ada data.")

elif menu == "2":
    st.subheader("➕ Tambah Pasien")
    id = st.text_input("Masukkan id")
    nama = st.text_input("Masukkan Nama")
    usia = st.text_input("Masukkan Usia")
    diagnosa = st.text_input("Masukkan diagnosa")
    if st.button("Simpan"):
        if id and nama:
            psn = Pasien(id, nama, usia, diagnosa)
            st.session_state.data_pasien.append(psn)
            st.success("Data berhasil ditambahkan.")
        else:
            st.warning("Harap isi semua kolom.")

elif menu == "3":
    st.subheader("✏️ Ubah Pasien")
    data = st.session_state.data_pasien
    data = st.session_state.data_pasien
    if data:
        st.write("Daftar Pasien:")
        for i, psn in enumerate(data):
            st.write(f"{i+1}. {psn}")
            
        pilihan = st.number_input("Pilih nomor pasien yang ingin diubah:", min_value=1, max_value=len(data), step=1)
        selected = data[pilihan-1]
        
        new_nama = st.text_input("Nama baru", value=selected.nama)
        new_usias = st.text_input("Usia baru", value=selected.usia)
        new_diagnosa = st.text_input("Diagnosa baru", value=selected.diagnosa)
        
        if st.button("Simpan Perubahan"):
            selected.nama = new_nama
            selected.usia = new_usias
            selected.diagnosa = new_diagnosa
            st.success("Data berhasil diubah!")
    else:
        st.info("Belum ada data.")

elif menu == "4":
    st.subheader("🗑️ Hapus Pasien")
    data = st.session_state.data_pasien
    if data:
        st.write("Daftar Pasien:")
        for i, psn in enumerate(data):
            st.write(f"{i+1}. {psn}")
            
        pilihan = st.number_input("Pilih nomor pasien yang ingin dihapus:", min_value=1, max_value=len(data), step=1)
        
        if st.button("Hapus"):
            deleted = data.pop(pilihan-1)
            st.success(f"Data {deleted.nama} berhasil dihapus!")
    else:
        st.info("Belum ada data.")

elif menu != "":
    st.warning("Masukkan angka 1 - 4 sesuai menu.")
