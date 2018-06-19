class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        MStable = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ABCtable = "abcdefghijklmnopqrstuvwxyz"
        translations = [''.join([MStable[ABCtable.index(x)] for x in word]) for word in words]
        print(translations)
        return len(set(translations))
