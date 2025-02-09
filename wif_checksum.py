import base58

def wifChecksum(wif):
    try:
        byte_str = base58.b58decode_check(wif)  # Decodes Base58Check, verifying checksum
        if byte_str[0] != 0x80:  # WIF private keys start with 0x80
            return False
        private_key_hex = byte_str[1:-1].hex()  # Extract private key (without prefix and checksum)
        if len(private_key_hex) > 64:
            private_key_hex = private_key_hex[:-2]  # Trim extra bytes
        return private_key_hex
    except:
        return False
