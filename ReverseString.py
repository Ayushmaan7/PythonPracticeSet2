def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

if __name__ == "__main__":
    input_sentence = input("Enter a sentence: ")
    reversed_result = reverse_words(input_sentence)
    print(f"Reversed sentence: {reversed_result}")
