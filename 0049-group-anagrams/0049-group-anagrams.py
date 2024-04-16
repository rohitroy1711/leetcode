# We can do this in O(n^2) we will write a function that takes two inputs and find out whether it is an anagram or not
# Make a for loop in the group anagrams run the outer loop from i = 0 to n-1 and run the inner for loop from j =  i+1 to n-1 and also make an new array that keeps track of the present round anagrams
# checkanagram(lis[i],lis[j]) if this returns true add these both to array of present round anagrams. after adding the pair into it try make the lis[j] to an empty string that takes care of repeatitions 
# if you donot find any anagram pair in the current round add the present item into the array

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:
                count = [0]*26
                for i in s:
                    count[ord(i)-ord('a')] += 1
                
                res[tuple(count)].append(s)
        return res.values()