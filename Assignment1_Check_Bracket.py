#Python3
bracket=[]
inp_string=input()
flag=1
index=[]
for i in range(len(inp_string)):
	if(inp_string[i]=='(' or inp_string[i]=='[' or inp_string[i]=='{'):
		bracket.append(inp_string[i])
		index.append(i+1)
	elif(inp_string[i]==']' or inp_string[i]==')' or inp_string[i]=='}'):
		if(len(bracket)!=0):
			check=bracket.pop()
			index.pop()
			if((check=='(' and inp_string[i]==')')or(check=='[' and inp_string[i]==']')or(check=='{' and inp_string[i]=='}')):
				continue
			else:
				print(i+1)
				flag=0
				break
		else:
			print(i+1)
			flag=0
			break	
if(flag!=0 and len(bracket)!=0):
	print(index.pop())
	flag=0
if(flag==1):
	print("Success")

