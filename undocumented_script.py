def scale_numbers_by_parity(numbers):
    """Multiply even numbers by 2 and odd numbers by 3.
    
    Args:
        numbers (list): The numbers to process.
        
    Returns:
        list: The calculated numbers.
    """
    # Preserve the original rules so the results do not change.
    return [
        number * 2 if number % 2 == 0 else number * 3
        for number in numbers
    ]


def format_words_by_length(words):
    """Format words based on their length.
    
    Args:
        words (list): The words to process.
    
    Returns:
        str: The formatted words joined together.
    """
    # Join the words with spaces and remove extra spaces at the end.
    return " ".join([
        word.upper() if len(word) > 5 else word.lower()
        for word in words
    ]).strip()


def main():
    """Run the number and word processing functions."""
    numbers = [1, 2, 3, 4, 5, 6, 7]
    words = ["apple", "banana", "kiwi", "grapefruit", "cherry"]

    processed_numbers = scale_numbers_by_parity(numbers)
    processed_words = format_words_by_length(words)

    print("Processed Numbers:", processed_numbers)
    print("Processed Strings:", processed_words)


if __name__ == "__main__":
    main()
