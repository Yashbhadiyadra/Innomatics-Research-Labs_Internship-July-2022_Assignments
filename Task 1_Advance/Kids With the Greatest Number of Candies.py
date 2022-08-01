class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        ans=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies >= max(candies):
                ans.append(True)
            else:
                ans.append(False)
        return ans
