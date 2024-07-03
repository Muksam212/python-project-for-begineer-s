words= '''
It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, 
sometimes by accident, sometimes on purpose (injected humour and the like).

'''

word_split = words.split()
word_freq = [word_split.count(w) for w in word_split]

print("String\n {} \n".format(words))
print("List\n {} \n".format(str((word_split))))
print("Frequency\n {}\n".format(str(word_freq)))
print("Pairs\n {} \n".format(dict(zip(word_split, word_freq))))