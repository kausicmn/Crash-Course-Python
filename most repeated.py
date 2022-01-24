


sentence="This is a common interview question"
print(sentence[::-1])

# k=[x for x in sentence]
# max=0
# x=""
# for char in k:
#     if k.count(char)>max:
#         x=char
#         max=k.count(char)
# print(x,max)

dict={}
for char in sentence:
    if char in dict:
        dict[char]=dict[char]+1
    else:
        dict[char]=1
print(dict)
print(sorted(dict.items(),key=lambda z:z[1],reverse=True))