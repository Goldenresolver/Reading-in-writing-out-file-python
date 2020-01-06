#Jason Polanco
#12/26/19
# A program that display the user's bank statement information and calculates
# account balances.

#declare and intialize variables
uFname= ""
uLname=""
uAge=0
infile= open("January1.txt","r")

# define main
def main():
    #Welcome user to program
    print("\nWelcome to  Broward College National Bank!")
    

#prompt user for name
    uFname= input("\nPlease enter your first name:")
    
    uLname= input("\nPlease enter your last name:")
    #prompt user for age
    uAge= int(input("\nPlease enter your age: "))

#convert user's name where it consisters of the first letter of the first name
#the first 5 digits of the last name, and the user's age( all letters must be lower case
    nFnam= uFname[0:1]
    nLnam= uLname[0:5]

    userName= nFnam+nLnam+str(uAge).lower()
    print(userName)
#convert the account number to following format XXX-XX-XX
    
#calculate the total of the deposits, the total of the withdrawals
# ending balance in the account

# read in from text file
    line1=infile.readline()
    line2=infile.readline()

    line3=infile.readline()
    line4=infile.readline()

 
# close the read in file
    infile.close()
   # create a variable for the first line
    accNum=(line1)
   # slice the first line to create the xxx-xx-xxx format
    newaccNum= accNum[0:3]
    newaccNum2=accNum[3:5]
    newaccNum3=accNum[5:]

    #convert the second line to a float in order perform math
    beginBal= float(line2)
    # split the 3 line from the read in file, because it contains ","
    line3List= line3.split(",")

    #convert line 3 into a list and create a variable that contains the lenght of the list
    line3AList= len(line3List)

    #split the 4th line from the read in file, because it contains ","

    line4List= line4.split(",")

   #convert line 4into a list and create a variable that contains the lenght of the list
    line4AList= len(line4List)

    
    # create a for loop iterate the values and add them up.
    for i in range(line3AList):
        w= 0
        w += float(line3List[i])
        print(w)


    for i in range(line4AList):
         d=0
         d+= float(line4List[i])



    # After values have been summed up through the loops, create a final balance
    # for the bank statement
    eBalance= beginBal + d - w
    finaleBalance = round(eBalance,2)
    
    
    # display final balance
    print(eBalance)

    # Create file to write to
    outfile = open("March.txt","w")

    
    # Write out to file display info
    outfile.write("Broward College National Bank".center(80))

    outfile.write("\n\n\t\t\tMarch Bank Statment".center(80))

    outfile.write("\n\n\t\tName\t\t\tUserName\t\tAccountNumber")
    outfile.write("\n\n\t\t------------------------------------------------------------")
    outfile.write("\n\n\t\t"+uFname+uLname+"\t\t"+userName+"\t\t"+str(newaccNum)+"-"+newaccNum2+"-"+newaccNum3)

    outfile.write("\n\n\t\tBeginning Balance:"+"$"+str(beginBal))

    # Display withdrawals, deposits, balance, by writing out. 
    outfile.write("\n\n\t\tTotal Withdrawals:"+"$"+str(w))
    outfile.write("\n\n\t\tTotal Deposits:"+"$"+str(d))
    outfile.write("\n\n\t\tEnding Balance:"+"$"+str(eBalance))
    
    # Close out the write file once finished. 
    outfile.close
    

main()

