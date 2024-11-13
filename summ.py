import os

def sum_results():
    total_count = 0
    result_files = os.listdir('results')
    for file in result_files:
        with open(os.path.join('results', file), 'r') as f:
            total_count += int(f.read())
    print(f'Total count of "a": {total_count}')

sum_results()