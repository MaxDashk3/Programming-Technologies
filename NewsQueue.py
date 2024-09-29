class News:
    def __init__(self, title, content):
        self.title = title
        self.content = content


#shows and deletes news in front of the queue
def pop(queue):
    if len(queue)==0:
        raise ValueError("Queue is empty")

    print(queue[0].title)
    print(queue[0].content)
    print()
    queue.pop(0)
    return queue

#adds news to queue
def add(title, content, queue):
    if not title or not content:
        raise ValueError("Data is empty")

    queue.append(News(title, content))
    return queue

#shows all news
def view_all(queue):
    if len(queue) == 0:
        raise ValueError("Queue is empty")

    for i in queue:
        print(i.title,"\n",i.content,"\n")

#gets index of news by its title (returns -1 if not found)
def title_index(title, queue):
    for i in range(len(queue)):
        if queue[i].title == title:
            return i
    return -1

#gets news item by title
def news_by_title(title, queue):
    index = title_index(title, queue)
    if index==-1:
        raise ValueError("Title not found")

    return queue[index]