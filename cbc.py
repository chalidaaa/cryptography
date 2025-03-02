# Fungsi umum untuk enkripsi dan dekripsi
def char_to_binary(char):
    return format(ord(char), '08b')

def binary_to_char(binary):
    return chr(int(binary, 2))

def left_rotate(bits):  # Rotasi kiri
    return bits[1:] + bits[0]

def right_rotate(bits):  # Rotasi kanan
    return bits[-1] + bits[:-1]

def xor(bits1, bits2):
    return ''.join('1' if b1 != b2 else '0' for b1, b2 in zip(bits1, bits2))

# Fungsi enkripsi CBC
def encrypt_cbc(plaintext, iv, key):
    block_size = 4  # Ukuran blok 4 bit
    ciphertext_blocks = []  # Menyimpan hasil setiap blok ciphertext

    # Konversi plaintext menjadi biner dan bagi menjadi blok-blok 4 bit
    plaintext_binary = ''.join(char_to_binary(char) for char in plaintext)
    blocks = [plaintext_binary[i:i + block_size] for i in range(0, len(plaintext_binary), block_size)]

    # Tambahkan padding jika panjang blok terakhir kurang dari 4 bit
    if len(blocks[-1]) < block_size:
        blocks[-1] += '0' * (block_size - len(blocks[-1]))

    # Konversi IV dan Key ke biner, gunakan hanya 4 bit terakhir
    iv_binary = char_to_binary(iv)[-block_size:]
    key_binary = char_to_binary(key)[-block_size:]

    current_iv = iv_binary  # IV pertama
    for block in blocks:
        # XOR plaintext dengan IV
        xor_result = xor(block, current_iv)
        # XOR hasil dengan key (enkripsi)
        cipher_block = xor(xor_result, key_binary)
        # Lakukan rotasi kiri pada cipher block
        rotated_cipher_block = left_rotate(cipher_block)
        # Simpan hasil yang sudah dirotasi
        ciphertext_blocks.append(rotated_cipher_block)
        # Update IV untuk blok berikutnya
        current_iv = rotated_cipher_block

    # Gabungkan blok ciphertext dan ubah menjadi karakter
    ciphertext_binary = ''.join(ciphertext_blocks)
    ciphertext_chars = ''.join(binary_to_char(ciphertext_binary[i:i + 8]) for i in range(0, len(ciphertext_binary), 8))

    return ciphertext_chars

# Fungsi dekripsi CBC
def decrypt_cbc(ciphertext, iv, key):
    block_size = 4  # Ukuran blok 4 bit
    plaintext_blocks = []  # Menyimpan hasil setiap blok plaintext

    # Konversi ciphertext menjadi biner
    ciphertext_binary = ''.join(char_to_binary(char) for char in ciphertext)
    blocks = [ciphertext_binary[i:i + block_size] for i in range(0, len(ciphertext_binary), block_size)]

    # Konversi IV dan Key ke biner, gunakan hanya 4 bit terakhir
    iv_binary = char_to_binary(iv)[-block_size:]
    key_binary = char_to_binary(key)[-block_size:]

    current_iv = iv_binary  # IV pertama
    for block in blocks:
        # Rotasi kanan pada blok ciphertext
        rotated_cipher_block = right_rotate(block)
        # XOR hasil rotasi dengan key (dekripsi)
        xor_result = xor(rotated_cipher_block, key_binary)
        # XOR hasil dengan IV untuk mendapatkan plaintext asli
        plaintext_block = xor(xor_result, current_iv)
        # Simpan hasil plaintext blok
        plaintext_blocks.append(plaintext_block)
        # Update IV untuk blok berikutnya
        current_iv = block

    # Gabungkan blok plaintext dan ubah menjadi karakter
    plaintext_binary = ''.join(plaintext_blocks)
    plaintext_chars = ''.join(binary_to_char(plaintext_binary[i:i + 8]) for i in range(0, len(plaintext_binary), 8))

    return plaintext_chars

# Program utama dengan pilihan dan looping
def main():
    while True:
        print("\n--- Pilihan Menu ---")
        print("1. Enkripsi CBC")
        print("2. Dekripsi CBC")
        print("3. Exit")
        pilihan = input("Masukkan pilihan (1/2/3): ")

        if pilihan == '1':
            plaintext = input("Masukkan plaintext (string): ")
            iv = input("Masukkan IV (1 karakter): ")
            key = input("Masukkan key (1 karakter): ")
            ciphertext = encrypt_cbc(plaintext, iv, key)
            print("\nHasil Ciphertext:")
            print(ciphertext)

        elif pilihan == '2':
            ciphertext = input("Masukkan ciphertext (string): ")
            iv = input("Masukkan IV (1 karakter): ")
            key = input("Masukkan key (1 karakter): ")
            plaintext = decrypt_cbc(ciphertext, iv, key)
            print("\nHasil Plaintext (setelah dekripsi):")
            print(plaintext)

        elif pilihan == '3':
            print("Terima kasih telah menggunakan program ini!")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Jalankan program utama
if __name__ == "__main__":
    main()
