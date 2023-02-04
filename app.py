uarr=barr={}
available_Business=[]
class user:

    def __init__(self, username=None,password=None,message=[],notif=[],btype=None,sid=None,date=None,subscribe=None):
        self.username = username
        self.password = password
        self.message = message
        self.notif = notif
        self.btype = btype
        self.sid = sid
        self.date = date
        self.subscribe = subscribe
    def adder(self,uarr):
        uarr.update({self.username:[self.password]})

class buisness:
    def __init__(self, username=None,password=None,price=0,num_row=0,message=[],notif=[],btype=None):
        self.username = username
        self.password = password
        self.price = price
        self.num_row = num_row
        self.message = message
        self.notif = notif
        self.btype =btype
    def adder(self,barr):
        barr.update({self.username:[self.password]})

def signin():
    print("ENTER TYPE OF USER")
    ux=int(input("Enter 0 for user, 1 for Buisness"))

    username = input("ENTER USERNAME: ").lower()
    password = input("ENTER PASSWORD: ")
    if ux==0:
        if username in uarr.keys() :
            if password== uarr[username][0]:
                print("Login Success as User ")
                return(username,password,ux)
            else:
                print("Password is incorrect")
        else:
            print("Username doesn't exist")

    elif ux==1:
        if username in barr.keys():
            if password == barr[username][0]:
                print("Login Success as Buisness")
                return (username, password, ux)
            else:
                print("Password is incorrect")
        else:
            print("Username doesn't exist")

    else:
        print("Login success as Admin")

def buisness_select(usernamex):
    print("Select Buisness")
    print("1. Restaurant")
    print("2. Cinema")
    print("3. Hotel")
    print("4. Train")
    print("5. Airplane")
    print("6. Exit")
    buisness = int(input("Enter your choice: "))
    if buisness == 1:
        print("Restaurant")
        btype=1
    elif buisness == 2:
        print("Cinema")
        btype=2
    elif buisness == 3:
        print("Hotel")
        btype=3
    elif buisness == 4:
        print("Train")
        btype=4
    elif buisness == 5:
        print("Airplane")
        btype=5
    elif buisness == 6:
        print("Exit")
        btype=None
    else:
        print("Invalid Choice")
        btype=None
    if btype!=None:
        # available_Business.append([usernamex,btype])
        barr[usernamex].append(btype)


    return btype

def create_seat_matrix(usernamex):
    num_row = int(input(print("Enter Number of Rows")))
    if num_row>3:
        matrix = [[0]*num_row for _ in range(num_row)]

        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))
        barr[usernamex].append(num_row,matrix)


    return [matrix,num_row]

def price(usernamex,matrix):
    if len(matrix)>3:
        price = int(input(print("Enter the base price")))
        return price
        barr[usernamex].append(num_row)
        print(barr)
    else:
        print("Add more rows")
        return None
        pass





if __name__ == "__main__":


    mudit = garv = ankur = kisha = muskan = user()
    mudit.username = "mudit"
    mudit.password = "123"
    mudit.adder(uarr)
    garv.username = "garv"
    garv.password = "123"
    garv.adder(uarr)
    kisha.username = "kisha"
    kisha.password = "123"
    kisha.adder(uarr)
    muskan.username = "muskan"
    muskan.password = "123"
    muskan.adder(uarr)
    ankur.username = "ankur"
    ankur.password = "123"
    ankur.adder(uarr)

    john = jack = julie = lily = mahesh = buisness()
    john.username = "john"
    john.password = "321"
    john.adder(barr)
    jack.username = "john"
    jack.password = "321"
    jack.adder(barr)
    julie.username = "julie"
    julie.password = "321"
    julie.adder(barr)
    lily.username = "lily"
    lily.password = "321"
    lily.adder(barr)
    mahesh.username = "mahesh"
    mahesh.password = "32"
    mahesh.adder(barr)


## Code starts here
    details = list(signin())
    usernamex = details[0]
    passwordx = details[1]
    user_typex = details[2]
    # print(details)
    if user_typex == 1:
    ## Buisness Options
        print("Welcome "+ usernamex)
        btype = buisness_select(usernamex)
        res = create_seat_matrix(usernamex)
        matrix=res[0]
        num_row=res[1]
        price = price(usernamex,matrix)
        available_Business.append([usernamex,btype,num_row,price])
        print(available_Business)

        # matrix[0][0]=1
        # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))




