list = [10,22,17,35,45,6,17,18,18,17]

most_occuring={}

for  i in list:
    if i  in most_occuring:
        most_occuring[i] +=1
    else:
        most_occuring[i] =1 


print (most_occuring)
most_occured =max(most_occuring,key=most_occuring.get)

print(most_occured,">>",most_occuring[most_occured])
