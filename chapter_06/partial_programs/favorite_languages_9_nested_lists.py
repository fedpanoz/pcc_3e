favorite_languages = {
      'jen': ['python', 'rust'],
      'sarah': ['c'],
      'edward': ['rust', 'go'],
      'phil': ['python', 'haskell'],
      }

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"{name}'s favourite languages are:")
        for language in languages:
            print(f"{language}")
    else:
        print(f"{name}'s favourite language is:")
        for language in languages:
            print(f"{language}")
    print()