class Trie:
    def __init__(self, val):
        self.map = {}
        self.val = val
        self.end = False


class Solution:
    # @return: The longest common prefix
    def longestCommonPrefix(self, strs):
        # write your code here
        # use trie
        root = Trie("")
        for str in strs:
            node = root
            for char in str:
                if char not in node.map:
                    node.map[char] = Trie(node.val + char)
                node = node.map[char]
            node.end = True
        node = root
        while len(node.map.keys()) == 1:
            if node.end: break
            key = node.map.keys()[0]
            node = node.map[key]
        return node.val
    # @param strs: A list of strings


if __name__ == "__main__":
    sl = Solution()
    print sl.longestCommonPrefix(["", "ab", "abc"])
