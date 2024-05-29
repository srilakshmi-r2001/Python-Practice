str='RVCE MCA DEPARTMENT'
#i
n=int(input("Enter the first number of charcaters you wish to remove:"))
print(str[n+1: ])
#iii
substr='RVCE'
l=len(str)
le=l-1
mid=int(l/2)
fml=str[0]+str[mid]+str[le]
print(fml)
#iv
apstr=str[ :mid]+substr+str[mid: ]
print(apstr)