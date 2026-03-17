# Time Complexity : Amortized O(1) for hasNext() and O(1) for next().
# Space Complexity : O(d) where d is the maximum depth of nested lists (stack size).
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
# Approach : We do lazy evaluation by keeping a stack of iterators to track where we are in each nested list.
# Every time hasNext() is called, we go as deep as needed to find the next integer.
# If we hit an integer, we save it and return true; else we just dive deeper.

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.st = [iter(nestedList)]
        self.nextEl = 0
    
    def next(self) -> int:
        return self.nextEl.getInteger()
    
    def hasNext(self) -> bool:
        while self.st:
            self.nextEl = next(self.st[-1], None)
            if self.nextEl is None:
                self.st.pop()
            else:
                if self.nextEl.isInteger():
                    return True
                else:
                    self.st.append(iter(self.nextEl.getList()))
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
