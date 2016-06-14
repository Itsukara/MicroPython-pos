import uos

# uos commands in linux style
def cd(p):
  uos.chdir(p)

def pwd():
  return uos.getcwd()

def ls(*d):
  ns = uos.listdir(*d)
  ns.sort()
  for n in ns:
    st = uos.stat(n)
    size = st[6]
    print("{:6d} {}".format(size, n))

def mkdir(p):
  uos.mkdir(p)

def rm(p):
  uos.remove(p)

def rmdir(p):
  uos.remove(p)

def mv(op, np):
  uos.rename(op, np)

def sync():
  uos.sync()

# linux like commands
def cat(n):
  with open(n, "r") as f:
    print(f.read())

def join(n1, n2, n3):
  with open(n1, "r") as f1:
    s = f1.read()
  with open(n2, "r") as f2:
    s += f2.read()
  with open(n3, "w") as f3:
    f3.write(s)

def nl(n):
  with open(n, "r") as f:
    s = f.read()
  s = s.split("\n")
  ln = 0
  for l in s:
    ln += 1
    print("{:3d}: {}".format(ln, l))

def cp(n1, n2):
  with open(n1, "r") as f1:
    s = f1.read()
  with open(n2, "w") as f2:
    f2.write(s)

def write(s, n):
  with open(n, "w") as f:
    f.write(s)

def read(n):
  with open(n, "r") as f:
    return f.read()

def fgrep(s):
  ns = uos.listdir()
  for n in ns:
    with open(n, "r") as f:
      r = f.read()
    ls = r.split("\n")
    ln = 0
    for l in ls:
      ln += 1
      if s in l:
        print("{}:{:3d}: {}".format(n, ln, l))
 
def getlines():
  s = ""
  while True:
    l = input()
    if l == '"""' or l == "'''":
      return s
    else:
      s += l + "\n"

        