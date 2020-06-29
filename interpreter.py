O="«»><+-,.[]()      ≥≤"; Oi=O.index; lpp=lambda l:"".join(map(str, l))
def mpp(m,p=0): return ("(..., "*((li:=max(0,p-7))>0) + "["*(li==0) +
 str(m[li:(ri:=p+8)])[1:-1] + "]"*(ri>=len(m)) + ", ...)"*(ri<len(m)))

def I(l,i,p=0,m=[0],o="",r=0,de=0,_=None):
 _W,_LO=_
 while l:
  if de>r: print(f"{r}: m[{p}]={m[p]} @ {mpp(m,p)}; inp='{lpp(i)}'\n{lpp(l)}")or input()
  n,*l=l; n=Oi(n)
  if n in[0,1]: p=n*(len(m)-1)
  elif n in[2,3,18,19]:
   f=True
   while (n in[2,3]or m[p]) and f: p+=1-[2,18,0,0,3,19].index(n)//2; m=[0]*(p<0)+m+[0]*(p==len(m)); p=max(0,p); f=n>15
  elif n in[4,5]: m[p]+=1-[4,0,5].index(n); m[p]=_W(m[p])
  elif 6==n: c,*i=i or "\u0000"; m[p]=_W(ord(c))
  elif 7==n: o=_LO(chr(m[p]),o)
  elif n in[8,10]:
   d=2*(n==10); f=True; t=1
   g=[t:=t+(Oi(k)==8+d)-(Oi(k)==9+d)for k in l].index(0)
   while m[p] and f:i,p,m,o=I(l[:g+1],i,p,m,o,r+1,de,_); f=n==8
   l=l[g:]
 return i,p,m,o

def E(c,de=0,env=None):
 env=env or{}; G=env.get; _w=G("W",256); _lo=G("LO",False)
 _W=lambda v: (_w and v%_w) or v; _LO=lambda c,o: (_lo and print(c,end=""))or o+c; _=[_W,_LO]
 l=[O[16*(len(l)>1 and l[-1]==l[-2])+len([*filter(bool,l.split(" "))])]for l in c.split("\n")]
 i,p,m,o=I(l,input(" inp >> ")if "," in l else"",r=0,de=de,_=_); (_lo and print()); return i,p,m,o
