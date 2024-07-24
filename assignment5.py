class multiplefunctions():
    def subfields():
        print("Sub-fields in AI are:")
        list=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for temp in list:
             print(temp)
    def oddeven():
        num=int(input("Enter the number:"))
        if(num%2==0):
            print(num,"is Even Number")
            msg="Even Number"
        else:
            print(num,"is Odd Number")
            msg="Odd Number"
        return msg
    
    def percentage():
        sub1=int(input("Subject1="))
        sub2=int(input("subject2="))
        sub3=int(input("Subject3="))
        sub4=int(input("Subject4="))
        sub5=int(input("Subject5="))
        total=sub1+sub2+sub3+sub4+sub5
        print("Total:",total)
        percent=(total/5)
        print("Percentage:",percent)
    
    def triangle():
        ht=int(input("Height="))
        bth=int(input("Breadth="))
        area=(ht*bth)/2
        print("Area formula=(height*breadth)/2")
        print("Area of triangle=",area)
        ht1=int(input("Height1="))
        ht2=int(input("Height2="))
        bth1=int(input("Breadth1="))
        perimeter=ht1+ht2+bth1
        print("Perimeter formula=Height1+Height2+Breadth1")
        print("perimeter of triangle=",perimeter)
    def eligiblity():
        gender=input("Your Gender=")
        age=int(input("Your Age="))
        if(gender=="male" and age>=21) or (gender=="female" and age>=18):
            print("Eligible")
            msg="Eligible"
        else:
            print("Not Eligible")
            msg="Not Eligible"
        return msg
    
        
    
