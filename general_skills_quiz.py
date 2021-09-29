# DownUnderCTF2021 
# Misc Challenge : General Skills Quiz 

from pwn import *
from urllib.parse import unquote
from base64 import b64decode, b64encode
from string import ascii_lowercase

# Host to Connect to
address = ("pwn-2021.duc.tf", 31905)
r = remote(address[0], address[1])

print(r.recvuntil("...").decode())
r.sendline()

# Add 1 + 1
print(r.recvuntil(":").decode())
r.sendline(b'2')

# Base10 to Hex
print(r.recvuntil(":").decode())
d = r.recvline().decode().strip()[2:]
r.sendline(str(int(d, 16)).encode())

# Hex to ASCII
print(r.recvuntil(":").decode())
d = r.recvline().decode().strip()
r.sendline(chr(int(d, 16)).encode())

# URL encoded to ASCII
print(r.recvuntil(":").decode())
d = r.recvline().decode().strip()
r.sendline(unquote(d).encode())

# Base64 to text
print(r.recvuntil(":").decode())
d = r.recvline().decode().strip()
r.sendline(b64decode(d))

# Text to Base64
print(r.recvuntil(":").decode())
d = r.recvline().decode().strip()
r.sendline(b64encode(d.encode()))

# ROT13 to Text
print(r.recvuntil(":").decode())
d = r.recvline().decode().strip()
e = ""
for i in d:
	if i in ascii_lowercase:
		e += ascii_lowercase[(ascii_lowercase.index(i) - 13) % len(ascii_lowercase)]
	else:
		e += i
print(d)
print(e)
r.sendline(e.encode())

# Text to ROT13
print(r.recvuntil(":").decode())
d = r.recvline().decode().strip()
e = ""
for i in d:
	if i in ascii_lowercase:
		e += ascii_lowercase[(ascii_lowercase.index(i) + 13) % len(ascii_lowercase)]
	else:
		e += i
print(d)
print(e)
r.sendline(e.encode())

# Binary to Base10
print(r.recvuntil(":").decode())
d = r.recvline().decode().strip()[2:]
r.sendline(str(int(d, 2)).encode())

# Decimal to Binary
print(r.recvuntil(":").decode())
d = r.recvline().decode().strip()
print(d)
print(bin(int(d)))
r.sendline(bin(int(d)).encode())

# End of Interactive Session
r.interactive()
