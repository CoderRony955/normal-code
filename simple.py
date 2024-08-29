import sys
from Student_details import Student_details
import matplotlib.pyplot as plt

def main():
#check if the name was present in Student_detials or not using if else condtion
    name = input("Enter your name: ")
    if(name in Student_details):
        print(f"Hello {name}, here is your details now you can check you total percentage or total marks :>")
        print()
        print(Student_details[name])#<--------- show student details which entered by the user 
    else:
        print(f"Sorry {name} named student not found :<")#<---------------- if the student name was not found in Student_details dictionary then the code was end using "sys.exit() function"
        sys.exit()
        
#then take inputs from the user for each subjects marks
    maths = int(input("Enter your maths marks: "))
    science = int(input("Enter your science marks: "))
    english = int(input("Enter your english marks: "))
    hindi = int(input("Enter your hindi marks: "))
    social = int(input("Enter your social marks: "))
    total = maths+science+english+hindi+social
    percentage = total/5
    print(f"""
          You have entered: 
          maths: {maths}
          science: {science}
          english: {english}
          hindi: {hindi}
          social: {social}
          """)
    print() #<------------------ using empty print() statement for spacing in output
    print(f"Here is your total marks: {total}")
    print(f"Here is your total percentage: {percentage}")
    
    """now we use if condtion for "pass" or "fail" but we can make it complicate like if student score less than 33 in anyone subject only then the student will failed like student must be need to score 33 to pass
    """
    
    if(percentage >= 33 and maths >= 33 and science >= 33 and english >= 33 and hindi >= 33 and social >= 33):
        print(f"Congratualtions {name}, you passed this exam :)")
    else:
        print(f"Sorry {name}, you are failed try next year :(")
        
    #-------------------------------------------------------------    
    #calling graph_scoring function    
    #------------------------------------------------------------
    graph_scoring(maths, science, english, hindi, social)
        
def graph_scoring(maths, science, english, hindi, social):
    plt.stem(["maths", "science", "english", "hindi", "social"], [maths, science, english, hindi, social])
    plt.title("Scoring of all subjects")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.show()
    

        
if __name__ == "__main__":
    main()

