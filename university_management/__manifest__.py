{
    'name' : 'University Management',
    'application' : True,
    'depends': ['base', 'mail'],
    'data' : [

        'security/ir.model.access.csv',

        'wizard/university_student_result_wizard_views.xml',
        'views/university_teacher_views.xml',
        'views/university_student_views.xml',
        'views/university_student_badge_views.xml',
        'views/university_student_result_views.xml',


    ]

}