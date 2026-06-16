class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speed_position = [sp for sp in zip(speed,position)]
        speed_position.sort(key = lambda x: x[1])
        time = [(target - sp[1])/sp[0] for sp in speed_position]
        res = 0
        while (time):
            t = time.pop()
            while ( time and t >=time[-1]):
                time.pop()
            res+=1
        return res