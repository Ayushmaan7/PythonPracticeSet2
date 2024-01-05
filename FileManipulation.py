import string

def create_text_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"Text file '{file_path}' created successfully.")

    except IOError:
        print(f"Error creating the file: {file_path}")

def count_word_occurrences(file_path):
    word_count = {}

    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Remove punctuation and convert to lowercase
                line = line.translate(str.maketrans("", "", string.punctuation))
                words = line.lower().split()

                for word in words:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1

        # Display the word occurrences
        print("Word occurrences in the file:")
        for word, count in word_count.items():
            print(f"{word}: {count}")

    except FileNotFoundError:
        print(f"File not found: {file_path}")

if __name__ == "__main__":
    file_path = "sample_text_file.txt"
    file_content = "This is a sample text file. It contains some words for testing.\nFeel free to add more content."

    # Create the text file
    create_text_file(file_path, file_content)

    # Count word occurrences in the created file
    count_word_occurrences(file_path)
