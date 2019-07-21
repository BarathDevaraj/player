def reverse(wd):
	rev=0
	while wd>0:
		rev=rev*10+(wd%10)
		wd//=10
	return rev
wd=int(input())
print (reverse(wd))
