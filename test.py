from morse_code import encode, decode
assert encode("SOS") == "... --- ..."
assert decode("... --- ...") == "SOS"
assert encode("HELLO") == ".... . .-.. .-.. ---"
assert decode(encode("TEST 123")) == "TEST 123"
assert encode("A") == ".-"
print("morse_code tests passed")
