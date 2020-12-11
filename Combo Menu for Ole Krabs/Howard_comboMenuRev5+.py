def menu():
    return('''
                          GALLEY GRUB
    1 KRABBY PATTY.........1.25   7 KRABBY MEAL......3.50
    2   w/sea cheese.......1.50   8 DOUBLE KRABBY M..3.75
    3 DOUBLE KRABBY PATTY..2.00   9 TRiPLE KRABBY M..4.00
    4   w/sea cheese.......2.25  10 SALTY SEA DOG....1.25
    5 TRiPLE KRABBY PATTY..3.00  11 FOOTLONG.........2.00
    6   w/sea cheese.......3.25  12 SAiLORS SURPRiSE.3.00
                                  13 GOLDEN LOAF.....2.00
       CORAL BiTS                 14  w/sauce........2.50
    15  Small............1.00
    16  Medium...........1.25   20 KELP SHAKE........2.00
    17  Large............1.50       SEAFOAM SODA
                               21 Small.....1.00
     18 KELP RiNGS.......1.50  22 Medium....1.25
     19     salty sauce.. .50  23 Large.....1.50\n''')

def order():
    total = 0.0
    menuList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]   #indices of the Menu
    #the food according to the numbers (indices) they are connected too   v (below)
    #               1                          2                   3                   4                                    5                              6                       7              8                       9                10             11             12             13                  14                  15                  16                  17                  18                  19                  20                  21                   22                     23
    foodList = ["KRABBY PATTY","KRABBY PATTY w/sea cheese","DOUBLE KRABBY PATTY","DOUBLE KRABBY PATTY w/sea cheese","TRiPLE KRABBY PATTY","TRiPLE KRABBY PATTY w/sea cheese","KRABBY MEAL","DOUBLE KRABBY MEAL","TRiPLE KRABBY MEAL","SALTY SEA DOG","FOOTLONG","SAiLORS SURPRiSE","GOLDEN LOAF","GOLDEN LOAF w/sauce","CORAL BiTS (Small)","CORAL BiTS (Medium)","CORAL BiTS (Large)","KELP RiNGS","KELP RiNGS w/salty sauce","KELP SHAKE","SEAFOAM SODA (Small)","SEAFOAM SODA (Medium)","SEAFOAM SODA (Large)"]
    costList = [    1.25      ,             1.50          ,        2.00         ,               2.50               ,         3.00        ,              3.50                ,    3.50     ,        3.75        ,        4.00        ,      1.25     ,   2.00   ,      3.00        ,     2.00    ,         2.50        ,         1.00       ,        1.25         ,        1.50        ,    1.50    ,            2.00          ,     2.00   ,        1.00          ,         1.25          ,         1.50         ]
    #the costs of each food according to the number (indices) ^ (above)
    listList = []
    orderList = []
    print("Welcome to the Krusty Krab, May I take your order ?")
    print(menu())
    order = 100
    while order != 0:
        # while True:
        
        try:
            order= int(input("put the numbers, When you're done just type '0' \n"))
            if order in menuList:
                Indice = menuList.index(order)  #gets the indice that the ui is connected to
                Item = foodList[Indice]         #uses the indice to find the according food
                Cost = float(format(costList[Indice],'.2f'))   #uses the indice to find the according cost

                print(Cost)
                orderList.append(Item)
                total += Cost
                tax = total * 1.07
        except:
            print("Invalid Choice, Enter what's on the Menu (1-23) ")
    listList.append(orderList)    
    print("Subtotal: ",total)
    print("Tax: 7%")
    print("Total: ",tax)    
order()
    #But you could contain the top two lines into one
    #     orderList.append(order)

# print("Your total is", '${:,.2f}'.format(total))     #string formating

# print("Your combo menu is as follows" + order+ "sandwich")
"""
    print(
        "Your order is:,
    {0} sandwich,
    {1} drink,
    {2} fries,
    {3} packets
    For a total of, '${:,.2f}'
    .format(order,userShake,userCoral,userKetchup,total))
"""