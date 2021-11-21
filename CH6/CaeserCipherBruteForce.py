#!/usr/bin/python3

SYMBOL_TABLE = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz12345678"+ \
    "90 !?."

LEN_SYM_TABLE = len(SYMBOL_TABLE)

print("[+] Length of Symbol table is {}".format(LEN_SYM_TABLE))


def decrypt(c_message, key):
  plaintext = []
  for ch in c_message:
    pos = SYMBOL_TABLE.find(ch)
    if pos == -1:
      plaintext.append(ch)
      continue
    if pos - key < 0:
      pos = (pos - key) + LEN_SYM_TABLE
    else: 
      pos = (pos - key)

    plaintext.append(SYMBOL_TABLE[pos])

  return ''.join(plaintext)


## bruteforce across keylength of SYMBOL_TABLE

def bruteForceCaeserCipher(message):
  for key in range(LEN_SYM_TABLE):
    print("Key: {} -- {}".format(key,decrypt(message,key)))

if __name__ == '__main__':
  message = "avnl1olyD4l'ylDohww6DhzDjhuDil"
  bruteForceCaeserCipher(message)
