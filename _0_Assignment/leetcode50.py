import time


class Solution:
    @staticmethod
    def longestPalindrome(s: str):
        # s_rever = s[::-1]
        # result = ''
        # for index1, value1 in enumerate(s):
        #     for index2, value2 in enumerate(s_rever):
        #         if value1 == value2:
        #     # index2 = s.index(value1)
        #             real_index = -index2
        #             c_str = s[index1:real_index]
        #             if c_str == c_str[::-1] and len(c_str) > len(result):
        #                 result = c_str
        # return result

        n = len(s)

        if n <= 1 or s == s[::-1]:
            return s

        start = 0
        r = 1

        for i in range(1, len(s)):
            test_1 = s[i - r - 1:i + 1]
            test_2 = s[i - r: i + 1]
            if i - r - 1 >= 0 and test_1 == test_1[::-1]:
                start = i - r - 1
                r += 2
            elif i - r >= 0 and test_2 == test_2[::-1]:
                start = i - r
                r += 1

        return s[start:start + r]
s = 'aabbaac'
s = 'ibawpzhrunsgfobmenlqlxnprtgijgbeicsuoihnmcekzmvtffmlpzuwlimuuzjhkzppmpqqrfwyrjrsltkypjpcjffpvhtdiwjdonutobpecsiqubiusvwsyhrddqjeqqpgofifmwvmcdjixjvjxrvyabqaqumfqiiqxizmhzevhxutsbgzcfggyyvolwaxfcpjhfpksxvgyxhddcssnxhygzvmyxrxqizzhpluxkautjmieximoskcffimctsfzgmihtoxkltopwobtfjvjymtuknxmsgevkeklprcaudidywwkfuhtatpeeiewczpwiegmpjquayfleczrvzekikbaeocpcurtxhcsysbbsyschxtrucpcoeabkikezvrzcelfyauqjpmgeiwpzcweieeptathufkwwydiduacrplkekvegsmxnkutmyjvjftbowpotlkxothimgzfstcmiffcksomixeimjtuakxulphzziqxrxymvzgyhxnsscddhxygvxskpfhjpcfxawlovyyggfczgbstuxhvezhmzixqiiqfmuqaqbayvrxjvjxijdcmvwmfifogpqqejqddrhyswvsuibuqiscepbotunodjwidthvpffjcpjpyktlsrjrywfrqqpmppzkhjzuumilwuzplmfftvmzkecmnhiousciebgjigtrpnxlqlnembofgsnurhzpwabi'
start_time = time.time()
print(Solution.longestPalindrome(s))
final_time = time.time()
print(final_time- start_time)