def count_palindrome(string):
    answer = 0
    i = 1
    while i <= len(string):
        for j in range(0, len(string) - i + 1):
            if string[j:j+i] == string[j:j+i][::-1]:
                answer += 1
        i += 1
    return answer

print(count_palindrome('aabcdeddffgf'))