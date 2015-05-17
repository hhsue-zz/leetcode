#!/usr/bin/python

class Solution:
    # @param beginWord, a string
    # @param endWord, a string
    # @param wordDict, a set<string>
    # @return an integer
    def ladderLength(self, beginWord, endWord, wordDict):
        nextWord = beginWord
        transformation = []
        transformation.append(beginWord)
        while True: 
            count = 0
            # check if next word is one away from endword
            print nextWord
            for i in range(len(endWord)):
                if nextWord[i] != endWord[i]:
                    count += 1
            print nextWord, count
            if count == 1:
                transformation.append(endWord)
                return transformation
            # if continue, find next nextWord
            for word in wordDict:
                count = 0
                # else find next word in transformation from wordDict
                for i in range(len(word)):
                    if word[i] != nextWord[i]:
                        count += 1
                if count == 1:
                    nextWord = word
                    transformation.append(word)
            
            #return -1

s=Solution()
print s.ladderLength('hit','cog',["hot","dot","dog","lot","log"])
#print s.ladderLength('hit','cog',["log","dot","dog","lot","hot"]) 

