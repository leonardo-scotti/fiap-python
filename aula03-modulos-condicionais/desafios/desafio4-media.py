def media(num1, num2, num3, num4):
    notas = num1 + num2 + num3 + num4
    media_notas = notas / 4
    return round(media_notas, 2)

print("Digite as notas do aluno a seguir.")
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segundda nota: "))
nota3 = float(input("Terceira nota: "))
nota4 = float(input("Quarta nota: "))

media_notas = media(nota1, nota2, nota4, nota4)

if media_notas >= 7:
    print(f"Média: {media_notas}\nAPROVADO")
elif media_notas >= 5 and media_notas < 7:
    print(f"Média: {media_notas}\nEM RECUPERAÇÃO")
elif media_notas < 0:
    print("DIGITE NOTAS VÁLIDAS")
else:
    print(f"Média: {media_notas}\nREPROVADO")