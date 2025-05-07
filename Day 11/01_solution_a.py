print("this is the solution_a file")

# method of a 
def display(text):
    print(text)

# now i need to call function of problem_b file
def call_problem_b():
    import problem_b
    problem_b.display("this is the problem b display function")
    # problem_b.call_problem_a()
# __name__ = 'solution_a'
if __name__ == '__main__':
    call_problem_b()
# otherwise directly call that like ->  call_problem_b()

