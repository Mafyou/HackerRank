def count_palindrome(sentence):
    answer = 0
    for index in range(len(sentence)):
        buffer = sentence[index]
        for next_letter in sentence[index:]:
            buffer += next_letter
            if buffer == buffer[::-1]:
                answer += 1
            else:
                break
    return answer

print(count_palindrome('aabcdeddffgf'))