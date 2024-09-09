from .data import parse_file


def make_workers_dict(workers:list) -> list[dict]:
    if not workers:
        return
    dict_workers = []
    for worker in workers:
        name, salary = worker.split(',')
        dict_workers.append({
            'name' : name,
             'salary' : int(salary)})
    return dict_workers

def total_salary(path: str) -> tuple:
    try:    
        workers = parse_file(path)
        dict_workers = make_workers_dict(workers)
        sum = 0
        for worker in dict_workers:
            sum += worker['salary']
        average_salary = round(sum / len(dict_workers), 1)
        return (sum, average_salary)
    except TypeError:
        print('Bad data!')
