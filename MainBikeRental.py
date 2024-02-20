import PooBikeRental as br

bike_system = br.BikeRental(100)
costumer = br.Costumer()



while True:
    print("""
        ====== BIKE RENTAL APP ======
        1. Display avaiable bikes 
        2. Request a bike hourly - $5.00
        3. Request a bike daily - $20.00
        4. Request a bike weekly - $60.00
        5. Return a bike 
        6. Exit
        """)
    choice = input('Enter a choice: ')
    try: 
        choice = int(choice)
    except ValueError:
        print('Please enter an available option')
        continue
    
    # display stock
    if choice == 1:
        bike_system.stock

    # hourly rent
    elif choice == 2:
        costumer.rental_time = bike_system.hourRent(costumer.requestBike())
        costumer.rental_basis = 2
    
    # daily rent
    elif choice == 3:
        costumer.rental_time = bike_system.dailyRentRent(costumer.requestBike())
        costumer.rental_basis = 3
    
    # weekly rent
    elif choice == 4:
        costumer.rental_time = bike_system.weeklyRentRentRent(costumer.requestBike())
        costumer.rental_basis = 4

    # return  a bike 
    elif choice == 5: 
        bill = bike_system.returnBike(costumer.returnBike())
        costumer.bill = bill
        costumer.rental_time, costumer.rental_basis, costumer.bikes = 0, 0, 0
    
    elif choice == 6:
        break

    else:
        print('Invalidad option')









