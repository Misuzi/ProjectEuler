largest_prime = 0
primes = []
number = 600851475143

while number > 2:
    for i in range(2,int(number+1)):
        if number % i == 0:
            primes.append(i)
            number /= i
            break

primes.sort
largest_prime = primes[-1]
print(largest_prime)
