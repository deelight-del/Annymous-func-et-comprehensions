#Creating a system for a petrol and oil bunker for updating the prices of their product(petrol and disel)

old_price = {'petrol':91.09, 'disel': 87.23}

petrol_update = float(input('Enter the change in petrol price '))
disel_update = float(input('Enter the change in disel price: '))

def petrol_updater(petrol_update, old_price):
    return {item: value+petrol_update for item, value in old_price.items() if item == 'petrol'}

def disel_updater(disel_update, old_price):
    return {item: value+disel_update for item, value in old_price.items() if item == 'disel'}

def price_upadter(petrol_update, disel_update, old_price):
    return petrol_updater(petrol_update, old_price), disel_updater(disel_update, old_price)
#Note that the scope of the variable of the local function  variable is differernt from the gloabl scope, although arguements of the function share
#the same name with some variables.

petrol_price, disel_price = price_upadter(petrol_update, disel_update, old_price)

new_petrol_price = petrol_price['petrol']
new_disel_price = disel_price['disel']
print(f'\nprice of petrol is now {new_petrol_price}')
print(f'price of disel is now {new_disel_price}')