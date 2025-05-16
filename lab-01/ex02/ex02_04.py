j=[]
# Duyệt qua tất cả các số trong đoạn từ 2000 đến 3200, kiểm tra điều kiện
for i in range(2000, 3201):

    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))

# In ra kết quả, cách nhau bằng dấu phẩy
print(','.join(j))
