def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
    base_words = set(words)

    @lru_cache(None)
    def check(word: str) -> bool:
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in base_words and suffix in base_words:
                return True
            if prefix in base_words and check(suffix):
                return True
        return False

    ans = []

    for word in words:
        if check(word):
            ans.append(word)
    return ans