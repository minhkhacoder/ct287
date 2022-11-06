import re

# f = open("B1.txt", "r")
# lines = f.readlines()
# BT1
# for i in lines:
#   x = re.findall("^[tc]", i)
#   if x:
#     r = re.findall("re", i)
#     if r: print(i)

# for email in lines:
  # x = re.findall(r"@([a-z]+\.[a-z]{2,3})", i)
  # y = re.findall(r"@([\w-]+\.+[\w-]{2,4})", i)
  # if x : print(x[0])
  # if y : print(y[0])
  # e = re.search(r"@([a-z]+\.[a-z]{2,3})", email)
  # print(e)
  # print(e)
  # if e:
    # print(email[e.end():])
    # x = re.search(r"\s$", email[:e.start()])
    # print(x)
    # if x is None:

f = open("B1.txt")
S = f.read().split("\n")
for e in S:
    rs = re.findall(r"\b\w+@\w+(?:\.\w+)+\b", e)
    if rs:
        for i in rs:
          print(re.search(r"(?<=@).+", i).group())

f.close()
