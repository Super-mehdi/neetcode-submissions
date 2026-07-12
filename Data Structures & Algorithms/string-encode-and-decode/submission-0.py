class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) +"-"+ s
        return encoded_str
    def decode(self, s: str) -> List[str]:
        decoded_str = []
        n = len(s)
        i,j=0,0
        while (j<len(s)-1):
            while (s[i:j+1].isdigit()):
                j+=1
            k,l=j+1,(j+int(s[i:j]))
            decoded_str.append(s[k:l+1])
            i,j = l+1,l+1
        print(decoded_str)
        return decoded_str
