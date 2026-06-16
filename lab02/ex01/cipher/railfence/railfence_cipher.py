class RailFenceCipher:
    def __init__(self):
        pass
    
    def railfence_encrypt(self, plaintext, numrails):
        rails = [[]for _ in range(numrails)]
        railindex = 0
        direction  = 1
        for char  in plaintext:
            rails[railindex].append(char)
            if railindex == 0:
                direction = 1
            elif railindex == numrails - 1:
                direction = -1
                railindex += direction
            ciphertext =  ''.join(''.join(rail) for rail in rails)
            return ciphertext
        
    def railfence_decrypt(self, ciphertext, numrails):
        raillengths = [0] * numrails
        railindex = 0
        direction = 1
        
        for _ in range(len(ciphertext)):
            raillengths[railindex] += 1
            if railindex == 0:
                direction = 1
            elif railindex == numrails - 1:
                direction = -1
            railindex += direction
        
        rails = []
        start = 0
        for length in raillengths:
            rails.append(ciphertext[start:start + length])
            start += length
        plaintext = ""
        railindex = 0
        direction = 1
        
        for _ in range(len(ciphertext)):
            plaintext += rails[railindex][0]
            rails[railindex] = rails[railindex][1:]
            if railindex == 0:
                direction =1
            elif railindex == numrails -1:
                direction = -1
            railindex += direction
        return plaintext
            