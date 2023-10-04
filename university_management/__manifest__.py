{
    'name' : 'University Management',
    'application' : True,
    'depends': ['base', 'mail'],
    'data' : [

        'security/ir.model.access.csv',

        'views/university_teacher_views.xml',
        'views/university_student_views.xml',
        'views/university_student_badge_views.xml'

    ]

}