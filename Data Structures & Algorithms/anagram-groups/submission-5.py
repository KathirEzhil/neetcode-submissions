class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def isAnagram(s1,s2):
            if len(s2) != len(s1):
                return False
            d1,d2 = {},{}
            for i in range(len(s1)):
                if s1[i] in d1:
                    d1[s1[i]] += 1
                else:
                    d1[s1[i]] = 1
            for i in range(len(s2)):
                if s2[i] in d2:
                    d2[s2[i]] += 1
                else:
                    d2[s2[i]] = 1
            if d1 == d2:
                return True
            return False
        
        new = []
        visited = set()

        for i in range(len(strs)):
            if i in visited:
                continue
            l = [strs[i]]
            for j in range(i+1,len(strs)):
                if (j not in visited) and isAnagram(strs[i],strs[j]):
                    l.append(strs[j])
                    visited.add(j)
            new.append(l)
        return new    
