class Solution:
	def findSubstring(self, s: str, words ) -> list[int]:

		rex = []
		word_l = len(words[0])
		d_word = {}
		for item in words:
			d_word[item] = d_word.get(item,0)+1

		idx = 0
		while idx < len(s):
			i = idx
			d_curr = {}
			if s[i:i+word_l] in words:
				for _ in range(len(words)):
					if s[i:i+word_l] in words:
						d_curr[s[i:i+word_l]] = d_curr.get(s[i:i+word_l],0) + 1
						i += word_l
					else:
						break
			if d_curr == d_word:
				rex.append(idx)

			idx += 1
		return rex