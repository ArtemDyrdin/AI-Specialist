def find_anagrams(filename):
    words = dict()
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()
            words[word] = ''.join(sorted(word))
            

    all_groups = []
    k = 0
    while len(words) != k:
        current_sorted_word = ''
        for i in words.values():
            if i != None:
                current_sorted_word = i
                break
        current_group = []
        for key, value in words.items():
            if value == current_sorted_word:
                current_group.append(key)
                words[key] = None
                k += 1
        all_groups.append(current_group)

    return all_groups

def main():
    filename = 'words.txt'
    for group in find_anagrams(filename):
        print(group)

if __name__ == '__main__':
    main()