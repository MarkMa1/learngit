# -* -  coding: utf-8  -* -
f=open('report.txt',encoding=' utf-8')
lines=f.readlines()
newline=[]
newtext=[]
for line in lines:
	sum=0
	newline=line.split()[:]
	for i in range(1,len(line.split())):
		sum+=int(line.split()[i])
	aver=round((sum)/(len(line.split())-1),1)
	newline.append(sum)
	newline.append(aver)
	newtext.append(newline)
# print(newtext)
newtext.sort(key=lambda x:x[-1],reverse=True)
# print(newtext)
for i in newtext:
	i.insert(0,newtext.index(i)+1)
# print (newtext)

total_av=[0 for s in range(1,12)]
for newline1 in newtext:
	for j in range(2,len(newline1)):
		total_av[j-2]+=int(newline1[j])
# print (total_av)
av_result=[round(i/len(newtext),2) for i in total_av]
av_result.insert(0,'平均')
av_result.insert(0,0)
# print (av_result)
newtext.insert(0,av_result)
# print (newtext)

for line in newtext:
	for i in range(2,len(line)-2):
		if int(line[i])<60:
			line[i]='不及格'
# print (newtext)
		
		
for line in newtext:
	print (line)
out=open('output.txt','w')
for line in newtext:
	out.writelines(str(line)+'\n')
out.close()



		
	