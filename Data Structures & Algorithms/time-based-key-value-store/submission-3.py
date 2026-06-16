class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store: return ""
        l , r = 0 , len(self.store[key])-1
        res = -1
        while l <= r:
            m = l+ (r-l)//2
            if self.store[key][m][1] <= timestamp:
                res = max(res, m)
                l = m + 1
            else:
                r = m - 1
        if res == -1: return ""
        return self.store[key][res][0]


        
