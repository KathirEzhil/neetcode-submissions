class Solution:
    def isPalindrome(self, s: str) -> bool:

        s2 = ""
        for i in s:
            if i.isalnum():
                s2 += i

        s1 = s2.lower().replace(" ","")
        print(s1)
        
        for i in range(len(s1)//2):
            
                
                if s1[i] != s1[-1-i]:
                    return False
        return True