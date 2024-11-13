import string
import random
import os

def create_text_files():
    os.makedirs('text_files', exist_ok=True)
    for i in range(100):
        with open(f'text_files/file_{i}.txt', 'w') as f:
            f.write(''.join(random.choices(string.ascii_lowercase, k=1000)))

create_text_files()