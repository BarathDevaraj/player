t=input()
print(''.join([ t[x:x+2][::-1] for x in range(0,len(t),2) ]))
