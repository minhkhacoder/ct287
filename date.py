import re

f = open("test3.csv", "r")
lines = f.readlines()

for date in lines:
  d = re.search(r"\s", date)
  s = date[:d.start()]
  e = date[d.end():]
  # print(date[:d.start()])
  x = re.search(r"\.", s)
  y = re.search(r"\.", e)
  if x is None:
    noPoint = re.sub(r"(\d{1,2})(\d{1,2})(\d{4})", "\\2/\\1/\\3", s)
    print(noPoint, end=" ")
  else:
    point = re.sub(r"(\d{1,2}).(\d{1,2}).(\d{4})", "\\2/\\1/\\3", s)
    print(point, end=" ")

  if y is None:
    noPoint = re.sub(r"(\d{1,2})(\d{1,2})(\d{4})", "\\2/\\1/\\3", e)
    print(noPoint)
  else:
    point = re.sub(r"(\d{1,2}).(\d{1,2}).(\d{4})", "\\2/\\1/\\3", e)
    print(point)