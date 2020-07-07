import sys; O="«»><+-,.[]()      ≥≤±∓;:"; Oi=O.index
lpp=lambda l:"".join(map(str, l)); ext=lambda m,p:([0]*(p<0)+m+[0]*(p==len(m)),max(0,p))
def mpp(m,p=0): return ("(..., "*((li:=max(0,p-7))>0) + "["*(li==0) +
 str(m[li:(ri:=p+8)])[1:-1] + "]"*(ri>=len(m)) + ", ...)"*(ri<len(m)))

def I(l,i=None,p=0,m=None,o="",r=0,de=0,_=None):
 _W,_I,_O=_; m=m or [0]
 while l:
  if de>r: print(f"{r}: m[{p}]={m[p]} @ {mpp(m,p)}; inp='{lpp(i)}'; out='{lpp(o)}'\n{lpp(l)}"); input()
  n,*l=l; n=Oi(n); f=True
  if n in[0,1]: p=n*(len(m)-1)
  elif n in[2,3,18,19]:
   while (n in[2,3]or m[p]) and f: p+=1-[2,18,0,0,3,19].index(n)//2; m,p=ext(m,p); f=n>15
  elif n in[4,5]: m[p]+=1-[4,0,5].index(n); m[p]=_W(m[p])
  elif n in[6,22]:
   while f or(m[p]and n>6): f or (p:=p+1); m,p=ext(m,p); m[p]=_W(_I()); f=False
  elif n in[7,23]:
   while (f and n==7)or(m[p]and n>7): o+=_O(m[p]); n==7 or(p:=p+1); m,p=ext(m,p); f=False
  elif n in[8,10]:
   d=2*(n==10); t=1
   g=[t:=t+(Oi(k)==8+d)-(Oi(k)==9+d)for k in l].index(0)
   while m[p] and f:i,p,m,o=I(l[:g+1],i,p,m,o,r+1,de,_); f=n==8
   l=l[g:]
  elif n in[20,21]: m[p]=sorted([0,m[p]+1-[20,0,21].index(n)]+[_W(-1)]*(_W(-1)!=-1))[1]
 return p,m,o

def E(c,de=0,env=None):
 env=env or{}; G=env.get; _w=G("W",256); _nio=G("NIO",False)
 _W=lambda v:int((_w and v%_w) or (not _w and v)); _O=lambda c:1+sys.stdout.write(o:=(f"{c}\n"if _nio else chr(c)))and o
 _I=(lambda:(r:=sys.stdin.readline())and int(r)or 0)if _nio else(lambda:(r:=sys.stdin.read(1))and ord(r)or 0)
 _=[_W,_I,_O]
 l=[O[16*(len(l)>1 and l[-1]==l[-2])+len([*filter(bool,l.split(" "))])]for l in c.split("\n")]
 return I(l,r=0,de=de,_=_)
