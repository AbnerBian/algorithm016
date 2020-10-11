class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hashmap={5:0,10:0}
        for i in bills:
            if(i==5):
                hashmap[i]+=1
            elif(i==10):
                hashmap[5]-=1
                hashmap[i]+=1
            else:
                if(hashmap[10]>0):
                    hashmap[10]-=1
                    hashmap[5]-=1
                else:
                    hashmap[5]-=3
            if(hashmap[5]<0):return False
        return True