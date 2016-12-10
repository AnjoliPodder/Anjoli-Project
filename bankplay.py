from bank.commercial import branch

bank1 = branch.Bank("HSBC")

b1 = branch.Branch(bank1, "25 Broadway", "BMCC Branch")
b2 = branch.Branch(bank1, "42 Street", "World Branch")
b3 = branch.Branch(bank1, "72 Street", "Family Branch")

donald = branch.Customer("Trump", "Donald")
john = branch.Customer("McCain", "John")

b1.visit(donald)
b1.visit(donald)
b2.visit(john)
b3.visit(donald)

print("This is the number of unique visitors at %s bank at %s: %s" % (b1.bank.name, b1.address, b1.uniqueVisitors()))

bank1.getBranchesVisited(donald)