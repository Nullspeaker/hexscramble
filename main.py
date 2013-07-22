def toHex(a): return "".join("%"+hex(ord(i))[2:] for i in list(a))
while True:
  INPUT_=input().replace("http://","").split("/")
  print( ("http://"+"/".join([toHex(j) for j in INPUT])).replace("%2e",".") )
