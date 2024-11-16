import datetime
import qrcode

def hitung_harga(tipe, jumlah, hari):
    harga = {
        'Pelajar': (25000, 35000),
        'Umum': (50000, 70000),
        'Anak': (20000, 30000),
        'WNA': (100000, 150000)
    }
    
    if hari in ['Sabtu', 'Minggu']:
        return harga[tipe][1] * jumlah
    return harga[tipe][0] * jumlah

def cetak_resi(tipe, jumlah, total_harga, metode_pembayaran):
    now = datetime.datetime.now()
    tanggal = now.strftime("%A, %d %B %Y, %H:%M")
    
    print("\n=== Wisata Arung Jeram Joss ===")
    print(tanggal)
    print(f"Tiket {tipe}: {jumlah} x Rp{total_harga // jumlah} = Rp{total_harga}")
    print(f"Metode Pembayaran: {metode_pembayaran}")
    
    if metode_pembayaran == "QRIS":
        qr_data = f"Pembayaran QRIS: {tipe}, Jumlah: {jumlah}, Total: Rp{total_harga}"
        qr = qrcode.make(qr_data)
        qr.show() 
        qr.save("qris_payment.png")  
        print("QR Code telah dibuat dan disimpan sebagai 'qris_payment.png'.")

    print("Semoga hari anda menyenangkan!")

def main():
    print("Selamat datang di Wisata Arung Jeram Joss!")
    
    hari = input("Masukkan hari (Senin - Minggu): ").capitalize()
    tipe = input("Masukkan tipe tiket (Pelajar/Umum/Anak/WNA): ").capitalize()
    jumlah = int(input(f"Masukkan jumlah tiket {tipe}: "))
    
    print("\nTipe Pembayaran:")
    print("(1) Tunai")
    print("(2) QRIS")
    print("(3) Kartu Kredit")
    print("(4) Debit")
    
    try:
        metode_pembayaran_index = int(input("Pilih metode pembayaran (1-4): "))
        metode_pembayaran = ""
        if metode_pembayaran_index == 1:
            metode_pembayaran = "Tunai"
        elif metode_pembayaran_index == 2:
            metode_pembayaran = "QRIS"
        elif metode_pembayaran_index in [3, 4]:
            metode_pembayaran = "Kartu"
        else:
            raise ValueError("Pilihan tidak valid.")
    except ValueError:
        print("Input tidak valid. Silakan pilih angka 1-4.")
        return

    total_harga = hitung_harga(tipe, jumlah, hari)
    cetak_resi(tipe, jumlah, total_harga, metode_pembayaran)

if __name__ == "__main__":
    main()
