def isprime(a):
	if a <= 3:
		return a > 1
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

λ_p = p - 1
λ_q = q - 1
λ_n = lcm(λ_p, λ_q)

pi = (p-1)*(q-1)

while True:
	e = int(input('e: '))
	if not 1 < e < λ_n:
		print("1 < e < λ(n) did not satisfied, Try again...")
	elif gcd(e, λ_n) != 1:
		print(f"e and λ(n) have common divisor: {gcd(e, λ_n)}. Not a co-prime, Try again...")
	else:
		break

d = 0
while true:
	d += 1
	x = (d * e) + 1 
	if x % λ_n == 0:
		break

print(f'p = {p}')
print(f'q = {q}')
print(f'n = {n}')
print(f'λ(n) = {λ_n}')
print(f'e = {e}')
print(f'd = {d}')
