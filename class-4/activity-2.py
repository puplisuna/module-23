def no_notes(a):
    Q = [1000,500,200,100,50,10,5,2,1]
    x = 0
    for i in range(len(Q)):
        q= Q[i]
        x = a // q
        print("notes of{} : {}".format(q, x))
        a = a % q
amount = int(input("Enter the amount: "))
no_notes(amount)        