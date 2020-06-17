O="«»><+-,.[]()"; Oi=O.index; lpp=lambda l:"".join(map(str, l))
def mpp(m,p=0): return ("(..., "*((li:=max(0,p-7))>0) + "["*(li==0) +
 str(m[li:(ri:=p+8)])[1:-1] + "]"*(ri>=len(m)) + ", ...)"*(ri<len(m)))

def I(l,i,p=0,m=[0],o="",r=0,de=0):
 while l:
  if de>1: print(f"{r}: m[{p}]={m[p]} @ {mpp(m,p)}; inp='{lpp(i)}'\n{lpp(l)}")or(de<3 or input())
  n,*l=l; n=Oi(n)
  if n in[0,1]: p=n*(len(m)-1)
  elif n in[2,3]: p+=1-[2,0,3].index(n); m=[0]*(p<0)+m+[0]*(p==len(m)); p=max(0,p)
  elif n in[4,5]: m[p]+=1-[4,0,5].index(n); m[p]%=256
  elif 6==n: c,*i=i or "\u0000"; m[p]=ord(c)
  elif 7==n: o+=chr(m[p])
  elif n in[8,10]:
   d=2*(n==10); f=True
   g=(t:=1)and[t:=t+(Oi(k)==8+d)-(Oi(k)==9+d)for k in l].index(0)
   while m[p] and f:i,p,m,o=I(l[:g+1],i,p,m,o,r+1,de); f=n==8
   l=l[g:]
 return i,p,m,o

def E(c,de=0):
 l=[O[len([*filter(bool,l.split(" "))])]for l in c.split("\n")]
 i,p,m,o=I(l,input(" inp >> ")if "," in l else"",r=0,de=de); return i,p,m,o
