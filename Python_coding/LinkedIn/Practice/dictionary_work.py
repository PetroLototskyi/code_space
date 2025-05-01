def describe_items(food_items, color):
    # Your code goes here
    result=[]
    for category in food_items:
        for subcategory in food_items[category]:
            for item in food_items[category][subcategory]:
                item_info=food_items[category][subcategory][item]
                if color ==item_info.get("color"):
                    result.append(f'The {item} is {item_info.get("taste")}.')
                

    return result


food_items = {
    'fruits': {
        'tropical': {
            'mango': {
                'color': 'orange',
                'taste': 'sweet',
                'nutrients': ['vitamin C', 'vitamin A', 'fiber']
            },
            'pineapple': {
                'color': 'yellow',
                'taste': 'tangy',
                'nutrients': ['vitamin C', 'manganese', 'fiber']
            }
        },
        'temperate': {
            'apple': {
                'color': 'red',
                'taste': 'sweet',
                'nutrients': ['vitamin C', 'fiber', 'potassium']
            },
            'pear': {
                'color': 'green',
                'taste': 'juicy',
                'nutrients': ['vitamin C', 'fiber', 'copper']
            }
        }
    },
    'vegetables': {
        'leafy': {
            'spinach': {
                'color': 'green',
                'taste': 'earthy',
                'nutrients': ['vitamin K', 'vitamin A', 'iron']
            },
            'kale': {
                'color': 'green',
                'taste': 'bitter',
                'nutrients': ['vitamin K', 'vitamin A', 'calcium']
            }
        },
        'root': {
            'carrot': {
                'color': 'orange',
                'taste': 'sweet',
                'nutrients': ['vitamin A', 'vitamin K', 'fiber']
            },
            'beet': {
                'color': 'red',
                'taste': 'earthy',
                'nutrients': ['vitamin C', 'folate', 'iron']
            }
        }
    }
}
result = describe_items(food_items, 'red')

print(result)