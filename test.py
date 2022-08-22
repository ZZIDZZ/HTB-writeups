import random,string

decode_this = "MmypTSPBJ{q6k_e1s_q1Ld8I}"
flag = "{Must be EZ}"
enc_flag = ""
random.seed("FINDIT")
for c in flag:
  if c.islower():
      enc_flag += chr((ord(c)-ord('a')+random.randrange(0,26))%26 + ord('a'))
  elif c.isupper():
      enc_flag += chr((ord(c)-ord('A')+random.randrange(0,26))%26 + ord('A'))
  elif c.isdigit():
      enc_flag += chr((ord(c)-ord('0')+random.randrange(0,10))%10 + ord('0'))
  else:
      enc_flag += c
print("Randomize Flag: "+ enc_flag)