import random
for character_set in range(8):
    
    character_set=["a","b","c","d","e","f","g",1,2,34,5,6,"@","#","$","E","D","R","F","N","B"]
    randome_character=random.choice(character_set)
    print(randome_character,end= "")
    b=[]
    b.append(randome_character)
        
    length=len(b)

    print(length,end="")
    password_dic={}
    password_dic[length]=randome_character
    print(password_dic)
