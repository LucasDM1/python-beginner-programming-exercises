# Your code here!!

def sing():
    counter=0
    for i in range(1,10):
       
        if counter == 4:
            print("whisper words of wisdom, let it be, let it be,")
            counter+=1
        elif counter == 8:
            print("there will be an answer, let it be")
            counter+=1
        else:
            print("let it be,")
            counter+=1
    
sing()


