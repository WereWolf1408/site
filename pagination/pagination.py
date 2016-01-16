class Pagination:
    instance = None
    list = []
    prev = None
    next = None
    pag_len = 10

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Pagination, cls).__new__(cls)
        return cls.instance

    def __init__(self, max_page=1, page=1):
        self.page = page
        self.max_page = max_page

    def firt_page(self):
        if self.max_page <= Pagination.pag_len:
            for i in range(1, self.max_page + 1):
                Pagination.list.append(i)
        else:
            for i in range(1, Pagination.pag_len + 1):
                Pagination.list.append(i)
                if i == 8:
                    Pagination.list.append('...')
                    Pagination.list.append(self.max_page)
                    Pagination.break_point(self, next=i)
                    break

    def last_page(self):
        Pagination.list.append(1)
        Pagination.list.append('...')
        for i in range(self.max_page - 7, self.max_page + 1):
            Pagination.list.append(i)
        Pagination.break_point(self, prev=Pagination.list[2])

    def create(self):
        Pagination.list.clear()

        if self.page == 1:
            Pagination.firt_page(self)
        elif self.page == self.max_page:
            Pagination.last_page(self)
        elif self.page == Pagination.next:
            Pagination.nnext(self)
        elif self.page == Pagination.prev:
            Pagination.pprev(self)
        return Pagination.list

    def pprev(self):
        if self.page - 8 <= 1:
            Pagination.firt_page(self)
        else:
            Pagination.list.append(1)
            Pagination.list.append('..')
            for i in range(self.page - 7, self.page):
                Pagination.list.append(i)
            Pagination.list.append('...')
            Pagination.list.append(self.max_page)
            Pagination.break_point(self, prev=Pagination.list[2],
                                   next=Pagination.list[8])

    def nnext(self):
        if self.page + 7 >= self.max_page:
            Pagination.last_page(self)
        else:
            Pagination.list.append(1)
            Pagination.list.append('...')
            for i in range(self.page + 1, self.page + 7):
                Pagination.list.append(i)
            Pagination.list.append('...')
            Pagination.list.append(self.max_page)
            Pagination.break_point(self, next=Pagination.list[7],
                                   prev=Pagination.list[2])

    def break_point(self, prev=None, next=None):
        Pagination.prev = prev
        Pagination.next = next

