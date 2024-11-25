print("Skill circle library system")
def final_call():
    x=int(input('''Do you want to continue \n Yes-1 No-2\n Choose any number from 1 to 2::'''))
    if(x==2):
        print("Thanks for visiting skill circle")
    else:
        options()
def options():
    a=int(input(" Press Any number from 1 to 5::::"))   
    if(a==1):
        print('''101
              book name=Peacock
              author name=Saurav
              pages no:=456''')
        final_call()
    elif(a==2):
        print('''102
            book name=Cow
            author name=Ajit
            pages no:=264''')
        final_call()
    elif(a==3):
        print('''103
            book name=Zebra
            author name=Karan
            pages no:=300''')
        final_call()
    elif(a==4):
        print('''104
            book name=Lion
            author name=Sam
            pages no:=900''')
        final_call()
    elif(a==5):
        print('''105
            book name=Tiger
            author name=Tom
            pages no:=241''')
        final_call()
   
options()


    