clients = ["John","Marry","Kate"]

clientsHighPriority = ["Tob","Pete"]
clientsLowPriority = ["Vicky","Lessly"]
for c in range(len(clientsHighPriority)):
    clients.insert(c,clientsHighPriority[c])
for l in range(len(clientsLowPriority)):
    clients.append(clientsLowPriority[l])

def showclient(v):
    for i in range(len(v)):
        print(i+1,". ",v[i],sep="")

showclient(clients)
for t in range(100):
    name=input("Client name?\n")
    if name!="":
        prior=input("What prority?low/high\n")
        if prior=="high":
            clients.insert(0,name)
            showclient(clients)
            break
        elif prior=="low":
            clients.append(name)
            showclient(clients)
            break
        else:
            prior=input("Wrong Command.Try again")
    else:
        prior=input("Wrong Command.Try again")
    