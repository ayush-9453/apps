#dictionaries are the ordered pair of data items.
#They store multiple data ina single variable. 
dic ={
   78:"Human", 
   77:"being"
 }
print(dic.keys())

for key in dic.keys():
    print(f"The value corresponding to the key {key} is {dic[key]}")

ep ={12:  24 , 13:69 ,14:69 ,15:79}
ep2 ={20:50 ,21:46  }
ep.update(ep2)
print(ep)