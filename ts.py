def solution_initialize():
    pass

def solution_move():
    pass

def tabu_rule_test():
    pass

def aspiration_rule_test():
    pass

def stopping_rule_test():
    pass

def main():
    solution_initialize()
    while stopping_rule_test():
        solution_candidate = solution_move()
        for solution in solution_candidate: