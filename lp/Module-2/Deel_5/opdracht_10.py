# from  fruitmand import fruitmand
# def get_weight(weight):
#     return weight['weight']
# gewicht =sorted (fruitmand, key= get_weight, reverse = True)
# for fruit in gewicht:
#     print(f'{fruit['name']} : {fruit['weight']}')



from  fruitmand import fruitmand
def get_weight(weight):
    return weight['weight']
gewicht = sorted (fruitmand, key = get_weight, reverse = True)
for fruit in gewicht:
    print(f'{fruit["name"]} : {fruit["weight"]}')

from  fruitmand import fruitmand
gewicht =sorted (fruitmand,  key= lambda x: x['weight'], reverse = True) # heb meer uitleg nodig over de sintax van de lamda             

# lambda x: x['weight']


print("================================")
for fruit in gewicht:
    print(f'{fruit['name']} : {fruit['weight']}')
