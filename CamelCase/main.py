def camelcase(s):
    answer = []
    isFirstWord = False
    for index in range(len(s)):
        isPassed = False
        if (ord(s[index]) > ord('A') and ord(s[index]) < ord('Z')) or not isFirstWord:
            isFirstWord = True
            for second_index in range(len(s)):
                if second_index > index and ord(s[second_index]) > ord('A') and ord(s[second_index]) < ord('Z'):
                    answer.append(s[index:second_index])
                    isPassed = True
                    break
            if not isPassed:
                answer.append(s[index:])
    return answer


print(camelcase('saveChangesInTheEditor'))