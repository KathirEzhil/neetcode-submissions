class Solution:

    def encode(self, strs: List[str]) -> str:

        if strs == []:
            return "empty"
        new = strs[0]
        for i in range(1,len(strs)):
            new = new + "/joiner_string/" + strs[i]
        return new


    def decode(self, s: str) -> List[str]: 
        
        if s == "empty":
            return []
        return s.split("/joiner_string/")