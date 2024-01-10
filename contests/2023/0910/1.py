def find_all_matches(arr1, arr2):
    if not arr1:
        return [[]]  # 返回一个空匹配
    if not arr2:
        return []

    first_item = arr1[0]
    rest_of_arr1 = arr1[1:]
    all_matches = []

    for item in arr2:
        matches_with_item = find_all_matches(rest_of_arr1, arr2)
        for match in matches_with_item:
            all_matches.append([[first_item, item]] + match)

    return all_matches

# 示例输入
array1 = [1, 2]
array2 = [3, 4]

# 调用函数找到所有匹配
all_matches = find_all_matches(array1, array2)

# 打印所有匹配
print(all_matches)