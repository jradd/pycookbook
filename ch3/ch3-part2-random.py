'3.x Picking Things at Random'

s = [1,2,3,4,5,6,7]
import random
# sample
a = random.sample(s,2)
print(a)
# shuffle

print(random.shuffle(s))
print(s)
# random.randint
# a <= N <= b.
print(random.randint(1,10))

# random.choice(seq)

print(random.choice(a))

# uniform
print(random.uniform(1,1000))
#Return a random floating point number N such that a <= N <= b


# other

# random.expovariate(lambd)

# random.gammavariate(alpha, beta)