

movie_rating={"hacker": {"rating":[8.4,9.3,7],
                        "duration":200,
                         "release year":2002},
              
              "  i robot":{"rating":[5.6,8.9,9],
                       "duration":100,
                       "release year":2001},
              " the social network":{"rating":[2.8,9,4,7,4,1,],
                                      "duration":110,
                                       "release year":2021}}
add_dic={}
name=input("enter the movie name: ")
rating=int(input("rate the movie: "))
for key,value in movie_rating.items():
    
    if name in key:
        if rating >9:
            print("your are not in rating range")
        elif rating<=0:
            print("give input correct number for rating")
        elif rating>1:
            add_dic[key]=value['rating'].append(rating)
            value['rating']=sum(value['rating'])/len(value['rating'])
            print(movie_rating)
            
            
