def compare_subjects_within_student(subj1_all_students, subj2_all_students):
    for i in subj1_all_students:
        if i not in subj2_all_students or type(subj1_all_students[i]) is str:
            continue
        sub1list = subj1_all_students[i]
        if sub1list[0] > sub1list[1]:
            sub1max = sub1list[0]
        else:
            sub1max = sub1list[1]

        sub2list = subj2_all_students[i]
        if sub2list[0] > sub2list[1]:
            sub2max = sub2list[0]
        else:
            sub2max = sub2list[1]
        if sub1max > sub2max:
            print(i +' - ' + subj1_all_students['subject'])
        elif sub1max < sub2max:
            print(i +' - '+ subj2_all_students['subject'])
        else:
            print(i +' - Same grade')
        

            
subject1 = {'subject' : 'Biology',
       'Nofar': [80, 100], 
       'Yizhar': [90, 90],
       'Nadav': [70, 95],
       'Niv':[94, 83],
       'Eva':[95,96]}

subject2 = {'subject' : 'History',
        'Nofar': [90, 85],
        'Yizhar':[70,90], 
        'Nadav': [67, 85],
        'Niv':[80, 100],
        'Roni':[60,99]}                                   

compare_subjects_within_student(subject1, subject2)
