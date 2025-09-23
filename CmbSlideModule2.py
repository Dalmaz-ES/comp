class AlnSeq: 
    
    def __init__(self, seq1, seq2):
        self.seq1 = seq1
        self.seq2 = seq2
    
    def hamming_distance(self):
        self.distance = 0
        for a,b in zip(self.seq1, self.seq2):
            if a != b:
                distance += 1
        return self.distance
        
    def hamming_similarity(self):
        score = 0
        for i in range(len(self.seq1)):
            if self.seq1[i] == self.seq2[i]:
                score += 1
            else: 
                score -= 1
        
        return score
    
if __name__ == "__name__":
    a1n1 = AlnSeq("ACCCTCGCTAGATAAATAGATCTGATAG", "ACTCTCGCTAGATGAATAGGTCTGTTAG")
    print(a1n1.hamming_distance())
    print(a1n1.hamming_similarity())
 

        




#ZIP METHOD, for a,b in zip([1,2,3],[4,5,6]) 
#         print(a,b)
#               1 4
#               2 5
#               3 6




