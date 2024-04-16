# O(N) we can make an hash map for one string and then we can subtract all the occurances of the second string in the first hash map finall if the total characters of the hashmap is 0 then it is a valid anagram. or else it is not an valid anagram.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        count =0
        for i in s:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        for i in t:
            if i not in hashmap:
                return False
            else:
                if hashmap[i] >0:
                    hashmap[i] -=1
                else:
                    return False
        for i in hashmap:
            count += hashmap[i]
        if count == 0:
            return True
        else:
            return False
        