def encrypt(key, fin, fout, *, block = 1 << 16):
    import cryptography.fernet, struct
    fernet = cryptography.fernet.Fernet(key)
    with open(fin, 'rb') as fi, open(fout, 'wb') as fo:
        while True:
            chunk = fi.read(block)
            if len(chunk) == 0:
                break
            enc = fernet.encrypt(chunk)
            fo.write(struct.pack('<I', len(enc)))
            fo.write(enc)
            if len(chunk) < block:
                break

def decrypt(key, fin, fout):
    import cryptography.fernet, struct
    fernet = cryptography.fernet.Fernet(key)
    with open(fin, 'rb') as fi, open(fout, 'wb') as fo:
        while True:
            size_data = fi.read(4)
            if len(size_data) == 0:
                break
            chunk = fi.read(struct.unpack('<I', size_data)[0])
            dec = fernet.decrypt(chunk)
            fo.write(dec)
def encrypt_or_decrypt_file(filename, key_file, outFile,mode="encrypt"):
    with open(key_file, 'rb') as f:
        key = f.read()
    if mode == "encrypt":
        encrypt(key, filename, outFile)
    elif mode == "decrypt":
        decrypt(key, filename, outFile)
    else: 
        print("Unknown Mode")
        raise
    
def test():
    import cryptography.fernet, secrets
    key = cryptography.fernet.Fernet.generate_key()
    
    with open('key.key', 'wb') as f:
        f.write(key)
    #encrypt(key, "1624 - Mein Lokal, Dein Lokal - Die 'alte Ziege' erfüllt alle Wünsche-7075192.mp4", 'data.enc')
    #decrypt(key, 'data.enc', 'data.out')
    #with open('data.out', 'rb') as f:
    #    assert data == f.read()

if __name__ == '__main__':
    test()
