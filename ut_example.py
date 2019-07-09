'''
EXAMPLE
'''
try:
    X = 199
    Y = 0
    Z = X/Y
except ZeroDivisionError:
    print('ZeroDivisionError')
except:
    print('Other Error')
finally:
    print('All Done')
