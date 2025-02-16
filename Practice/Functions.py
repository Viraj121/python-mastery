cities = ["delhi","gurgoan","noida"]
heroes = ["thor","captain america","shaktiman"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)

def print_list(list):
    for item in list:
        print(item,end=" ")

print_list(cities)