def I(l,i,p=0,m=[0]):
 while l:
  n,*l=l
  if n in[0,1]: p=n*(len(m)-1)
  elif n in[2,3]: p+=1-[2,0,3].index(n); m=[0]*(p<0)+m+[0]*(p==len(m)); p=max(0,p)
  elif n in[4,5]: m[p]+=1-[4,0,5].index(n); m[p]%=256
  elif 6==n: c,*i=i or "\u0000"; m[p]=ord(c)
  elif 7==n: print(chr(m[p]), end="")
  elif n in[8,10]:
   d=2*(n==10); f=True
   g=(t:=1)and[t:=t+(k==8+d)-(k==9+d)for k in l].index(0)
   while m[p] and f:i,p,m=I(l[:g],i,p,m); f=n==8
   l=l[g:]
 return i,p,m

def E(c): I(l:=[len([*filter(bool,l.split(" "))])for l in c.split("\n")],input(" inp >> ")if 6 in l else""); print()
