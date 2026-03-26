from datetime import datetime, timedelta

class DateIterator:
    def __init__(self, start_date, end_date):
        if isinstance(start_date, str):
            self.start = datetime.strptime(start_date, '%Y-%m-%d').date()
        else:
            self.start = start_date

        if isinstance(end_date, str):
            self.end = datetime.strptime(end_date, '%Y-%m-%d').date()
        else:
            self.end = end_date

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if (self.current > self.end)and((self.start<self.end)or(self.start==self.end))or(self.current < self.end)and(self.start>self.end):
            raise StopIteration
        current_date = self.current
        self.current += timedelta(days= (-1 if self.start > self.end else 1))
        return current_date

for i in [-1,0,1]:
    for j in [1,2,3]:
        print(f"i => {i:2} | j => {j} | i*j => {i*j:2} | {15} , {15+i*j} |",list(DateIterator(f'2025-11-{15}',f'2025-11-{15+i*j}')))