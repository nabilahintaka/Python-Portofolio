def tambah_barang(belanjaan):
    nama_barang = input("Masukan nama item:  ")
    try:
        harga_barang = float(input("Masukan harga item:  "))
        belanjaan[nama_barang] = harga_barang
        print(f"\nBarang {nama_barang} berhasil ditambahkan ke keranjang. dengan harga: Rp. {harga_barang:.2f}.")
    except ValueError:
        print("\nError: Masukan harga harus berupa angka.")

def hapus_barang(belanjaan):
    nama_barang = input("Masukan nama item yang ingin dihapus:  ")
    if nama_barang in belanjaan:
        del belanjaan[nama_barang]
        print(f"\nBarang {nama_barang} berhasil dihapus.")
    else:
        print("\nError: Item yang anda cari tidak ditemukan.")

def lihat_barang(belanjaan):
    if not belanjaan:
        print("\nBelanjaan anda masih kosong. Silahkan tambahkan item.  ")
    else:
        print("\nBarang beralnaan anda:")
        for nama_barang, harga_barang in belanjaan.items():
            print(f"- {nama_barang}: Rp. {harga_barang:.2f}")

def hitung_total(belanjaan):
    total = sum(belanjaan.values())
    print(f"\nTotal harga barang belanjaan anda: Rp. {total:.2f}")

def main():
    belanjaan = {}
    while True:
        print("\nMenu:")
        print("1. Menambah barang")
        print("2. Hapus barang")
        print("3. Tampilkan barang di keranjang")
        print("4. Lihat total belanja")
        print("5. Exit")
        
        inputmenu = input("Pilihan: ")
        
        if inputmenu == '1':
            tambah_barang(belanjaan)
        elif inputmenu == '2':
            hapus_barang(belanjaan)
        elif inputmenu == '3':
            lihat_barang(belanjaan)
        elif inputmenu == '4':
            hitung_total(belanjaan)
        elif inputmenu == '5':
            print("Keluar dari program Toko kita. Terima kasih!")
            break
        else:
            print("")

if __name__ == "__main__":
    print("\nSelamat datang di Toko kita!")
    
    main()