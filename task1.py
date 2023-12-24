from queue import Queue


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
    while not q.empty():
        print(q.queue)
        print(f'Request {q.get()} processed....')
        print(q.queue, '\n')

not_go_exit = True

while not_go_exit:
    generate_request()
    process_request()
    not_go_exit = input('>>> Enter to STOP, other text for continue >>>')