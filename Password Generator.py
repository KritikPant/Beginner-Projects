import string
import random

while True:
    def password(userInput):
        specialCharacter = [random.choice(string.punctuation) for character in range(userInput)]
        wordLower = [random.choice(string.ascii_lowercase) for lower in range(userInput)]
        wordUpper = [random.choice(string.ascii_uppercase) for upper in range(userInput)]
        numbers = [random.choice(string.digits) for number in range(userInput)]
        generatedPassword = ''.join(specialCharacter + wordLower + wordUpper + numbers)
        generatedPassword = ''.join(random.choice(generatedPassword) for value in range(userInput))
        return generatedPassword

    question = int(input('Please enter the password length: '))
    answer = password(question)
    print(answer)
    input("Press enter for the next password: ")
