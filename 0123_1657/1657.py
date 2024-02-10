def closeStrings(word1, word2):
    if set(word1) != set(word2):
        return False

    word1_count = [0] * 26
    word2_count = [0] * 26

    for c in word1:
        word1_count[ord(c) - ord("a")] += 1
    for c in word2:
        word2_count[ord(c) - ord("a")] += 1

    word1_count.sort()
    word2_count.sort()

    return word1_count == word2_count
