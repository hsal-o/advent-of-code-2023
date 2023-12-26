import time

# Code adapted from Code Unveiled's explaination: https://www.youtube.com/watch?v=tvyvJ0CqnXo&ab_channel=CodeUnveiled

class Rule():
    def __init__(self, part, operator, rating, destination):
        self.part = part
        self.operator = operator
        self.rating = rating
        self.destination = destination

    def check(self, part_rating):
        if(self.operator == '>'):
            return part_rating > self.rating
        elif(self.operator == '<'):
            return part_rating < self.rating
        
    def __str__(self):
        return f"{self.part}{self.operator}{self.rating}:{self.destination}"
    
class Workflow():
    def __init__(self, name, rules, default):
        self.rules = rules
        self.name = name
        self.default = default

    def __str__(self):
        rules = ""
        for i, rule in enumerate(self.rules):
            rules += str(rule)
            if(i < len(self.rules)-1):
                rules += ","

        return f"{self.name}{{{rules},{self.default}}}"
    
def process_workflows(raw_workflows):
    # Build workflows
    workflows = {}
    for raw_workflow in raw_workflows:
        data = raw_workflow.replace("}", "").split("{")
        name = data[0] # Grab workflow name from data
        raw_rules = data[1].split(",") # Split up raw rule data
        default = raw_rules.pop() # Grab default rule

        rules = []
        # Build rules from raw rules data
        for raw_rule in raw_rules:
            part = raw_rule[0]
            operator = raw_rule[1]
            x = raw_rule[2:].split(":")
            rating = int(x[0])
            destination = x[1]

            new_rule = Rule(part, operator, rating, destination)
            rules.append(new_rule)

        new_workflow = Workflow(name, rules, default)
        # print(new_workflow)
        workflows[name] = new_workflow

    return workflows

def process_ratings(raw_ratings):
    ratings = []
    for raw_rating in raw_ratings:
        raw_rating = raw_rating[1:-1].split(",")

        new_rating = {}
        for pair in raw_rating:
            # pair in form of "<PART>=<VALUE>"
            part, value = pair.split("=")
            new_rating[part] = int(value)

        ratings.append(new_rating)

    return ratings

def process_rating(rating):
    global workflows

    curr_workflow = workflows["in"]

    # keep_going = True
    while(curr_workflow != "A" and curr_workflow != "R"):
        for rule in curr_workflow.rules:

            if(rule.check(rating[rule.part])):
                curr_workflow = workflows[rule.destination]
                break
        else:
            curr_workflow = workflows[curr_workflow.default]


    if(curr_workflow == 'A'):
        return sum(rating.values())
    else:
        return 0

def get_total_combinations(workflows):
    all_ratings = []
    rating = {}
    rating["x"] = (1, 4000)
    rating["m"] = (1, 4000)
    rating["a"] = (1, 4000)
    rating["s"] = (1, 4000)

    nodes = [("in", rating)]

    while(len(nodes) > 0):
        workflow_name, rating = nodes.pop()

        # Go over every rule in workflow
        for rule in workflows[workflow_name].rules:
            condition_rating = rating.copy()

            # Rating intervals are split accordingly
            if(rule.operator == '<'):
                # Condition part will cover part's start range to rule's rating range,
                # Part will cover rule's rating range to part's end range
                condition_rating[rule.part] = (condition_rating[rule.part][0], rule.rating - 1)
                rating[rule.part] = (rule.rating, rating[rule.part][1])
            elif(rule.operator == '>'):
                # Condition part will cover rule's rating range to part's end range
                # Part will cover part's start range to rule's rating range,
                condition_rating[rule.part] = (rule.rating + 1, condition_rating[rule.part][1])
                rating[rule.part] = (rating[rule.part][0], rule.rating)

            if(rule.destination in ["A", "R"]):
                if(rule.destination == "A"):
                    all_ratings.append(condition_rating.copy())
            else:
                # Branch out by fulfilling the condition
                nodes.append((rule.destination, condition_rating.copy()))

        # Consider Workflow's default rule
        if(workflows[workflow_name].default in ["A", "R"]):
            if(workflows[workflow_name].default == "A"):
                all_ratings.append(rating.copy())
        else:
            nodes.append((workflows[workflow_name].default, rating.copy()))

    total_combinations = 0
    for rating in all_ratings:
        combinations = 1
        for value in rating.values():
            combinations *= value[1] - value[0] + 1
        total_combinations += combinations

    return total_combinations

def main():
    global workflows
    start_time = time.time()

    raw_workflows, *raw_ratings = open("input.txt").read().split("\n\n")
    raw_workflows = raw_workflows.split()

    workflows = process_workflows(raw_workflows)
    workflows["A"] = "A"
    workflows["R"] = "R"

    total_combinations = get_total_combinations(workflows)

    print(f"total_combinations: {total_combinations}")
    
    # Calculate the elapsed time
    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.3f} seconds")

if __name__ == "__main__":
    workflows = {}
    main()
