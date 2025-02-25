def pad(message: bytes) -> bytes:
    block_size = 16
    pad_len = block_size - (len(message) % block_size)

    padding = bytes([pad_len] * pad_len)
    return message + padding

m = b"Example message."
padded_m = pad(m)
print("Original:", m)
print("Padded:", padded_m)
