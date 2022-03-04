
from errno import ENETDOWN
from re import U
import this

from pkg_resources import WorkingSet

def main():
    doc= """

        **************************************
        **    Welcome to the Snakes Cafe!   **
        **    Please see our menu below.    **
        **
        ** To quit at any time, type "quit" **
        **************************************

        Appetizers
        ----------
        Wings
        Cookies
        Spring Rolls

        Entrees
        -------
        Salmon
        Steak
        Meat Tornado
        A Literal Garden

        Desserts
        --------
        Ice Cream
        Cake
        Pie

        Drinks
        ------
        Coffee
        Tea
        Unicorn Tears

        ***********************************
        ** What would you like to order? **
        *********************************** 
    """
        # define a 4 dictionaries the main types of items

    Appetizers = {'Wings': 0, 'Cookies': 0, 'Spring Rolls': 0}
    Entrees = {'Salmon': 0, 'Steak': 0,
                'Meat Tornado': 0, 'A Literal Garden': 0}
    Desserts = {'Ice Cream': 0,
                    'Cake': 0, 'Pie': 0}
    Drinks = {'Coffee': 0, 'Tea': 0, 'Unicorn Tears': 0}
        # take user input            
    # print(help(main))
    print(doc)
    user = str(input('>')).capitalize()
        # looping and take orders till user enter quit 
    while user != 'Quit':
        # check if teh input were in any of the 4 dictionarires 
        if user in Appetizers.keys():
            for key in Appetizers.keys():
                if key == user:
                    Appetizers[user]+=1
                    print(str(Appetizers[user])+" order of "+user+" Added to the menu") 
        elif user in Entrees.keys():
            for key in Entrees.keys():
                if key ==user:
                    Entrees[user]+=1
                    print(str(Entrees[user])+" order of "+user+" Added to the menu") 
        elif user in Desserts: 
            for key in Desserts.keys():
                if key == user:
                    Desserts[user]+=1
                    print(str(Desserts[user])+" order of "+user+" Added to the menu") 
        elif user in Drinks: 
            for key in Drinks.keys():
                if key == user:
                    Drinks[user]+=1
                    print(str(Drinks[user])+" order of "+user+" Added to the menu") 
        else:
            print('Wrong input ')           
        
        user = str(input('\n>')).capitalize()

main()
        