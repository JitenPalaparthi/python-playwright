
pincodes = {
    "560086":"Bangalore-1",
    "560096":"Bangalore-2",
    "560034":"Bangalore-3",
    "695401":"Trivandrum-1",
    "522001":"Guntur-1"
}

for k,v in pincodes.items():
    print("Key:",k,"Value:",v)

print(len(pincodes))

print(pincodes["560086"])

pincodes["560086"]="Bengaluru-1"
print(pincodes["560086"])

print(pincodes.get("5600861")) # get is no value it returns None

try:
    print(pincodes["5600861"]) # is no value it throws KeyError
except KeyError:
    print("no key found")





