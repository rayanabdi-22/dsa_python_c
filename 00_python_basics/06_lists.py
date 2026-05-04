import random

lists = random.sample(range(10),5)
print(lists)
print(f"Start at index 2 {lists[2:]}")#start at index 2
print(f"Stop at index 3{lists[:3]}")#stop at index 3 