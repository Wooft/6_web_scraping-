class Habr:

    def __init__(self, finish):
        self.start = 0
        self.finish = finish
        pass

    def __iter__(self):
        self.cursor = self.start - 1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == 0:
            self.page = 'https://habr.com/ru/all/page'
        if self.cursor > 0:
            self.page = f'https://habr.com/ru/all/page{self.cursor}/'
        if self.cursor >= self.finish:
            raise StopIteration

        return self.page

