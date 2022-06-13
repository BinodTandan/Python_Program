sub1 = int(input("Enter the marks of Science: "))
sub2 = int(input("Enter the marks of Math: "))
sub3 = int(input("Enter the marks of Computer: "))
total = (sub1+sub2+sub3)/3

# if(sub1>=33 and sub2>=33):
#     f1 = True
# else:
#     f1 = False
    

# if(f1== True and sub3>=33):
#     f2 = True
# else:
#     f2 = False


# if(f2 == True and total>=40):
#     print("pass")
# else:
#     print("fail")
if(sub1<33 or sub2<33 or sub3<33):
    print("You are failed in at least in one of the subject")
elif(total<40):
    print("You are failed due to total perecent less than 40")
else:
    print("Conguratulation! You passed the exam")