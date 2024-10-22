from django.shortcuts import redirect, render
from django.http import HttpResponse

from cadastro.forms import AlunoForm, CursoForm, ProfessorForm, TurmaForm
from .models import Aluno, Curso, Professor, Turma

from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'inicio.html')

def segundo(request):
    return HttpResponse("<h1>Segunda</h1>")

def pagina(request):
    return render(request, 'pagina.html')

def mensagem(request):
    return render(request, 'inicio.html')

def mensagem2(request):
    return render(request, 'pagina2.html')

def listarcursos(request):
    cursos = Curso.objects.order_by('nome')
    return render(request, 'listarcursos.html', 
                  {'cursos': cursos})

def incluircursos(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.error(request,
                "Inclusão feita com sucesso!")
            return redirect('listarcursos')
    form = CursoForm()
    return render(request,
                  'form_curso.html',
                  {'formulario':form})

def alterarcurso(request, codigo):
    c = Curso.objects.get(id=codigo)

    if request.method == "POST":
        form = CursoForm(request.POST, instance = c)
        if form.is_valid():
            form.save()
            messages.error(request,
                "Alteração feita com sucesso!")
            return redirect('listarcursos')
    form = CursoForm(instance=c)
    return render(request, 'form_curso.html',
                  {'formulario': form})

def excluircurso(request, codigo):
    c = Curso.objects.get(id=codigo)
    try:
        c.delete()
    except: 
        messages.error(request,
                "Não é possível excluir.")
    return redirect('listarcursos')

#Alunos
def listaralunos(request):
    alunos = Aluno.objects.order_by('nome')
    return render(request, 'listaralunos.html',
                  {'alunos': alunos})


def incluiraluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.error(request,
                "Inclusão feita com sucesso!")
            return redirect('listaralunos')
    form = AlunoForm()
    return render(request,
                      'form_aluno.html',
                      {'formulario':form})

def alteraraluno(request, codigo):
    c = Aluno.objects.get(id=codigo)

    if request.method == "POST":
        form = AlunoForm(request.POST, instance = c)
        if form.is_valid():
            form.save()
            messages.error(request,
                "Alteração feita com sucesso!")
            return redirect('listaralunos')
    form = AlunoForm(instance=c)
    return render(request, 'form_aluno.html',
                  {'formulario': form})

def excluiraluno(request, codigo):
    c = Aluno.objects.get(id=codigo)
    c.delete()
    return redirect('listaralunos')

#Professores
def listarprofessores(request):
    professores = Professor.objects.order_by('nome')
    return render(request, 'listarprofessores.html',
                  {'professores': professores})

def incluirprofessores(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.error(request,
                "Inclusão feita com sucesso!")
            return redirect('listarprofessores')
    form = ProfessorForm()
    return render(request,
                      'form_professor.html',
                      {'formulario':form})

def alterarprofessor(request, codigo):
    c = Professor.objects.get(id=codigo)

    if request.method == "POST":
        form = ProfessorForm(request.POST, instance = c)
        if form.is_valid():
            form.save()
            messages.error(request,
                "Alteração feita com sucesso!")
            return redirect('listarprofessores')
    form = ProfessorForm(instance=c)
    return render(request, 'form_professor.html',
                  {'formulario': form})

#Turmas
def listarturmas(request):
    turmas = Turma.objects.order_by('dataInicio')
    return render(request, 'listarturmas.html',
                  {'turmas': turmas})

def incluirturma(request):
    if request.method == 'POST':
        form = TurmaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.error(request,
                "Inclusão feita com sucesso!")
            return redirect('listarturmas')
        
    form = TurmaForm()
    return render(request,
                      'form_turma.html',
                       {'formulario':form})

def alterarturma(request,codigo):
    t = Turma.objects.get(id=codigo)
    if request.method == 'POST':
        form = TurmaForm(request.POST, instance=t)
        if form.is_valid():
            form.save()
            messages.error(request,
                "Inclusão feita com sucesso!")
            return redirect('listarturmas')
        form = TurmaForm(instance=t)
        return render(request, 'form_turma.html', {'formulario': form})

def excluirturma(request, codigo):
    t = Turma.objects.get(id=codigo)
    t.delete()
    return redirect('listarturmas')

