def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)

    # Создаем матрицу размером (m+1)x(n+1) для хранения длин подстрок
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    max_length = 0
    end_index = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i

    longest_substring = str1[end_index - max_length: end_index]
    return longest_substring

str1 = "Hello, World!"
str2 = "Welcome to the World!"
longest_substring = longest_common_substring(str1, str2)
print("Наибольшая общая подстрока:", longest_substring)
