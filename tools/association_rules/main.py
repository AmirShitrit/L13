import sys

from tools.association_rules.find_rules import find_rules

num_of_antecedents = sys.argv[1]
num_of_consequents = sys.argv[2]

find_rules(num_of_antecedents, num_of_consequents)