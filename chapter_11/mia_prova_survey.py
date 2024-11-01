from survey import AnonymousSurvey
''' Fai una domanda e prepare il sondaggio'''
domanda = "Qual' è la tua lingua madre?"
lista_di_sondaggio = AnonymousSurvey(domanda)

lista_di_sondaggio.show_question()
print("Digita 'q' to quit in qualsiasi momento.n")
while True:
    risposta = input('Linguaggio: ')
    if risposta == 'q':
        break
    lista_di_sondaggio.store_response(risposta)
    
print('Grazie a tutti per il sondaggio')

lista_di_sondaggio.show_results()
