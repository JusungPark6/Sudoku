import random
class SAT:

    def __init__(self, cnf_filename):
        self.var_to_index, self.clauses = self.read_cnf(cnf_filename)
        self.index_to_var = {index: var for var, index in self.var_to_index.items()}
        self.assignments = [random.choice([True, False]) for _ in
                            range(len(self.var_to_index) + 1)]  # +1 because we start from index 1

    def read_cnf(self, filename):
        var_to_index = {}
        clauses = []
        with open(filename, "r") as f:
            for line in f:
                clause = []
                for literal in line.strip().split():
                    if literal.startswith('-'):
                        var_name = literal[1:]
                    else:
                        var_name = literal
                    if var_name not in var_to_index:
                        var_to_index[var_name] = len(var_to_index) + 1
                    clause.append(var_to_index[var_name] if literal == var_name else -var_to_index[var_name])
                clauses.append(clause)
        return var_to_index, clauses

    def is_satisfied(self, clause):
        for lit in clause:
            if lit > 0 and self.assignments[lit]:
                return True
            if lit < 0 and not self.assignments[-lit]:
                return True
        return False

    def evaluate(self):
        return all(self.is_satisfied(clause) for clause in self.clauses)

    def score_variable(self, variable):
        original_value = self.assignments[variable]
        self.assignments[variable] = not original_value
        score = sum(self.is_satisfied(clause) for clause in self.clauses)
        self.assignments[variable] = original_value
        return score

    def gsat(self, max_flips=10000, h=0.5):
        for _ in range(max_flips):
            if self.evaluate():
                return True

            if random.random() > h:
                variable_to_flip = random.randint(1, len(self.var_to_index))
            else:
                scores = [(variable, self.score_variable(variable)) for variable in
                          range(1, len(self.var_to_index) + 1)]
                max_score = max(scores, key=lambda x: x[1])[1]
                best_variables = [variable for variable, score in scores if score == max_score]
                variable_to_flip = random.choice(best_variables)

            self.assignments[variable_to_flip] = not self.assignments[variable_to_flip]

        return False

    def write_solution(self, filename):
        with open(filename, "w") as f:
            for index, val in enumerate(self.assignments[1:], start=1):  # Start from index 1
                var_name = self.index_to_var[index]
                sign = "" if val else "-"
                f.write(f"{sign}{var_name}\n")
