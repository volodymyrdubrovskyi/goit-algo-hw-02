from collections import deque


def input_text():
    text_init = input('введіть текст для перевірки >>> ')
    text = text_init.lower()
    text = text.replace(' ','')
    return text, text_init

def txt_to_que(text):
    q = deque()
    if len(text) > 0:
        for i in range(len(text)):
            q.append(text[i])
    return q

def is_polyndrome(q:deque):
    for i in range(len(q)//2):
        if q.pop() != q.popleft():
            return 'Ні'
    return 'Так'

text, text_init = input_text()
q = txt_to_que(text)
# print(q, text_init)
print(f'Текст "{text_init}" є паліндромом? Відповідь: {is_polyndrome(q)}')