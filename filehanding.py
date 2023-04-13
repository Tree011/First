# we can read , write and append files in pythin using this i/o.
# f= ' yoooo this shit is cool'
# with open('avi.txt','w') as g:
#     g.write(f)

with open('avi2.txt','r') as g:
    s= g.read()
    print(s)
j= '  append this shit'
with open('avi.txt','a') as h:
    h.write(j)


#so basically use r,w,a differently.


with open('avi3.txt','w+') as r:
    r.write('hiiiiiiii to you babes')
    r.seek(0)#move the file pointer to start as after writing the pointer moves and cant read so if you have to make different i/o blocks or jjust add in one using seek.
    print(r.read())