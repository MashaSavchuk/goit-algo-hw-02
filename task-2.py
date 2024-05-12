# Завдання 2

# Необхідно розробити функцію, яка приймає рядок як вхідний параметр, додає всі його символи до 
# двосторонньої черги (deque з модуля collections в Python), а потім порівнює символи з обох кінців черги, 
# щоб визначити, чи є рядок паліндромом. Програма повинна правильно враховувати як рядки з парною, 
# так і з непарною кількістю символів, а також бути нечутливою до регістру та пробілів.

from collections import deque
def is_palindrome(s) -> bool:
    
    prep = ''.join([ch.lower() for ch in s if ch.isalpha()])
    # print(prep)

    deq = deque(prep)

    # deq = deque()
    # for ch in prep:
    #     deq.append(ch)
  
    # print(deq)

    while len(deq) > 1:
      if deq.pop() != deq.popleft():
          # Не поліндом
          return False
      # Якщо пройшли всі символи і не було різних то поліндром
      return True

print(is_palindrome("Pan ap"))  
print(is_palindrome("Ola  alo")) 
print(is_palindrome("qwerty")) 
