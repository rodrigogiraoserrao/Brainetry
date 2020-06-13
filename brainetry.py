def I(l,i,p=0,m=[0]):
 while l:
  n,*l=l
  if n in[0,1]: p=n*(len(m)-1)
  elif n in[2,3]: p+=1-[2,0,3].index(n); m=[0]*(p<0)+m+[0]*(p==len(m)); p=max(0,p)
  elif n in[4,5]: m[p]+=1-[4,0,5].index(n); m[p]%=256
  elif 6==n: c,*i=i or "\u0000"; m[p]=ord(c)
  elif 7==n: print(chr(m[p]), end="")
  elif 8==n:
   g=(t:=1)and[t:=t+(k==8)-(k==9)for k in l].index(0)
   while m[p]:i,p,m=I(l[:g],i,p,m)
   l=l[g:]
 return i,p,m
def E(c): I([len([*filter(bool,l.split(" "))])for l in c.split("\n")],input(" inp >> ")); print()
