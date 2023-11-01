import random


class SAT2:
    def __init__(self, filename):
        # Read the .cnf file and initialize the clauses
        self.clauses = self.read_clauses(filename)
        self.variables = self.initialize_variables(self.clauses)

    def read_clauses(self, filename):
        with open(filename, 'r') as f:
            clauses = [list(map(int, line.split())) for line in f.readlines()]
        return clauses

    def initialize_variables(self, clauses):
        vars = set()
        for clause in clauses:
            for var in clause:
                vars.add(abs(var))
        return {v: random.choice([True, False]) for v in vars}

    def walksat(self, max_flips=100000, p=0.3):
        for _ in range(max_flips):
            unsatisfied = [clause for clause in self.clauses if not self.is_clause_satisfied(clause)]

            if not unsatisfied:
                return True  # Satisfying assignment found

            if random.random() < p:
                # Choose an unsatisfied clause uniformly at random
                clause = random.choice(unsatisfied)
                var = random.choice(clause)  # Choose a variable from this clause
                self.variables[abs(var)] = not self.variables[abs(var)]  # Flip the variable
            else:
                # Score variables from a randomly chosen unsatisfied clause
                clause = random.choice(unsatisfied)
                scores = {}
                for var in clause:
                    scores[var] = self.get_score(var)
                # Choose the best variable to flip
                best_vars = [v for v, s in scores.items() if s == max(scores.values())]
                var_to_flip = random.choice(best_vars)
                self.variables[abs(var_to_flip)] = not self.variables[abs(var_to_flip)]

        return False  # No satisfying assignment found within max_flips

    def is_clause_satisfied(self, clause):
        return any([(v > 0 and self.variables[v]) or (v < 0 and not self.variables[-v]) for v in clause])

    def get_score(self, var):
        current_value = self.variables[abs(var)]
        self.variables[abs(var)] = not current_value
        score = sum([self.is_clause_satisfied(clause) for clause in self.clauses])
        self.variables[abs(var)] = current_value  # Revert the change
        return score

    def write_solution(self, filename):
        with open(filename, 'w') as f:
            for var, value in self.variables.items():
                if value:
                    f.write(str(var) + "\n")
                else:
                    f.write("-" + str(var) + "\n")