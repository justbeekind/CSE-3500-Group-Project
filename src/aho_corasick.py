class AhoCorasick:
    # Constructor
    def __init__(self, patterns: list[str]):
        pass

    # Searches for a pattern -> returns a list of tuples with (index, pattern)
    def search(self, pattern: str) -> list[(int, str)]:
        pass

class TrieNode:
    def __init__(self):
        self.children = {}  # Character -> TrieNode
        self.fail = None    # Failure link
        self.output = []    # Patterns ending at this node


class Trie:
    # Constructor
    def __init__(self):
        self.root = TrieNode()

    # Insert a pattern into the Trie
    def insert(self, pattern: str):
        current = self.root

        for char in pattern:
            if char not in current.children:
                current.children[char] = TrieNode()

            current = current.children[char]

        # Mark the end of the pattern
        current.output.append(pattern)

    # Insert multiple patterns
    def insert_patterns(self, patterns: list[str]):
        for pattern in patterns:
            self.insert(pattern)