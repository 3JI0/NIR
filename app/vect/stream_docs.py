'''Считывает и выдает по одному конкретному документу за раз'''

def stream_docs(path):
    with open(path, 'r', encoding = 'utf-8') as csv:
        next(csv) #Пропустить заголовок
        for line in csv:
            text, label = line[:-3], int(line[-2])
            yield text, label