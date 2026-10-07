
def add_item(item, bucket=[]):
    bucket.append(item)
    return bucket

print(add_item(1))
# [1]
print(add_item(2))
# [1, 2]
print(add_item.__defaults__)
# whatever the above says...
# ([1, 2,], )

# 2/2 correct