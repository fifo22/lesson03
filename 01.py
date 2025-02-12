enter_simbol = str(input("Введите символы: "))

s_big=0
s_all=0
for i in enter_simbol:
      if(i.islower()):
            s_big+=1
      else:
            s_all+=1
print("Количество символов верхнего регистра:",s_big)
print("Количество всех остальных символов:",s_all)

#Результат:
#Введите символы: qweASD123$%^
#Количество символов верхнего регистра: 3
#Количество всех остальных символов: 9
#
#Process finished with exit code 0
