class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if(endWord not in wordList):
            return 0
        from collections import defaultdict
        from collections import deque
        visited=defaultdict(int)
        hashmap=defaultdict(list)
        stack=deque([(beginWord,0)])
        visited={beginWord:0}
        for word in wordList:
            for i in range(len(beginWord)):
                tmp=word[:i]+'*'+word[i+1:]
                hashmap[tmp].append(word)
        while(stack):
            currentWord, level =stack.popleft() 
            for i in range(len(currentWord)):
                tmp=currentWord[:i]+'*'+currentWord[i+1:]
                if(tmp in hashmap):
                    for word in hashmap[tmp]:
                        if(word not in visited):
                            visited[word]=level+1
                            stack.append((word,level+1))
            if(endWord in visited):
                print(visited)
                return visited[endWord]+1
        return 0