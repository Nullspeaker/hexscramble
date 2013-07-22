_BANNED=["$","&","+",",","/",":",";","=","?","@","."]
def toHex(a): return "".join("%"+hex(ord(i))[2:] if not (i in _BANNED) else i for i in list(a))
while True:
  INPUT=input().replace("http://","")
  print( ("http://"+"".join([toHex(j) for j in INPUT])) )
