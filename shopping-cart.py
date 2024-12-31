def tambah_barang(belanjaan):
    nama_barang = input("Enter item name: ")
    try:
        harga_barang = float(input("Enter price: "))
        belanjaan[nama_barang] = harga_barang
        print(f"\nItem {nama_barang} successfully added to cart. with price: Rp. {harga_barang:.2f}.")
    except ValueError:
        print("\nError: Price input must be a number.")

def hapus_barang(belanjaan):
    nama_barang = input("Enter the name of the item you want to delete:  ")
    if nama_barang in belanjaan:
        del belanjaan[nama_barang]
        print(f"\nItem {nama_barang}  has been successfully deleted from the shopping cart.")
    else:
        print("\nError: The item you are looking for was not found.")

def lihat_barang(belanjaan):
    if not belanjaan:
        print("\nYour cart is still empty. Please add items.  ")
    else:
        print("\nYour shopping items:")
        for nama_barang, harga_barang in belanjaan.items():
            print(f"- {nama_barang}: Rp. {harga_barang:.2f}")

def hitung_total(belanjaan):
    total = sum(belanjaan.values())
    print(f"\nTotal price of your shopping items: Rp. {total:.2f}")

def main():
    belanjaan = {}
    while True:
        print("\nMenu:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Show Item in Cart")
        print("4. View Total Purchase")
        print("5. Exit")
        
        inputmenu = input("Options: ")
        
        if inputmenu == '1':
            tambah_barang(belanjaan)
        elif inputmenu == '2':
            hapus_barang(belanjaan)
        elif inputmenu == '3':
            lihat_barang(belanjaan)
        elif inputmenu == '4':
            hitung_total(belanjaan)
        elif inputmenu == '5':
            print("See You! Thank you for shopping at Toko Kita.")
            break
        else:
            print("")

if __name__ == "__main__":
    print("\nWelcome to Toko kita!")
    
    main()
