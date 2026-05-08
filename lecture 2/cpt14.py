# Input marks in 5 subjects and check pass/fail (pass if all ≥ 40).

sub_1 = int(input("enter subject_1 mark :="))
sub_2 = int(input("enter subject_2 mark :="))
sub_3 = int(input("enter subject_3 mark :="))
sub_4 = int(input("enter subject_4 mark :="))
sub_5 = int(input("enter subject_5 mark :="))

if (sub_1 >= 40):
    print('pass' or 'fail')
elif (sub_2 >= 40):
    print('pass' or 'fail')
elif (sub_3 >= 40):
    print('pass' or 'fail')
elif (sub_4 >= 40):
    print('pass' or 'fail')
elif (sub_5 >= 40):
    print('pass' or 'fail')
else:
    print("fail")