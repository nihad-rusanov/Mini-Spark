class RDD:
    def __init__(self, data):
        self.data = data
        self.operations = []  

    def map(self, func):
        self.operations.append(('map', func))
        return self

    def filter(self, func):
        self.operations.append(('filter', func))
        return self

    def collect(self):
        result = self.data
        for op, func in self.operations:
            if op == 'map':
                result = list(map(func, result))
            elif op == 'filter':
                result = list(filter(func, result))
        return result


