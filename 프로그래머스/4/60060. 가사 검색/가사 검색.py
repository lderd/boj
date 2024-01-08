class Node(object):
    def __init__(self):
        self.data = {}
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word):
        current_node = self.head
        l = len(word)
        for char in word:
            if l not in current_node.data:
                current_node.data[l] = 0
            if char not in current_node.children:
                current_node.children[char] = Node()
            current_node.data[l] += 1
            current_node = current_node.children[char]
            l -= 1

    def search(self, word):
        current_node = self.head
        l = len(word)
        for char in word:
            if char == '?':
                break
            else:
                if char in current_node.children:
                    current_node = current_node.children[char]
                    l -= 1
                else:
                    return 0
        if l in current_node.data:
            return current_node.data[l]
        return 0


def solution(words, queries):
    answer = []
    pre = Trie()
    suffix = Trie()
    for word in words:
        pre.insert(word)
        suffix.insert(''.join(reversed(word)))
    for q in queries:
        if q[0] == '?':
            answer.append(suffix.search(''.join(reversed(q))))
        else:
            answer.append(pre.search(q))
    return answer