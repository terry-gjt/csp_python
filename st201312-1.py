# 出现次数最多的数
def st201312_1():
    n = int(input())
    s = input()
    nums = list(map(int,s.split(' ')))
    nums1 = list(set(nums))#去重复值
    nums1.sort()
    # print(nums1)
    nums2 = []
    i = 0
    l = len(nums1)
    # print(l)
    for x in nums1:#统计次数
        nums2.append(nums.count(x))
    # print(nums2)
    Max = max(nums2)
    count_Max = nums2.count(Max)
    if count_Max == 1:
        print(nums1[nums2.index(Max)])
    elif count_Max > 1:
        Min = nums1[nums2.index(Max)]
        j = 0;
        while j < l:
            if nums2[j] == Max and nums1[j] < Min:
                Min = nums1[j]
            j = j + 1
        print(Min)

if __name__ == '__main__':
    st201312_1()