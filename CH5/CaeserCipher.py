#!/usr/bin/python3

SYMBOL_TABLE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

LEN_TABLE = len(SYMBOL_TABLE)

def encrypt(message, sub_number=3):
  cipher = []
  for ch in message:
    if not ch.isalnum():
      cipher.append(ch)
      continue
    pos = SYMBOL_TABLE.find(ch)
    if pos + sub_number > LEN_TABLE:
      pos = (pos + sub_number) - LEN_TABLE
    else:
      pos = pos + sub_number

    cipher.append(SYMBOL_TABLE[pos])

  return ''.join(cipher)



def decrypt(c_message, sub_number=3):
  plain_text = []
  for ch in c_message:
    # without isalnum method
    # this makes handling symbols better
    pos = SYMBOL_TABLE.find(ch)
    if pos == -1:
      plain_text.append(ch)
      continue
    if pos - sub_number < 0:
      pos = (pos - sub_number) + LEN_TABLE
    else:
      pos = pos - sub_number

    plain_text.append(SYMBOL_TABLE[pos])

  return ''.join(plain_text)

if __name__ == '__main__':
  print("[+] Caeser Cipher Program")
  print("[+] Length table {}".format(LEN_TABLE))
  print("[+] Cipher text of 'This is my world' is \
      {}".format((encrypt('This is my world'))))
  print("[+] Decrypt the strin 'Wklv lv p1 zruog' is {}".format(decrypt(\
  'Kv?uqwpfu?rncwukdng?gpqwijB',2)))

