def main():
    infile = open('book of John text.txt', 'r')
    john = infile.read()

    words = john.split()

    word_index = {'Father':0, 'God':0, 'Christ':0, 'Spirit':0, 'spirit':0, 'life':0, 'man':0}

    for word in words:
        if word in word_index:
            word_index[word] += 1

    for word, count in word_index.items():
        print(f"{word}: {count}")

main()


