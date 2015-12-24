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
        if self.max_page < MyPagination.pag_len:
            del(MyPagination.list[:])
            MyPagination.get_simple_list(self)
        elif self.page < MyPagination.pag_len-1:
            del(MyPagination.list[:])
            MyPagination.next(self)
        elif self.page + MyPagination.pag_len >= self.max_page:
            del(MyPagination.list[:])
            MyPagination.previous(self)
        elif self.page == self.last_next_page:
            del(MyPagination.list[:])
            MyPagination.last_next(self)
        elif self.page == self.last_prev_page:
            del(MyPagination.list[:])
            MyPagination.last_prev(self)
        #     еже третий случай, если ввести номер страницы через url и не выпониться ни одно из условий
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
            MyPagination.last_next_page = self.list[len(MyPagination.list) - 3]
            MyPagination.last_prev_page = self.list[len(MyPagination.list) - 3]

    def last_next(self):
        end = self.page + MyPagination.pag_len
        MyPagination.list.append(1)
        MyPagination.list.append('...')

        for value in range(self.page+1, end):
            self.list.append(value)

        MyPagination.list.append('...')
        MyPagination.list.append(self.max_page)
        self.last_next_page = MyPagination.list[len(MyPagination.list) - 3]
        self.last_prev_page = MyPagination.list[2]

    def next(self):
        for page in range(1, self.max_page):
            if page == MyPagination.pag_len:
                MyPagination.list.append('...')
                MyPagination.list.append(self.max_page)
                MyPagination.last_next_page = MyPagination.list[len(MyPagination.list) - 3]
                break
            MyPagination.list.append(page)

    def previous(self):
        first = self.max_page - MyPagination.pag_len + 1
        MyPagination.list.append(1)
        MyPagination.list.append('...')
        MyPagination.last_prev_page = first

        for page in range(first, self.max_page+1):
            MyPagination.list.append(page)


# pagination = Pagination(max_page=1, page=1)
# print(pagination.paginations())
# pagination = Pagination(max_page=40, page=9)
# print(pagination.paginations())
# pagination = Pagination(max_page=5,  page=1)
# print(pagination.paginations())
# pagination = Pagination(max_page=10, page=1)
# print(pagination.paginations())
# pagination = Pagination(max_page=11, page=8)
# print(pagination.paginations())
# pagination = Pagination(max_page=12, page=9)
# print(pagination.paginations())
