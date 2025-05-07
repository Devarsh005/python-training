# import problem_a
# problem_a.show("this is the problem b and now i imported problem a")

def display(text):
    print(text)

def call_problem_a():
    import problem_a
    problem_a.show("this is the problem b and i call a show function of problem a")
