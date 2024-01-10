from collections import defaultdict


class FrequencyTracker:

    def __init__(self):
        self.num2freq = defaultdict(int)
        self.freq2freqq = defaultdict(int)

    def add(self, number: int) -> None:
        if self.num2freq[number] != 0:
            self.freq2freqq[self.num2freq[number]] -= 1
        self.num2freq[number] += 1
        self.freq2freqq[self.num2freq[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.num2freq[number] > 0:
            self.freq2freqq[self.num2freq[number]] -= 1
            self.num2freq[number] -= 1
            self.freq2freqq[self.num2freq[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        if self.freq2freqq[frequency]:
            return True
        else:
            return False




# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)