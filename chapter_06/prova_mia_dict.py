favourite_languages = {
    'gino': 'C++', 
    'alberto': 'Rust', 
    'sabrina': 'Haskell'
}

print(favourite_languages)

print(f'Il linguaggio favorito di Sabrina è: {favourite_languages["sabrina"].upper()}')

print(f"Una prova di get: {favourite_languages.get('Puzza', 'Nun ce un casso')}")

print(f"Seconda prova di get; {favourite_languages.get('alberto')}")

print(f"Terza prova di get: {favourite_languages.get('sorbona')}")

for key, value in favourite_languages.items():
    print(f'La key e: {key}')
    print(f'Il valore e: {value}\n')
  
for persone in favourite_languages.keys():
    print(f'la persona si chiama: {persone}\n') 
    
for linguaggi in favourite_languages.values():
    print(f'il linguaggio preferito e : {linguaggi}\n')
    
if 'Lino' not in favourite_languages.keys():
    print('Lini non e nella lista')
    
for name in sorted(favourite_languages.keys()):
    print(f'{name}')
    
for linguaggi in sorted(favourite_languages.values()):
    print(f'il linguaggio e: {linguaggi.upper()}\n')
    
provina = [2, 3, 2, 5, 5, 98, 6, 98, 2, 2, 2, 2]
zinco = set(provina)
print(zinco)
print(type(zinco))

prova_set = {'gino', 'alberto', 'gino', 'fantasma', 'grazia', 'paolo', 'grazia'}
print(prova_set)
print(type(prova_set))