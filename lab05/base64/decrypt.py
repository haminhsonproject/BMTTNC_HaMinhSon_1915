import base64

def main():
    try:
        with open("data.txt", "r") as file:
            encoded_string = file.read().strip()
            
        decodeed_bytes = base64.b64decode(encoded_string)
        decoded_string = decodeed_bytes.decode("utf-8")
            
        print("Chuoi sau giai ma", decoded_string)

    except Exception as e:
        print("Error", e)
        
if __name__ == "__main__":
    main()