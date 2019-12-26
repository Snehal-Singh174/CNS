text="snehal singh"
s1=""
d={'a':'g','b':'h','c':'i','d':'j','e':'k','f':'l','g':'m','h':'n','i':'o','j':'p','k':'q','l':'r','m':'s','n':'t','o':'u',
'p':'v','q':'w','r':'x','s':'y','t':'z','u':'a','v':'b','w':'c','x':'d','y':'e','z':'f'}
for i in text:
	if i==" ":
		s1+=" "
	elif i.isupper():
		f=i.lower()
		if f in d:
			c=d[f]
			k=c.upper()
			s1+=k

	else:
		if i in d:
			s1+=d[i]
d1={}
for i in text:
	if i==" ":
		continue
	else:
		c=text.count(i)
		d1[i]=c
		
d2={}
for i in s1:
	if i==" ":
		continue
	else:
		e=s1.count(i)
		d2[i]=e
print("Plain text: ",text)
print("Encrypted text: ",s1)
print("Plain text :")
for i in d1:
	print("The frequency of",i,"is",d1[i])
	
print("Encrypted text :")
for i in d2:
	print("The frequency of",i,"is",d2[i])

