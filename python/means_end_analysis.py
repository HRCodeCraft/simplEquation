class MeansEndAnalysis:
    def __init__(self, initial_state, goal_state, operators):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.operators = operators

    def is_goal_reached(self, state):
        return state == self.goal_state

    def get_possible_operations(self, state):
        possible_operations = []
        for operator in self.operators:
            if operator['precondition'](state):
                possible_operations.append(operator)
        return possible_operations

    def apply_operator(self, state, operator):
        return operator['effect'](state)

    def means_end_analysis(self, current_state, path):
        if self.is_goal_reached(current_state):
            return path

        possible_operations = self.get_possible_operations(current_state)
        if not possible_operations:
            return None

        for operator in possible_operations:
            new_state = self.apply_operator(current_state, operator)
            new_path = path + [operator['name']]
            result = self.means_end_analysis(new_state, new_path)
            if result is not None:
                return result

        return None

def main():
    print("Define the problem:")

    # Initial state
    initial_state = input("Enter the initial state: ")

    # Goal state
    goal_state = input("Enter the goal state: ")

    # Operators
    operators = []
    num_operators = int(input("Enter the number of operators: "))

    for i in range(num_operators):
        name = input(f"Enter the name of operator {i + 1}: ")
        precondition = input(f"Enter the precondition of operator {i + 1} (Python function code that returns True or False): ")
        effect = input(f"Enter the effect of operator {i + 1} (Python function code that returns the new state): ")

        # Converting the string to actual Python function using exec and eval
        exec(f'precondition_fn = lambda state: {precondition}')
        exec(f'effect_fn = lambda state: {effect}')

        operators.append({
            'name': name,
            'precondition': eval('precondition_fn'),
            'effect': eval('effect_fn')
        })

    # Creating MEA object
    mea = MeansEndAnalysis(initial_state, goal_state, operators)

    # Finding the solution
    solution = mea.means_end_analysis(mea.initial_state, [])

    if solution:
        print("Solution found! Steps to reach the goal:")
        for step in solution:
            print(step)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
