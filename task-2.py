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
