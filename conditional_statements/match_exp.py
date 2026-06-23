# mostly in different programming languages there is traditional switch-casse.

# Python doesn't provide that traditional switch case. but we can achieve that similar behaviour.
# In python 3.10 version and after that python will support that behaviour by using 'match'.

day=5

match day:
    case 1:
        print('Mon')
    case 2:
        print('Tue')
    case 3:
        print('Wed')
    case 4:
        print('Thu')
    case 5:
        print('Fri')
    case 6:
        print('Sat')
    case 7:
        print('Sun')


# the match expression is evaluated once.
# the value of expression is compared with value of each case.
