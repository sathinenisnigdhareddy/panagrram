#panagram program

capital=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
small=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
str=input("enter a string")
list1=list(str)

flag='found'
for i in range(0,26):
    if( capital[i]  not in list1 and small[i] not in list1):
        flag='not found'
        break
if(flag=='not found'):
    print('string is not a panagram')
else:
    print('string is a panagram')

        
        
