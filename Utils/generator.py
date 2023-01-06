#Generating Random Bits
import random
def generate(bit_size,fixed_sequence=False,fixed_size=0,fixed_freq=0):
    bits = ["0","1"]
    sequence = []
    if fixed_size> 0:
        for i in range(fixed_freq):
            sequence.append("0"*fixed_size)
    for i in range(bit_size-(fixed_size*fixed_freq)):
        sequence.append(random.choice(bits))
    #Shuffling The Bits To Make Consecutive Zeros Random
    random.shuffle(sequence)
    #Mapping The Numbers back to int
    sequence = list(map(int,list("".join(sequence))))
    return sequence

#Getting Longest Palindromic SubString
def get_modified_string(sequence):
    i = 0
    modified_sequence = ["#"]
    while(i<len(sequence)):
        modified_sequence.append(sequence[i])
        modified_sequence.append("#")
        i +=1
    return modified_sequence

def manachers_algorithm(sequence):
    sequence = get_modified_string(sequence)
    size = len(sequence)
    lps = [0] * size
    c = 0
    r = 0
    maxlen = 0
    index = 0
    for i in range(size):
        mirror = (2*c) - i
        if(i<r):
            lps[i] = min(r-i,lps[mirror])
        a = i + (1+lps[i])
        b = i - (1+ lps[i])
        while(a <size and b>=0 and sequence[a]==sequence[b]):
            lps[i] += 1
            a +=1
            b -=1
        if (i + lps[i] > r):
            c = i
            r = i + lps[i]
            if(lps[i]>maxlen):
                maxlen = lps[i]
                index = i
    ans = sequence[index-maxlen:index+maxlen+1]
    ans = [i for i in ans if i!='#']
    return ans