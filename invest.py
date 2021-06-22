import os
import time
os.system('cls')
print("-"*100)
print("\t\t\t\t\t█══welcome══█")
print("-"*100)

sal= float(input("Enter the Salary: "))*12
dsal=sal
exp= float(input("Enter the Expenses: "))*12
dexp=exp
rs= int(input("Enter Rate at which Salary increase per year: "))
rexp= int(input("Enter Rate at which Expenses increase per year: "))

rinv= int(input("Enter Rate of Investment: "))
tsav=0

os.system('cls')
print("Let's see the difference when you save the Savings & when you invest the Savings:")
time.sleep(4)

print("\n=> Without Investment Amount:")
print("-"*100)
print("\t Year\t\t\t Income\t\t\t Expenses\t\t Savings")
print("-"*100)
for i in range(1,21):
	if i==1:
		saving= dsal-dexp
		tsav+=saving
		print("\t {}\t\t\t {:.2f}\t\t {:.2f}\t\t {:.2f}".format(i,dsal,dexp,saving))
	else:
		dsal=dsal+(dsal*rs/100)
		dexp=dexp+(dexp*rexp/100)
		saving= dsal-dexp
		tsav+=saving
		print("\t {}\t\t\t {:.2f}\t\t {:.2f}\t\t {:.2f}".format(i,dsal,dexp,saving))
print("-"*100)
print("Total Savings: {:.2f}".format(tsav))
print("-"*100)

time.sleep(2)

print("\n=> With Investment Amount:")
print("-"*120)
print("\t Year\t\t\t Income\t\t\t Expenses\t\t Savings\t\t Invested @ {}".format(rinv))
print("-"*120)
tinv=0
inv=0
yr=19
for i in range(1,21):
	if i==1:
		saving= sal-exp
		inv=saving
		for j in range(1,yr+1):
			inv=inv+(inv*rinv/100)
		tinv+=inv
		yr-=1
		print("\t {}\t\t\t {:.2f}\t\t {:.2f}\t\t {:.2f}\t\t {:.2f}".format(i,sal,exp,saving,inv))
	else:
		sal=sal+(sal*rs/100)
		exp=exp+(exp*rexp/100)
		saving= sal-exp
		inv=saving
		for j in range(1,yr+1):
			inv=inv+(inv*rinv/100)
		tinv+=inv
		yr-=1
		print("\t {}\t\t\t {:.2f}\t\t {:.2f}\t\t {:.2f}\t\t {:.2f}".format(i,sal,exp,saving,inv))
print("-"*120)
print("Total Amount: {:.2f}".format(tinv))
print("-"*120)
time.sleep(2)
x=tinv/tsav
print("""
With the decision to invest the savings, your balance has increased significantly. 
The balance has grown to Rs.{:.2f} from Rs.{:.2f} 
This is {:.2f}x times the regular saving amount.""".format(tinv,tsav,x))
