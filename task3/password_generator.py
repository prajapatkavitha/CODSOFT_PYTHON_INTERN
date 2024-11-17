import string
import random
def generate_password(length, complexity):
    """  Generates a random password based on the specified length and complexity.
    Parameters:
    length (int): The desired length of the password.
    complexity (str): The desired complexity of the password, can be 'low', 'medium', or 'high'.
    Returns:
    str: The generated password.
    """
    characters = ""
    if complexity == "low":
        characters = string.ascii_lowercase
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Invalid complexity level. Please choose 'low', 'medium', or 'high'."
    password = "".join(random.choice(characters) for _ in range(length))
    return password
def main():
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 8:
                print("Password length should be at least 8 characters.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    while True:
        complexity = input("Enter the desired complexity of the password (low/medium/high): ").lower()
        if complexity in ["low", "medium", "high"]:
            break
        else:
            print("Invalid complexity level. Please choose 'low', 'medium', or 'high'.")
    password = generate_password(length, complexity)
    print(f"Your generated password is: {password}")
if __name__ == "__main__":
    main()
