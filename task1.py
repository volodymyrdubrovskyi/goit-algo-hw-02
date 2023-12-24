from queue import Queue


max_while_limit = 1000

# Створюємо чергу
q = Queue()

def generate_request():
    global q
    req = 'Go!'
    while req:
        req = input('створити нову заявку (пустий текст для завершення вводу заявок):')
        if req != '':
            q.put(req)
            print('черга: ', q.queue)

def process_request():
    global q
    if q.empty():
        print('черга пуста')
    w = 0
    while (not q.empty()) or (w < max_while_limit):
        print(q.queue)
        print(f'Request {q.get()} processed....')
        print(q.queue, '\n')
        w += 1

not_go_exit = True

w = 0
while (not_go_exit) or (w < max_while_limit):
    generate_request()
    process_request()
    not_go_exit = input('>>> Enter to STOP, other text for continue >>>')
    w += 1