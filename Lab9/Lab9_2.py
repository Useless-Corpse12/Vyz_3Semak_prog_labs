from datetime import datetime, timedelta

class DateIterator:
    def __init__(self, start_date, end_date,n=None):
        if isinstance(start_date, str):
            self.start = datetime.strptime(start_date, '%Y-%m-%d').date()
        else:
            self.start = start_date

        if isinstance(end_date, str):
            self.end = datetime.strptime(end_date, '%Y-%m-%d').date()
        else:
            self.end = end_date

        if n==None :
            self.n=abs((self.end-self.start).days)
        elif n<1 or int(n)!=n :
            raise ValueError("количество итераций должно быть целым и >=1")
        else:
            self.n=n

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        ratio = self.i / (self.n) if self.n > 0 else 0
        days = round(ratio * abs((self.end - self.start).days))
        current_date = self.start + timedelta(days=days) * (1 if self.start <= self.end else -1)
        self.i += 1
        return current_date


for i in [-1,0,1]:
    for j in [1,2,3]:
        print(f"i => {i:2} | j => {j} | i+j+1 => {i+j+1} |{15-i*j},{15+i*j} |",list(DateIterator(f'2025-11-{15-i*j}',f'2025-11-{15+i*j}',j+i+1)))
print("n не ввели с 13 по 16 число",list(DateIterator('2025-11-13','2025-11-16')))