# Challenge 2 URL - http://www.pythonchallenge.com/pc/def/map.html

# Challenge is 
#   the picture on the webpage show
#   K -> M
#   O -> Q
#   E -> G
#   It is a crypto key, We need to decipher the test given below to find out the solution

cipher = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# Solution:
import string

alphabets = list(string.ascii_lowercase)

#creating a dictionary will the cipher key for all the alphabets like a -> c, b -> d
keys_dict = { x : alphabets[(i + 2) % 26] for i,x in  enumerate(alphabets) }

decipher = list()
for c in cipher:
    if c in alphabets:
        decipher.append(keys_dict[c])
    else:
        decipher.append(c)

print("".join(decipher))


# decipher string will be
# i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.


# solution 2 : using string.maketrans()

intab = "abcdefghilmnopqrstuvwxyz"
outtab = "cdefghilmnopqrstuvwxyzab"
transtab = string.maketrans(intab, outtab)

print cipher.translate(transtab)

# solution 2 also give the same answer. as said we need to apply our change to the URL which is map.html

url = "map"

print url.translate(transtab)

# the answer is ocr. hence the answer URL will be http://www.pythonchallenge.com/pc/def/ocr.html