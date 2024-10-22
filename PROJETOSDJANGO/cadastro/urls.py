from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('segundo', views.segundo,
                name='segundo'),

    #Página
    path('pagina', views.pagina, 
                name='pagina'),

    #Mensagem
    path('mensagem', views.mensagem,
                name='mensagem'),
    path('mensagem2', views.mensagem2, name='mensagem2'),

    #Cursos
    path('listarcursos', views.listarcursos,
                name='listarcursos'),

    path('alterarcurso/<int:codigo>',
                views.alterarcurso,
                name='alterarcurso'),

    path('incluircurso', views.incluircursos,
                name='incluircurso'),

    path('excluircurso/<int:codigo>', views.excluircurso,
                name='excluircurso'),

    #Alunos
    path('listaralunos', views.listaralunos,
                name='listaralunos'),    

    path('incluiraluno', views.incluiraluno,
                name='incluiraluno'),

    path('alteraraluno/<int:codigo>',
                views.alteraraluno,
                name='alteraraluno'),

    path('excluiraluno/<int:codigo>', views.excluiraluno,
                name='excluiraluno'),

    #Professores
    path('listarprofessores', views.listarprofessores,
                name='listarprofessores'),

    path('incluirprofessores', views.incluirprofessores,
                name='incluirprofessores'),

    path('alterarprofessores/<int:codigo>',
                views.alterarprofessor,
                name='alterarprofessores'),

    #Turmas
    path('listarturmas', views.listarturmas,
                name='listarturmas'),

    path('incluirturma', views.incluirturma,
                 name='incluirturma'),

    path('alterarturma/<int:codigo>', views.alterarturma, 
                name='alterarturma'),
    

    path('exluirturma/<int:codigo>', views.excluirturma,
                name='excluirturma')
]   
