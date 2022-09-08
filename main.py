truth = 'truth'
dare = 'dare'
i=0
q=0

while i<3:
    choise = input('Make your choise {} or {}: '.format(truth, dare))
    if choise == truth:
        print ('You choosed truth')
    if i==3:
        print('You choosed 3 Truths in a row, choose dare')
        continue
    i += 1
