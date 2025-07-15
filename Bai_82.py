# Bài 82: Tìm key có giá trị lớn nhất
def key_max_value(d):
    return max(d, key=d.get) if d else None

# Bài 83: Tìm key có giá trị lớn thứ nhì
def second_largest_key(d):
    if len(d) < 2:
        return None
    sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return sorted_items[1][0]

# Bài 84: Tìm path đến giá trị lớn nhất trong dict lồng nhau
def find_max_in_nested(d, current_path=""):
    if not isinstance(d, dict):
        return (d, current_path)
    max_val = float('-inf')
    max_path = ""
    for k, v in d.items():
        new_path = f"{current_path}.{k}" if current_path else k
        val, path = find_max_in_nested(v, new_path)
        if val > max_val:
            max_val = val
            max_path = path
    return (max_val, max_path)

# Bài 85: Gom nhóm key theo giá trị
def group_keys_by_value(d):
    result = {}
    for key, value in d.items():
        result.setdefault(value, []).append(key)
    return result

# Bài 86: Tìm key có tổng giá trị lớn nhất trong dict lồng nhau
def max_sum_key(d):
    def sum_values(v):
        if isinstance(v, dict):
            return sum(sum_values(x) for x in v.values())
        return v
    return max(d, key=lambda k: sum_values(d[k]))

# Bài 87: Tìm key có giá trị “dài nhất”
def longest_value_key(d):
    def get_length(v):
        if isinstance(v, (str, list, tuple, dict, set)):
            return len(v)
        return v
    return max(d, key=lambda k: get_length(d[k]))


# ======= TEST MẪU =======

if __name__ == "__main__":
    d1 = {'a': 5, 'b': 10, 'c': 7}
    print("Bài 82:", key_max_value(d1))  # b

    d2 = {'a': 30, 'b': 10, 'c': 20}
    print("Bài 83:", second_largest_key(d2))  # c

    nested = {'a': 10, 'b': {'x': 50, 'y': 20}, 'c': 30}
    print("Bài 84:", find_max_in_nested(nested))  # (50, 'b.x')

    d3 = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
    print("Bài 85:", group_keys_by_value(d3))  # {1: ['a', 'c'], 2: ['b', 'e'], 3: ['d']}

    d4 = {
        'A': {'x': 10, 'y': 20},
        'B': {'x': 5, 'y': {'z': 15, 'w': 25}},
        'C': 100
    }
    print("Bài 86:", max_sum_key(d4))  # C

    d5 = {
        'name': 'Alice',
        'scores': [95, 88, 92],
        'info': {'age': 30, 'job': 'engineer'},
        'id': 1001
    }
    print("Bài 87:", longest_value_key(d5))  # info
