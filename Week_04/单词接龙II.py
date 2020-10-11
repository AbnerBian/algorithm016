class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        from collections import defaultdict,deque
        if(endWord not in wordList):
            return []
        hashmap=defaultdict(list)
        preWord=defaultdict(list)
        visited={beginWord:0}
        queue=deque([(beginWord,0)])
        for word in wordList:
            for i in range(len(beginWord)):
                tmp=word[:i]+'*'+word[i+1:]
                hashmap[tmp].append(word)
        while(queue):
            curr,level=queue.popleft()
            for i in range(len(curr)):
                tmp=curr[:i]+'*'+curr[i+1:]
                for word in hashmap[tmp]:
                    if(word not in visited):
                        visited[word]=level+1
                        queue.append((word,level+1))
                    if(visited.get(word)==level+1 and word!=curr):
                        preWord[word].append(curr)
                    if(endWord in visited and visited.get(endWord)<level+1):
                        break
        print(visited)
        print(preWord)
        if(endWord not in visited):
            return []
        res=[[endWord]]
        while(res[0][0]!=beginWord):
            res=[[word]+r for r in res for word in preWord[r[0]]]
        return res