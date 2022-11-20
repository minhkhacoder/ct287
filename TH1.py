
# BT1
# filename = input()

# list = []
# for f in filename:
#   if f not in list:
#     list.append(f)
# list.sort()
# for i in list:
#   print(i + ": " + str(filename.count(i)))

# =============================

st = input()
length = len(st)
mid = st[3:length-3]

if st[:3] == "ATG" and length >= 9 and len(mid) % 3 == 0:
  if st[length-3:] == "TAA" or st[length-3:] == "TAG" or st[length-3:] == "TGA":
    index = 0
    flag = 1
    for i in range(int(len(mid) / 3)):
      if mid[index] == mid[index+1] and mid[index] == mid[index+2]:
        flag = 0
        break
      else:
        index += 3
        if index > len(mid) - 3: break

    if flag == 1:
      print("YES")
    else: print("NO")
else: 
  print("NO")