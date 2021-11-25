from django.shortcuts import render

# Create your views here.
import random


def generate_session_token(length = 10):
    #you can choose another way to like using the list of values
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97,123)] + [str(i) for i in range(10)]) for _ in range(length))