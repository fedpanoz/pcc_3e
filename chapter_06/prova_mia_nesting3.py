aliens = []
for alien_number in range(16):
    new_alien = {'color':'green', 'points': 5, 'speed':'medium'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    alien['color'] = 'PINK'
    alien['points'] = 1698
    alien['speed'] = 'SPEED-OF-LIGHHHHTSSSS!!'
    
print(aliens)
print()