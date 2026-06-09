book=[1,0,2,3,1,1,0,5,3,7,0,5]
count=0
for book in book:
    if book==0:
        count+=1
        print("overdues books=",count)
        