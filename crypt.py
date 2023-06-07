import string
lowercase_alphabet = string.ascii_lowercase
print(lowercase_alphabet)
print(lowercase_alphabet[0])
text = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
new_text = ""

for char in text:
    if char in lowercase_alphabet:
        index = (lowercase_alphabet.index(char) + 10) % 26
        new_char = lowercase_alphabet[index]
        new_text += new_char
    else:
        new_text += char

print(new_text)

def cipher(text,pos):
  new_text = ""

  for char in text:
      if char in lowercase_alphabet:
        index = (lowercase_alphabet.index(char) + pos) % 26
        new_char = lowercase_alphabet[index]
        new_text += new_char
      else:
        new_text += char
  return(print(new_text))

reply = "hey vishal , i feel a bit low now . but i can't reduce my speed , i have to utilise my time effectively at any cot"
cipher(reply,-10)

f_msg = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
cipher(f_msg,10)
s_msg= "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
cipher(s_msg,14)
nc = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
cipher(nc,7)

v_msg= "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!"
key = "friends"





def vigenere_cipher(text, key):
    lowercase_alphabet = string.ascii_lowercase

    # Generate the key expansion
    key_expansion = ""
    key_length = len(key)
    text_length = len(text)
    repetitions = text_length // key_length
    remainder = text_length % key_length

    key_expansion = key * repetitions + key[:remainder]

    # Encrypt the text using the Vigenère cipher
    encrypted_text = ""
    for i in range(len(text)):
        char = text[i]
        key_char = key_expansion[i]

        if char in lowercase_alphabet:
            id1 = lowercase_alphabet.index(key_char)
            id2 = lowercase_alphabet.index(char)
            id3 = (id1 + id2) % 26
            encrypted_char = lowercase_alphabet[id3]
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
            key_expansion = key_expansion[:i] + " " + key_expansion[i:]

    return encrypted_text

# Example usage
#text = "hello world!"
#key = "secret"
encrypted_text = vigenere_cipher(v_msg, key)
print("Encrypted text:", encrypted_text)
