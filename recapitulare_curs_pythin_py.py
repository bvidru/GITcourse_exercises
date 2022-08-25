def most_common():
    common_word = {}
    with open('task7.txt') as file:
        for line in file:
            words = line.strip().lower().split()
            for word in words:
                common_word[word] = common_word.get(word, 0) + 1
    return sorted(common_word.items(), key=lambda x: x[1], reverse=True)[:5]

if __name__ == "__main__":
    print(most_common())