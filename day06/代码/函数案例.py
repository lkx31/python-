"""
需求: 奇偶求和.
    编写一个程序，求出一个列表中偶数和奇数的和。

    定义函数calculate_sum()，参数为一个数字列表numbers_list, 分别求出偶数和奇数的和。
    最后，返回一个列表(元组)，第一个元素为偶数的和，第二个元素为奇数的和。
"""
def calculatate_sum(numebers_list):
    oushuhe = []
    jishuhe = []
    for i in numebers_list:
        if i % 2 == 0:
            oushuhe.append(i)
        else:
            jishuhe.append(i)
    return oushuhe,jishuhe
oushu,jishu=calculatate_sum([1,2,3,4,5,6])
print(oushu,jishu)