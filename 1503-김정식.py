#est_list = ['one','two','three']
#for i in test_list:
 #   print(i)

# marks1.py

#marks = [90,25,48,61,99]

#number = 0
#for mark in marks:
  #  number = number +1
   # if mark >= 60:
     #   print("%d번 학생은 합격입니다." % number)
  #  else:
      #  print("%d번 학생은 불합격입니다." % number)

# marks2.py 
#marks = [90, 25, 67, 45, 80]

#number = 0 
#for mark in marks: 
   # number = number +1 
  #  if mark < 60:
      #  continue 
  #  print("%d번 학생 축하합니다. 합격입니다. " % number)

   # a = range(10)
   # a
#range(0, 10)

#a = range(1, 11)
#a
#range(1, 11)

#add = 0 
#for i in range(1, 11): 
  #  add = add + i
#print(add)

#marks3.py
#mark = [90,25,67,45,80]
#for number in range(len(marks)):
   # if marks[number] < 60:
   #     continue
   # print("%d번 학생 축하합니다. 합격입니다." % (number+1))

#for i in range(2,10):        # 1번 for문
  #  for j in range(1, 10):
   #     print(j*i, end=" ")
    #print('')

#a = [1,2,3,4]
#result = []
#for num in a:
 #  result.append(num*3)
#print(result)

#a = [1,2,3,4]
#result = [num * 3 for num in a if num % 2 == 0]
#print(result)
#[6, 12]

#result = [x*y for x in range(2,10)
 #for y in range(1,10)]
#print(result)

# while 1:
#   a = int(input('마름모를 출력하려면 0 직삼각형을 출력할려면 1'))

#   def 마름모():
#     n = int(input())
#     c = n+1
#     for i in range(1,n+2):
#       print(" "*(n+1-i)+"*"*(i*2-1))
#     for i in range(1,n+1):
#       c = c -1
#       print(" "*(n+1-c)+"*"*(c*2-1))

#   def 직삼각형():
#     n = int(input())
#     c = n+1
#     for i in range(n+1):
#       c= c-1
#       print(" "*(i)+"*"*c)

#       if a == 0:
#         마름모()
#       elif a == 1:
#         직삼각형()
#         break