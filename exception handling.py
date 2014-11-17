__author__ = 'Ayla'
#1. Write a procedure that
#   i. Asks the user to input their social security number. The phrasing for the question should be passed in as a string.
#   ii. Checks to make sure the input has the correct format AAA-GG-SSSS using a try except. AAA is the area number, GG is
#   the group number, and SSSS is the serial number.
#   iii. returns the AAA, GG, and SSSS as a tuple if the user put in a valid SS number, otherwise it returns None.



#NOTES:
#A. Numbers with all zeros in any digit group (000-##-####, ###-00-####, ###-##-0000) are not allowed.
#B. Numbers with 666 or 900-999 (Individual Taxpayer Identification Number) in the first digit group.
#C. The number 078-05-1120 is invalid as it was used in an advertising campaign.
#D. There currently no area numbers in the 900's.

#
question= ''
def socialsecuritynumber(question):
    social = input(question)
    try:
        aaa,gg,ssss = social.split('-')
        if len(aaa) != 3 or len(gg) != 2 or len(ssss) != 4:
            print('Invalid social security number')
            return None
        if aaa == '000' or gg =='00' or ssss == '0000':
            print("Invalid social security number")
            return None
        if aaa =='666' or '900'>='999':
            print("Invalid social security number")
            return None
        if aaa =='078' or gg =='05' or ssss =='1120':
            print("Invalid social security number")
            return None

        aaa=int(aaa)
        gg=int(gg)
        ssss=int(ssss)

        return aaa, gg, ssss
    except ValueError:
        print("Enter a valid social security number")
        return None


#socialsecuritynumber("Please input social security number")

#2. Write a procedure SS that calls the procedure above until the user puts in a valid SS#.
#3. The string that asks the user to input their SS# should be hardcoded as a variable at the beginning of the program.
#This string should be passed to the above two procedures.

def SS(question):
    social = input(question)
    socialsecuritynumber(question)





SS(question)


#try
    #split('-')
    #int( )
    # if aaa <= 899
#except

#exception: split
# if test length of split
#exception: convert to three ints
# if test the ints







        #two = input('next three numbers ')
        #if len(two)== 2:

        #four = input('last four numbers ' )
         #   if len(four) == 4:








#2. Write a procedure SS that calls the procedure above until the user puts in a valid SS#.
#3. The string that asks the user to input their SS# should be hardcoded as a variable at the beginning of the program.
#This string should be passed to the above two procedures.

#def ss():

#3ab-22-3182
#len 3?
#1. split -> does it throw an exception?
        #i. does the split have 3 things in the list?
#are each of the three integers?
#aaa=int(aaa)