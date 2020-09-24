
import base64
from base64 import *
print("By Mostafa El-Guerdawi")
print("")
txt = input("enter txt to hash: )
print("")
way = str(input("1===> b64encode\n2===> b32encode\n3===> b16encode\n4===> b85encode\na5===> 85encode")
hash1 = base64.b64encode(txt.encode("ascii"))
hash2 = base64.b32encode(txt.encode("ascii"))
hash3 = base64.b16encode(txt.encode("ascii"))
hash4 = base64.b85encode(txt.encode("ascii"))
hash5 = base64.a85encode(txt.encode("ascii"))
if way == "1" :
         print("")
         print("your hash is: ") ,hash1)
elif way == "2" :
         print("your hash is: ") ,hash2)
elif way == "3" :
         print("your hash is: ") ,hash3)
elif way == "4" :
         print("your hash is: ") ,hash4)
elif way == "5" :
         print("your hash is: ") ,hash5)
else :
         print("Error...")
         
        
