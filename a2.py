def reverse(wd):
	fact=1
	while wd>0:
		fact*=wd
		wd-=1
	return fact
wd=int(input())
print (reverse(wd))
