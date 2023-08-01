"""
Joyal was given a sentence. His task is to delete the two words that comes together and print the sentence so that the words in the output sentence have distinct words compared to their adjacent words. If no words are present in the output sentence print -1

Input Description:
You are given input string 'S'

Output Description:
Print the all the words that are left in the string 's' so that the words in the output sentence have distinct words compared to their adjacent words. Print -1 if no words are left

Sample Input :
I am john cena cena john
Sample Output :
I am
"""

def find_Adj(phrase):
    words=[i for i in sentence.split(" ")]
    length=len(words)
    word_list=[]
    for i in range(length-1):
        if words[i]==words[i+1]:
            x=word[i]
            word.replace(x,"")
            print(words)    
        else:
            if len(words) is none:
                return -1
sentence=input()
print(find_Adj(sentence))
