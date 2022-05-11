lloyd = { #dicionario com nomes e notas dos alunos
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = { #dicionario com nomes e notas dos alunos
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = { #dicionario com nomes e notas dos alunos
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

def average(numbers):#função calcula a media
  total = sum(numbers)
  total = float(total)
  return total/len(numbers)

def get_average(student):#função que faz a media peso porcentagem
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  return 0.1 * homework + 0.3 * quizzes + 0.6 * tests

def get_letter_grade(score):#função tranforma media em letra
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"

def get_class_average(class_list):#função calcula a media da turma
  results = []
  for student in class_list:
    student_avg = get_average(student)
    results.append(student_avg)
  return average(results)

students = [lloyd, alice, tyler] #lista de estudantes

avg = get_class_average(students)#chamando a função q calcula a media da
                                 #turma e jogando na variavel ""avg
print(avg)#imprimindo media
print(get_letter_grade(avg))#imprimindo media com letra.