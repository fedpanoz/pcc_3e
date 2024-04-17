favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'gino': 'haskell',
    'phil': 'python',
    'verbena': 'hla_assembly',
    }
friends = ['gino', 'verbena']

"""for y in favorite_languages.values():
    print(y)
print("\n")    
for y in favorite_languages.keys():
    print(y)

pippone = favorite_languages.get('pippone', 'No language found')
print(pippone)"""

for x, y in favorite_languages.items():
    print(f"{x.title()} favourite language is {y}")
    
print("\n")

for x in favorite_languages.keys():
    print(x)
print("\n")

for y in favorite_languages.values():
    print(y)

for x, y in favorite_languages.items():
    if x in friends:
        print(f"{x.title()} favourite language is {y}")
        
             
print(favorite_languages.keys())
print(favorite_languages.values())
print(type(favorite_languages.keys()))
print(type(favorite_languages.values()))
      