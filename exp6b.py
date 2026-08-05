def is_palindrome(text):
    queue = Queue()
    cleaned = ""

    # Remove special characters and convert to lowercase
    for ch in text:
        if ch.isalnum():
            cleaned += ch.lower()

    # Insert characters into the queue
    for ch in cleaned:
        queue.put(ch)

    # Compare queue elements with reversed string
    for ch in reversed(cleaned):
        if queue.get() != ch:
            return False

    return True

# Main Program
text = input("Enter a string: ")

if is_palindrome(text):
    print("The given string is a Palindrome.")
else:
    print("The given string is Not a Palindrome.")
