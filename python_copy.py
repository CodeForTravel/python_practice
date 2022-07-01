## shallow copy
from copy import copy, deepcopy
list_a = [3,4,[9,4],5,6,2]
list_b = copy(list_a)
list_b[2].append(7)
list_a[2].append(8)
list_a.append(9)
list_b.append(10)
print(f"list_b: {list_b}")
print(f"list_a: {list_a}")
print("===================\n\n")

# deep copy
list_c = [2,4,6,[2,5],5,6]
list_d = deepcopy(list_c)
list_d[3].append(8)
list_c.append(9)
list_d.append(10)
print(f"list_d: {list_d}")
print(f"list_c: {list_c}")