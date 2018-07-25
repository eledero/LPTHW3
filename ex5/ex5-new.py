name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

cms = height * 2.52
kgs = weight * 0.453592

print(f"Lets talk about {name}.")
print(f"He's {cms} inches tall.")
print(f"he's {kgs} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the cofee.")

# this line is tricky, try to get it exactly right
total = age + cms + kgs
print(f"If I add {age}, {cms}, and {kgs} I get {total}.")






