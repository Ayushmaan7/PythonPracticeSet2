def count_words(sentence):
    words = sentence.split()
    return len(words)

if __name__ == "__main__":
    input_sentence = input("Enter a sentence: ")
    word_count = count_words(input_sentence)
    print(f"Number of words in the sentence: {word_count}")
