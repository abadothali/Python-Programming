# Take input marks from the user and chek pass or faild | if marks >= 40 pass else faild.
def result_check(marks):
    if marks >= 40:
        print("Pass")
    else:
        print("Faild")

marks = int(input("Enter Numbers: "))
result_check(marks)
