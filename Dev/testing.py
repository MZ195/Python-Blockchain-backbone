import collections
import operator

def characters_count(characters):
    print("Given string: {}".format(characters))
    print("Processing {} characters".format(len(characters)))
    
    partitioned_data = collections.defaultdict(list)

    for char in characters:
        partitioned_data[char].append(1)

    characters_count = []
    for char, occurances in partitioned_data.items():
        characters_count.append((char, sum(occurances)))

    characters_count.sort(key=operator.itemgetter(1))
    characters_count.reverse()

    for char, count in characters_count:
        print('%-*s: %2s' % (3, char, count))


if __name__ == "__main__":
    characters_count("hello")
    # longest word in english
    characters_count("pneumonoultramicroscopicsilicovolcanoconiosis")