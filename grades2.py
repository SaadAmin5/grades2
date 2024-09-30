def grading ():
    
    while True:

        try:

            score=input('Enter score between 0-100 or press enter to exit: ')

            if score=='':
                print('You exit')
                break


            if int(score) >=0 and int(score)<=100:

                if int(score)>80:
                    grade='A grade'
                    print(grade)

                elif int(score)>50:
                    grade='B grade'
                    print(grade)

                elif int(score)>30:
                    grade='Pass'
                    print(grade)
                else:
                    grade='Fail'
                    print(grade)
            else:
                print('Please enter score between 0 - 100')

        except ValueError:
            print('Please enter a number')


grading()