def count_words(paragraph):
    words = paragraph.split()
    word_count = len(words)
    return word_count

paragraph = input("Enter a paragraph: ")
num_words = count_words(paragraph)
print(f"The paragraph  contains {num_words} words.")