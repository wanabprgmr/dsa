# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print("in rec", result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)


# import re

# txt = "The rain in Spain"
# x = re.search("^The", txt)

# print(x)

# import json

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# print(json.dumps(x, indent= 4,sort_keys=True))

import platform

print(platform.architecture)
print(platform.machine())
print(platform.node())
print(platform.platform())
print(platform.processor())
print(platform.python_build())
print(platform.python_compiler())
print(platform.python_version())
print(platform.release())
print(platform.system())
print(platform.uname())
print(platform.version())
print(platform.python_branch())
print(platform.python_implementation())
print(platform.python_revision())
