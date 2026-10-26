# KBC GAME

questions = [
  ["Which language is mainly used for web page structure?", "Python", "HTML", "C++", "Java", "None", 2],
  ["Which language is used to style web pages?", "CSS", "C", "Java", "Python", "None", 1],
  ["Which language is known as the brain of a web page?", "JavaScript", "Python", "HTML", "C#", "None", 1],
  ["Which of these is a programming language?", "HTML", "CSS", "Python", "Photoshop", "None", 3],
  ["Which symbol is used for comments in Python?", "//", "#", "/* */", "<!-- -->", "None", 2],
  ["Which function is used to print output in Python?", "print()", "printf()", "cout<<", "System.out.println", "None", 1],
  ["Which data type is used to store True/False?", "int", "bool", "string", "float", "None", 2],
  ["Which operator is used for addition in Python?", "+", "*", "%", "/", "None", 1],
  ["Which loop repeats a block of code?", "while", "print", "input", "stop", "None", 1],
  ["Which keyword is used to define a function in Python?", "function", "def", "fun", "define", "None", 2],
  ["Which one is used to store multiple values?", "Variable", "List", "If", "Return", "None", 2],
  ["Which keyword is used for decision making?", "loop", "if", "define", "elif", "None", 2],
  ["What does IDE stand for?", "Integrated Development Environment", "Internet Drive Engine", "Internal Data Execution", "None", "None", 1],
  ["Which one is a Python library?", "React", "NumPy", "Laravel", "Flutter", "None", 2],
  ["Which symbol is used for multiplication?", "+", "-", "*", "/", "None", 3],
  ["What is the correct file extension for Python?", ".java", ".js", ".py", ".html", "None", 3],
  ["Which data type stores decimal values?", "int", "bool", "float", "char", "None", 3],
  ["Which function takes user input?", "input()", "print()", "read()", "scan()", "None", 1],
  ["Which loop always runs at least once?", "while", "do-while", "for", "None of these", "None", 2],
  ["Which of these is a backend language?", "HTML", "CSS", "Python", "Bootstrap", "None", 3],
  ["Which tag is used to display images in HTML?", "<p>", "<h1>", "<img>", "<div>", "None", 3],
  ["Which operator gives remainder?", "+", "*", "%", "/", "None", 3],
  ["Which company created Java?", "Apple", "Google", "Sun Microsystems", "IBM", "None", 3],
  ["What is used to repeat code a fixed number of times?", "if", "for loop", "print", "stop", "None", 2],
  ["Which language is used for Android app development?", "Swift", "Kotlin", "PHP", "HTML", "None", 2],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000,
          640000, 1250000, 2500000, 5000000, 10000000, 20000000, 30000000,
          50000000, 75000000, 100000000, 150000000, 200000000, 300000000,
          500000000, 700000000]

money = 0

for i in range(len(questions)):
  
  question = questions[i]
  
  print("\n------------------------------------------------------")
  print(f" Question {i+1} for Rs. {levels[i]}")
  print("------------------------------------------------------")
  
  # Show question text
  print(f"👉 {question[0]}\n")
  
  # Show options
  print(f"a. {question[1]}          b. {question[2]}")
  print(f"c. {question[3]}          d. {question[4]}")

  reply = int(input("\nEnter your answer (1-4) or 0 to quit: "))

  if reply == 0:
    money = levels[i-1]
    break

  if reply == question[-1]:  # correct answer
    print(f"\n✔ Correct answer! You won Rs. {levels[i]}")
    
    if i == 4:
      money = 10000
    elif i == 9:
      money = 320000
    elif i == 14:
      money = 10000000

  else:
    print("\n❌ Wrong answer!")
    break

print(f"\n💰 Your take-home money is Rs. {money}")
