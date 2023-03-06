oceans = ["Atlantic", "Pacific", "Indian", "Artic", "Southern"]


print(f"{sorted(oceans)}\n{len(oceans)}")

oceans.sort
print(oceans)

oceans.reverse()
print(oceans)

del oceans[4]
print(oceans)

print(oceans.pop())
print(oceans)

oceans.remove('Southern')
print(oceans)

oceans.append("Pacific")
print(oceans)

oceans.insert(3, "Atlantic")
print(oceans)