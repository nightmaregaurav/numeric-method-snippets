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
print("Computing n = pq")
print(f"n = {p} * {q}")
n = p*q
print(f"n = {n}")

print("Calculating Carmichael's totient of n as λ(n)")
print("Since n = pq, λ(n) = lcm(λ(p), λ(q))")
print("Again, since p and q are prime, λ(p) = φ(p) = p − 1")
print("Likewise, λ(q) = q − 1")
print("Hence λ(n) = lcm(p − 1, q − 1)")
print(f"Or λ({n}) = lcm({p} − 1, {q} − 1)")
λ_p = p - 1
λ_q = q - 1
λ_n = lcm(λ_p, λ_q)
print(f"Or λ({n}) = lcm({λ_p}, {λ_q})")
print(f"Or λ({n}) = {λ_n}")

while True:
	e = int(input('Choose e such that 1 < e < λ(n), e and λ(n) are co-prine: '))
	if not 1 < e < λ_n:
		print("1 < e < λ(n) did not satisfied, Try again...")
	elif gcd(e, λ_n) != 1:
		print(f"e and λ(n) have common divisor: {gcd(e, λ_n)}. Not a co-prime, Try again...")
	else:
		break

print("Determine d as the modular multiplicative inverse of e modulo λ(n)")
print("IE: (de + 1) mod λ(n) = 0")
d = 0
while true:
	d += 1
	x = (d * e) + 1 
	if x % λ_n == 0:
		break
print(f'd = {d}')
