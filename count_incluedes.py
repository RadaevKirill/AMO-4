import os

def count_a_in_file(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
    count = text.count('a')
    result_file = file_path.replace('text_files', 'results').replace('.txt', '.res')
    with open(result_file, 'w') as f:
        f.write(str(count))

def process_files():
    os.makedirs('results', exist_ok=True)
    files = os.listdir('text_files')
    for file in files:
        count_a_in_file(os.path.join('text_files', file))

process_files()