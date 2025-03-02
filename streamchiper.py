def text_to_bin(text):
    """Mengonversi teks menjadi representasi biner"""
    return ''.join(format(ord(char), '08b') for char in text)

def xor_encrypt(plaintext_bin, keystream_bin):
    # Pastikan panjang plaintext_bin dan keystream_bin sama
    if len(plaintext_bin) != len(keystream_bin):
        raise ValueError("Plaintext dan keystream harus memiliki panjang yang sama.")
    
    # Lakukan operasi XOR untuk setiap bit dalam plaintext_bin dan keystream_bin
    ciphertext_bin = ''
    for p, k in zip(plaintext_bin, keystream_bin):
        # XOR antara setiap bit plaintext_bin dan keystream_bin
        ciphertext_bin += str(int(p) ^ int(k))  # XOR antara bit
    
    return ciphertext_bin

def bin_to_text(binary_string):
    """Mengonversi biner kembali ke teks"""
    chars = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

def main():
    # Input dari pengguna dalam bentuk teks
    plaintext = input("Masukkan plaintext (teks biasa): ")
    keystream = input("Masukkan keystream (teks biasa): ")

    # Konversi teks ke biner
    plaintext_bin = text_to_bin(plaintext)
    keystream_bin = text_to_bin(keystream)

    # Pastikan panjang biner dari plaintext dan keystream sama
    if len(plaintext_bin) != len(keystream_bin):
        print("Error: Plaintext dan keystream harus memiliki panjang yang sama.")
        return
    
    # Proses enkripsi
    ciphertext_bin = xor_encrypt(plaintext_bin, keystream_bin)
    
    # Konversi ciphertext biner kembali ke teks
    ciphertext = bin_to_text(ciphertext_bin)
    
    # Output hasil enkripsi
    print(f"Plaintext  : {plaintext}")
    print(f"Keystream  : {keystream}")
    print(f"Ciphertext : {ciphertext}")

if __name__ == "__main__":
    main()
