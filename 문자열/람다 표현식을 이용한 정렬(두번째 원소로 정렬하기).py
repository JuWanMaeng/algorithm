class Solution:
    def reorderLogFiles(self, logs):
        digit,letter=[],[]
        for log in logs:
            if log.split()[1].isdigit():
                digit.append(log)
            else:
                letter.append(log)
                
        letter.sort(key=lambda x:(x.split()[1:],x.split()[0:]))      #람다함수 사용
        return letter+digit
        