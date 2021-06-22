''' This code helps you to get idea about how the savings of 1 year get growing till 20 years after inevsting
you can see increament of particular year sequentialy
'''
p=271200
r=12
y=19
for i in range(1,20):
	p=p+(p*r/100)
	print(i,"=>{:.2f}".format(float(p)))