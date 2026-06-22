class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0": return "0"
        zero = 0
        res = ""
        for i in range(len(num2)-1,-1,-1):
            res = self.add(res, self.mul(num1,num2[i],zero))
            zero+=1
        return res

    def mul(self, num1, num2, zero):
        num1 = num1[::-1]
        n2 = int(num2)
        carry = 0
        res = []
        i = 0
        while i < len(num1) or carry:
            if i == len(num1): 
                res.append(str(carry))
                break
            n1 = int(num1[i])
            n3 = n1 * n2 + carry
            res.append(str(n3%10))
            carry = n3//10
            i+=1
        return "".join(res[::-1] + ["0"] * zero) 
    
    def add(self, num1, num2):
        num1 = num1[::-1]
        num2 = num2[::-1]
        i = 0
        res = []
        carry = 0
        while i < len(num1) or i < len(num2) or carry:
            n3 = 0
            if i < len(num1): n3+=int(num1[i])
            if i < len(num2): n3+=int(num2[i])
            if carry: n3+=carry
            res.append(str(n3 % 10))
            carry = n3 //10
            i+=1
        return "".join(res[::-1])

