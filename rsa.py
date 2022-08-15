def isprime(a):
	if a <= 3:
		return n > 1
	if not a % 2 or not a % 3:
		return False
	
	i = 5
	stop = int(a ** 0.5)
	while i <= stop:
		if not a % i or not a % (i + 2):
			return False
		i += 6
	return True

def gcd(a,b):
	while a != b:
		if a>b:
			a -= b
		else:
			b -= a
	return a

def lcm(a,b):
	if a == b == 0:
		return 0
	a,b = min(a,b), max(a,b)
	return abs(a) * (abs(b) / gcd(a,b))	


flag = True
while flag:
	p = int(input('P: '))
	if not isprime(p):
		print("P is not prime, Try again...")
	else:
		flag = False
flag = True
while flag:
	q = int(input('Q: '))
	if not isprime(q):
		print("Q is not prime, Try again...")
	elif q == p:
		print("Q & P cannot be same, Try again...")
	else:
		flag = False

n = p*q
pi = (p-1)*(q-1)

print(f'n = {n}')
print(f'pi(n) = {pi}')

while True:
	e = int(input('e: '))
	if e <= 1 or e >= pi:
		print("1<e<pi(n) did not satisfied, Try again...")
	elif gcd(e, q) != 1:
		print(f"e and pi(n) have common divisor: {gcd(e, q)}. Not a co-prime, Try again...")
	else:
		break

for i in range(1,10): 
	x = 1 + i*pi 
	if x % e == 0: 
		d = int(x/e) 
		break

print(f'd = {d}')
