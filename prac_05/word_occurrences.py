"""
CP1404/CP5632 Practical
Word Occurrences
Estimate: 20 minutes
Actual: 25 minutes
"""


def main():
    """Count occurrences of words in a string and display sorted results."""
    text = input("Text: ")
    words = text.split()
    word_to_count = {}
    for word in words:
        word_to_count[word] = word_to_count.get(word, 0) + 1

    max_length = max(len(word) for word in word_to_count)
    for word, count in sorted(word_to_count.items()):
        print(f"{word:{max_length}} : {count}")


main()
