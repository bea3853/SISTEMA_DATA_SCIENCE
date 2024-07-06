import json

qA = int(input('quantidade de alunos: '))
nomes = [0] * qA
media = [0] * qA
alunos = {'alunos': []}

for i in range(qA):
    nomes[i] = input('nome do aluno: ')
    media[i] = float(input(' media aluno: '))

for j in range(qA):
    alunos['alunos'].append(
        {  'Nome': nomes[j],
            'Media': media[j]
        }
    )
with open('alunos.json', 'w') as arquivo:     
    json.dump(alunos, arquivo, indent=4)