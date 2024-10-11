#  BÀI 61 :Nhập vào một list số nguyên L, hãy sắp xếp list L theo thứ tự từ bé đến lớn
# Nhập vào list số nguyên
L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))

# Sắp xếp list theo thứ tự từ bé đến lớn
L.sort()

# In ra list đã được sắp xếp
print("List sau khi sắp xếp là:", L)