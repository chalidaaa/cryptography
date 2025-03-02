def text_to_binary(text):
    # Mengkonversi tiap karakter ke biner dg format 8 bit
    binary = ' '.join(format(ord(char), '08b') for char in text)
    return binary

def binary_to_text(binary):
    # Memisahkan biner per 8 bit, lalu konversi ke karakter
    text = ''.join(chr(int(b, 2)) for b in binary.split())
    return text

def main_menu():
    while True:
        # Pilih opsi convert
        print("\nChalida Abdat - A11.2023.15031")
        print("\nPilih opsi:")
        print("1. Teks ke Biner")
        print("2. Biner ke Teks")
        print("3. Exit")

        choice = input("Masukkan pilihan (1/2/3): ")

        if choice == '1':
            # Input teks dan konversi ke biner
            input_text = input("Masukkan teks yang ingin dikonversi ke biner: ")
            binary_output = text_to_binary(input_text)
            print(f"Teks '{input_text}' dalam biner adalah: {binary_output}")
        elif choice == '2':
            # Input biner dan konversi ke teks
            input_binary = input("Masukkan biner yang ingin dikonversi ke teks: ")
            text_output = binary_to_text(input_binary)
            print(f"Biner '{input_binary}' dalam teks adalah: {text_output}")
        elif choice == '3':
            # Exit program
            print("Terima kasih! Program berakhir. -chalida")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

# Do the main program
main_menu()