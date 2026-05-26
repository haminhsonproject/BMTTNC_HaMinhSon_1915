class PlayFairCipher:
    
    def create_playfair_matrix(self, key):

        key = key.upper().replace("J", "I")

        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

        matrix = []

        for letter in key:
            if letter in alphabet and letter not in matrix:
                matrix.append(letter)

        for letter in alphabet:
            if letter not in matrix:
                matrix.append(letter)

        playfairmatrix = [matrix[i:i+5] for i in range(0, 25, 5)]

        return playfairmatrix

    def findlettercoords(self, matrix, letter):

        for row in range(5):
            for col in range(5):

                if matrix[row][col] == letter:
                    return row, col

    def split_pairs(self, text):

        text = text.upper().replace("J", "I").replace(" ", "")

        pairs = []

        i = 0

        while i < len(text):

            a = text[i]

            if i + 1 < len(text):

                b = text[i + 1]

                if a == b:

                    pairs.append(a + "X")
                    i += 1

                else:

                    pairs.append(a + b)
                    i += 2

            else:

                pairs.append(a + "X")
                i += 1

        return pairs

    def playfair_encrypt(self, plaintext, matrix):

        pairs = self.split_pairs(plaintext)

        encrypted_text = ""

        for pair in pairs:

            row1, col1 = self.findlettercoords(matrix, pair[0])
            row2, col2 = self.findlettercoords(matrix, pair[1])

            # same row
            if row1 == row2:

                encrypted_text += (
                    matrix[row1][(col1 + 1) % 5]
                    + matrix[row2][(col2 + 1) % 5]
                )

            # same column
            elif col1 == col2:

                encrypted_text += (
                    matrix[(row1 + 1) % 5][col1]
                    + matrix[(row2 + 1) % 5][col2]
                )

            # rectangle
            else:

                encrypted_text += (
                    matrix[row1][col2]
                    + matrix[row2][col1]
                )

        return encrypted_text

    def playfair_decrypt(self, ciphertext, matrix):

        ciphertext = ciphertext.upper()

        decrypted_text = ""

        for i in range(0, len(ciphertext), 2):

            pair = ciphertext[i:i+2]

            row1, col1 = self.findlettercoords(matrix, pair[0])
            row2, col2 = self.findlettercoords(matrix, pair[1])
            if row1 == row2:

                decrypted_text += (
                    matrix[row1][(col1 - 1) % 5]
                    + matrix[row2][(col2 - 1) % 5]
                )

            elif col1 == col2:

                decrypted_text += (matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
                )
            else:
                decrypted_text += (matrix[row1][col2] + matrix[row2][col1]
                )
        banro = ""
        for i in range(0, len(decrypted_text)-2, 2):
            if decrypted_text[i] == decrypted_text[i+2]:
                banro += decrypted_text[i]
            else:
                banro += decrypted_text[i] + "" + decrypted_text[i+1]
                
        if decrypted_text[-1] == "X":
            banro += decrypted_text[-2]
        else:
            banro += decrypted_text[-2]
            banro += decrypted_text[-1]
        return banro    