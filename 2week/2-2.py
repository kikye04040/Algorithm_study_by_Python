def length_of_longest_substring(s):
    char_map = {}
    start = maxLength = 0

    for i, char in enumerate(s):
        if char in char_map and start <= char_map[char]:
            start = char_map[char] + 1
        else:
            maxLength = max(maxLength, i - start + 1)

        char_map[char] = i

    return maxLength

print(length_of_longest_substring("abcabcbb"))
print(length_of_longest_substring("bbbbb"))
