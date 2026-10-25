class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            piece = str(len(s)) + "#" + s
            encoded_str += piece
        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        result = []
        i= 0
        while i < len(s):
            j = i 
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            i = j + 1
            
            decoded_piece = s[i:i+length]
            result.append(decoded_piece)
            i+= length

        return result
                
