

def safe_convert_int(value, default=0):
    try:
        return int(value)
    except (ValueError,TypeError):
        try:
            return float(value)
        except (TypeError,ValueError):
            return default
        

value = "Hello Python Learners!"

r = safe_convert_int(value)
print(r) #0

value = "097986"

r = safe_convert_int(value)
print(r) # 97986

value = "23123.5454"

r = safe_convert_int(value)
print(r)

value = None # What is the type here? no value and not type

r = safe_convert_int(value)
print(r)



def safe_convert_int_or_throw(value):
    try:
        return int(value)
    except (ValueError,TypeError):
        try:
            return float(value)
        except (TypeError,ValueError):
            raise
        
value = "Hello Python Learners!"

try:
    r = safe_convert_int_or_throw(value)
    print(r)
except Exception as e:
    print("Some error-->",e.args[0])

value = "123"
r = safe_convert_int_or_throw(value)
print(r)