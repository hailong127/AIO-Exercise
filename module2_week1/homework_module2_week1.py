# Câu 1: A
# tạo mảng một chiều từ 0 đến 9
import pandas as pd
import matplotlib.image as mpimg
import numpy as np
arr = np.arange(0, 10, 1)

# Câu 2: D
# tạo một mảng boolean 3x3 với tất cả giá trị là True
arr = np.ones((3, 3)) > 0

arr = np.ones((3, 3), dtype=bool)

arr = np.full((3, 3), fill_value=True, dtype=bool)

# Câu 3: A
arr = np.arange(0, 10)
print(arr[arr % 2 == 1])

# Câu 4: B
arr = np.arange(0, 10)
arr[arr % 2 == 1] = -1
print(arr)

# Câu 5: B
arr = np.arange(10)
arr_2d = arr.reshape(2, -1)
print(arr_2d)

# Câu 6: A
arr1 = np.arange(10).reshape(2, -1)
arr2 = np.repeat(1, 10).reshape(2, -1)
c = np.concatenate([arr1, arr2], axis=0)
print("Result: \n", c)

# Câu 7: C
arr1 = np.arange(10).reshape(2, -1)
arr2 = np.repeat(1, 10).reshape(2, -1)
c = np.concatenate([arr1, arr2], axis=1)
print("C = ", c)

# Câu 8: A
arr = np.array([1, 2, 3])
print(np.repeat(arr, 3))
print(np.tile(arr, 3))

# Câu 9: C
a = np.array([2, 6, 1, 9, 10, 3, 27])
index = np.nonzero((a >= 5) & (a <= 10))
print("result", a[index])

# Câu 10: D


def maxx(x, y):
    if x >= y:
        return x
    else:
        return y


a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
pair_max = np.vectorize(maxx, otypes=[float])
print(pair_max(a, b))

# Câu 11: A
a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
print("Result", np.where(a < b, b, a))

# Câu 12: A
# Download image


def rgb_to_gray_lightness(rgb):
    # Get the maximum and minimum values among the RGB channels
    max_val = np.max(rgb, axis=2)
    min_val = np.min(rgb, axis=2)
    # Compute the Lightness grayscale value
    gray = (max_val + min_val) / 2
    return gray


gray_img_01 = rgb_to_gray_lightness(img)
gray_img_01[0, 0]

# Câu 13: A

# Download the image

# Read the image
img = mpimg.imread('/content/dog.jpeg')

# Convert the image to grayscale using the Average method


def rgb_to_gray_average(rgb):
    # Compute the average of the RGB channels
    gray = np.mean(rgb, axis=2)
    return gray


gray_img_02 = rgb_to_gray_average(img)

# Display the value of the first pixel
print(gray_img_02[0, 0])

# Câu 14: C

# Download the image


# Read the image
img = mpimg.imread('/content/dog.jpeg')

# Convert the image to grayscale using the Luminosity method


def rgb_to_gray_luminosity(rgb):
    # Compute the Luminosity grayscale value
    gray = 0.21 * rgb[:, :, 0] + 0.72 * rgb[:, :, 1] + 0.07 * rgb[:, :, 2]
    return gray


gray_img_03 = rgb_to_gray_luminosity(img)

# Display the value of the first pixel
print(gray_img_03[0, 0])

# Câu 15: C
# Download data


df = pd.read_csv('/content/advertising.csv')
data = df.to_numpy()

# Lấy giá trị lớn nhất trong cột 'Sales'
max_value = df['Sales'].max()

# Lấy chỉ mục của giá trị lớn nhất
max_index = df['Sales'].idxmax()

print(f"Giá trị lớn nhất trong cột 'Sales': {max_value}")
print(f"Chỉ mục tương ứng của giá trị lớn nhất: {max_index}")

# Câu 16: B
# giá trị trung bình của cột TV
mean_tv = df['TV'].mean()

print(f"Giá trị trung bình của cột 'TV': {mean_tv}")

# Câu 17: A
# số lượng bản ghi có giá trị tại cột Sales lớn hơn hoặc bằng 20
count_sales_ge_20 = (df['Sales'] >= 20).sum()

print(
    f"Số lượng bản ghi có giá trị tại cột 'Sales' lớn hơn hoặc bằng 20: {count_sales_ge_20}")

# Câu 18: B
# Lọc các bản ghi có giá trị tại cột 'Sales' lớn hơn hoặc bằng 15
filtered_df = df[df['Sales'] >= 15]

# Tính giá trị trung bình của cột 'Radio' trong các bản ghi đã lọc
mean_radio = filtered_df['Radio'].mean()

print(
    f"Giá trị trung bình của cột 'Radio' với điều kiện cột 'Sales' >= 15: {mean_radio}")

# Câu 19: C
# Tính giá trị trung bình của cột 'Newspaper'
mean_newspaper = df['Newspaper'].mean()

# Tính tổng các giá trị của cột 'Newspaper' lớn hơn giá trị trung bình
total_newspaper_above_mean = df[df['Newspaper']
                                > mean_newspaper]['Newspaper'].sum()

print("Giá trị trung bình của cột Newspaper", mean_newspaper)
print(
    f"Tổng các giá trị của cột 'Newspaper' lớn hơn giá trị trung bình: {total_newspaper_above_mean}")

# Câu 20: C
# giá trị trung bình của cột Sales
mean_sales = df['Sales'].mean()

print(f"Giá trị trung bình của cột 'Sales': {mean_sales}")

# Câu 21: C
