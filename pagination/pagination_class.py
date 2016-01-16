class MyPagination:
    instance = None
    last_prev_page = None
    last_next_page = None
    pag_len = 10
    list = []

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(MyPagination, cls).__new__(cls)
        return cls.instance

    def __init__(self, max_page, page=1):
        self.page = page
        self.max_page = max_page

    def paginations(self):
        MyPagination.list.clear()

        if self.max_page < MyPagination.pag_len:
            MyPagination.get_simple_list(self)
        elif self.page < MyPagination.pag_len-1:
            MyPagination.next(self)
        elif self.page + MyPagination.pag_len >= self.max_page:
            MyPagination.previous(self)
        elif self.page == self.last_next_page:
            MyPagination.last_next(self)
        elif self.page == MyPagination.last_prev_page:
            MyPagination.last_prev(self)
        return MyPagination.list

    def get_simple_list(self):
        for page in range(1, self.max_page + 1):
            MyPagination.list.append(page)

    def last_prev(self):
        end = self.page - MyPagination.pag_len
        MyPagination.list.append(1)
        MyPagination.list.append('...')

        for value in range(end, self.page):
            MyPagination.list.append(value)
            MyPagination.list.append('...')
            MyPagination.list.append(self.max_page)
            MyPagination.break_point(self, next=self.list[len(MyPagination.list) - 3],
                                     prev=self.list[len(MyPagination.list) - 3])

    def last_next(self):
        end = self.page + MyPagination.pag_len
        MyPagination.list.append(1)
        MyPagination.list.append('...')

        for value in range(self.page+1, end):
            self.list.append(value)

        MyPagination.list.append('...')
        MyPagination.list.append(self.max_page)
        MyPagination.break_point(self, next=MyPagination.list[len(MyPagination.list) - 3], prev=MyPagination.list[2])

    def next(self):
        for page in range(1, self.max_page):
            if page == MyPagination.pag_len:
                MyPagination.list.append('...')
                MyPagination.list.append(self.max_page)
                MyPagination.break_point(self, next=MyPagination.list[len(MyPagination.list) - 3])
                break
            MyPagination.list.append(page)

    def previous(self):
        first = self.max_page - MyPagination.pag_len + 1
        MyPagination.list.append(1)
        MyPagination.list.append('...')
        MyPagination.break_point(self, prev=first)

        for page in range(first, self.max_page+1):
            MyPagination.list.append(page)

    def break_point(self, prev=None, next=None):
        MyPagination.last_next_page = next
        MyPagination.last_prev_page = prev

pagination = MyPagination(max_page=13, page=30)
pagination = MyPagination(max_page=21, page=30)
print(pagination.paginations())
