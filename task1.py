from queue import Queue

max_while_limit = 1000

def generate_request(q:Queue):
    req = 'Go!'
    while req:
        req = input('створити нову заявку (пустий текст для завершення вводу заявок):')
        if req != '':
            q.put(req)
            print('черга: ', q.queue)
    return q

def process_request(q:Queue):
    if q.empty():
        print('черга пуста')
    w = 0
    while (not q.empty()) and (w < max_while_limit):
        print(q.queue)
        print(f'Request {q.get()} processed....')
        print(q.queue, '\n')
        w += 1
    return q


q = Queue()
not_go_exit = True
w = 0
while (not_go_exit) and (w < max_while_limit):
    q = generate_request(q)
    q = process_request(q)
    not_go_exit = input('>>> Enter to STOP, other text for continue >>>')
    w += 1