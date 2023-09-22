import string
import secrets
import random
from django.shortcuts import render, redirect

def password_generation_page(request):
    # Check if the generated password is already in the session
    generated_password = request.session.get('generated_password')

    if not generated_password:
        special_characters = string.punctuation.replace('"', '')  # Remove double quotation mark
        numbers = string.digits
        lowercase_letters = string.ascii_lowercase
        all_characters = special_characters + numbers + lowercase_letters

        password_length = secrets.choice(range(10, 19))
        password = [secrets.choice(special_characters), secrets.choice(numbers)]

        for _ in range(password_length - 2):
            password.append(secrets.choice(all_characters))

        random.shuffle(password)
        generated_password = ''.join(password)

        # Ensure that the last character is not a double quotation mark
        while generated_password.endswith('"'):
            generated_password = generated_password[:-1]

        # Store the generated password in the session
        request.session['generated_password'] = generated_password

    return render(request, 'password_generation_page.html', {'generated_password': generated_password})
