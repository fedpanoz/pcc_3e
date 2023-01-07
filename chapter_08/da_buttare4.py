def send_messages(argo):
    while argo:
        current = argo.pop()
        print(current)
        sent_messages.append(current)



sent_messages = []
sms = ['How are you', 'Is it ok', 'you are gorgeous', 'It seems awful']

send_messages(sms[:])
print(sent_messages)
print(sms)