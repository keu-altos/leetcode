class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap1 = {}
        hashMap2 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in hashMap1:
                hashMap1[s[i]]+=1
            else:
                hashMap1[s[i]]=1
            if t[i] in hashMap2:
                hashMap2[t[i]]+=1
            else:
                hashMap2[t[i]]=1
        return hashMap2 == hashMap1


if __name__ == "__main__":
    solution = Solution()
    s = "racecar" 
    t = "carrace"
    print(solution.isAnagram(s, t))
    s = "jar"
    t = "jam"
    print(solution.isAnagram(s, t))
