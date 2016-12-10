class Teller:
    def __init__(self, last_name, first_name, branch):
        self.last_name = last_name
        self.first_name = first_name
        self.branch = branch

    def greetCustomer(self, cust):
        print("Hello %s. Welcome to %s" % (cust.getName(), self.branch))

    def getName(self):
        return "%s %s" %(self.first_name, self.last_name)

class Customer:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name
        self.bank_visits = 0

    def getName(self):
        return "%s %s" %(self.first_name, self.last_name)

class Branch:
    def __init__(self, bank, address, name = ""):
        self.name = name
        self.address = address
        self.employees = []
        self.visitor_count = 0
        self.visitors = {}
        self.bank = bank
        bank.addBranch(self)

    def visit(self, cust):
        if not(cust is None):
            if cust in self.visitors:
                self.visitors[cust] += 1
            else:
                self.visitors[cust] = 1
    def uniqueVisitors(self):
        return len(self.visitors)

class Bank:
    def __init__(self, name):
        self.name = name
        self.branches = []

    def addBranch(self, branch):
        self.branches.append(branch)

    def numBranches(self):
        return len(self.branches)

    #given a customer name, give me a list of branches where this customer has visited at least once
    def getBranchesVisited(self, cust):
        result = []
        for branch in self.branches:
            if cust in branch.visitors:
                result.append(branch)
        return result