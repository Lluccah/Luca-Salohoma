# this for loop controls the number of lines
# range(1, 10) generates numbers from 1 to 9
for i in range(1, 10):

# if i is 5 or less, increase the number of stars
    if i <= 5:
        # "*" * i repeasts the '*' character i times
        print('*' * i)
# if i is greater than 5, decrease the number of stars
    else:
     # 10 - i gives the decreasing pattern from 4 to 1
     print('*' * (10 - i))

     