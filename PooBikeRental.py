import datetime as dt 

class BikeRental: 

    def __init__(self, stock = 0):
        """Initializer for bike rental class"""
        self.__stock = stock

    @property
    def stock(self):
        """Display avialable bikes in the system"""
        print(f'\nWe have currently {self.__stock} bikes available\n')
        return self.__stock
    
    @stock.setter
    def stock(self, new_stock):
        return self.__stock + new_stock
    
    def hourRent(self, number_of_bikes):
        """Rent a bike on hourly basis"""
        if number_of_bikes <= 0: 
            print('You shouled rent almost 1 bike')
            return None
        elif number_of_bikes > self.__stock:
            print(f'At this moment we only have {self.__stock} available')
            return None
        else:
            starting_rent_datetime = dt.datetime.now()
            self.__stock -= number_of_bikes
            print(f'You´ve rented {number_of_bikes} for hourly basis at {starting_rent_datetime.hour}:{starting_rent_datetime.minute}:{starting_rent_datetime.second}')
            print('You will be charged $5 usd for each bike per hour')
            print('We hope you enjoy the service! \n')
            return starting_rent_datetime

    def dailyRent(self, number_of_bikes):
        """Rent a bike on daily basis"""
        if number_of_bikes <= 0: 
            print('You shouled rent almost 1 bike')
            return None
        elif number_of_bikes > self.__stock:
            print(f'At this moment we only have {self.__stock} available')
            return None
        else:
            starting_rent_datetime = dt.date.today()
            self.__stock -= number_of_bikes
            print(f'You´ve rented {number_of_bikes} on daily basis today {starting_rent_datetime}')
            print('You will be charged $20 usd for each bike daily')
            print('We hope you enjoy the service! \n')
            return starting_rent_datetime
        

    def weeklyRent(self, number_of_bikes):
        """Rent a bike on weekly basis"""
        if number_of_bikes <= 0: 
            print('You shouled rent almost 1 bike')
            return None
        elif number_of_bikes > self.__stock:
            print(f'At this moment we only have {self.__stock} available')
            return None
        else:
            starting_rent_datetime = dt.date.today()
            self.__stock -= number_of_bikes
            print(f'You´ve rented {number_of_bikes} on weekly basis today {starting_rent_datetime}')
            print('You will be charged $60 usd for each bike daily')
            print('We hope you enjoy the service! \n')
            return starting_rent_datetime
        

    def returnBike(self, request):
        """Accept a rented bike from a customer, increase number of available
bikes and return a bill"""
        rental_time, rental_basis, number_of_bikes= request
        bill = 0
        if rental_time and rental_basis and number_of_bikes:
            self.__stock += number_of_bikes
            now = dt.datetime.now() 
            rental_period = now - rental_time

            # hourly bill calculation
            if rental_basis == 2:
                bill = round(rental_period.seconds / 3600) * 5 * number_of_bikes
                print('Thanks for returning your bike, hope you enjoyed the service')
                print(f'The total bill is: ${bill}')
                return bill
            
            # daily bill calculatin 
            elif rental_basis == 3:
                bill = round(rental_period.days) * 20 * number_of_bikes
                print('Thanks for returning your bike, hope you enjoyed the service')
                print(f'The total bill is: ${bill}')
                return bill
            
            # weekly bill calculation
            elif rental_basis == 4: 
                bill = round(rental_period.days / 7) * 60 * number_of_bikes   
                print('Thanks for returning your bike, hope you enjoyed the service')
                print(f'The total bill is: ${bill}')
                return bill 

            # 30% off promo discount  
            if 3 <= number_of_bikes <= 6:
                print('\nYou have a discount of 30% off')
                bill = bill * .70   
                print('Thanks for returning your bike, hope you enjoyed the service')
                print(f'The total bill is: ${bill}')
                return bill
        else:
            print('We don´t have information about your bike rental in our system')
            return None


class Costumer:

    def __init__(self, bikes = 0, rental_basis = 0, rental_time = 0, bill = 0):
        """Initializer for costumer class"""
        self.bikes = bikes
        self.rental_basis = rental_basis
        self.rental_time = rental_time
        self.bill = bill 
        pass

    def requestBike(self):
        """Takes a request from the customer for the number of bikes"""
        bikes = input('How many bikes would you like to rent? ')
        try:
            bikes = int(bikes)
        except ValueError:
            print('Invalid input')
            return -1
        
        if bikes < 1:
            print('You have to rent at least one bike')
            return -1 
        else:
            self.bikes = bikes
            return self.bikes
            
    

    def returnBike(self):
        """Allows customers to return their bikes to the rental shop"""
        if self.rental_time and self.rental_basis and self.bikes:
            return self.rental_time, self.rental_basis, self.bikes
        else:
            return 0, 0, 0
        


