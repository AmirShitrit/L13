import csv

import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from mlxtend.frequent_patterns import apriori, association_rules

file_path = "grocery_dataset.txt"

def find_rules(num_of_antecedents, num_of_consequents):
    grocery_items = set()
    with open(file_path) as f:
        reader = csv.reader(f, delimiter=",")
        for i, line in enumerate(reader):
            grocery_items.update(line)

    transactions = list()
    with open(file_path) as f:
        reader = csv.reader(f, delimiter=",")
        for i, line in enumerate(reader):
            row_val = {item: False for item in grocery_items}
            row_val.update({item: True for item in line})
            transactions.append(row_val)
    grocery = pd.DataFrame(transactions)

    # frequent_itemsets = apriori(grocery, min_support=0.047, use_colnames=True)
    frequent_itemsets = apriori(grocery, min_support=0.007, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.2)
    filtered_rules = rules[(rules["antecedents"].apply(len) == num_of_antecedents) & (rules["consequents"].apply(len) == num_of_consequents)]
    filtered_rules = filtered_rules.sort_values(by=["certainty"], ascending=[False])

    print(filtered_rules[["antecedents", "consequents"]].head(20))

    # Plot associations
    G = nx.DiGraph()

    for _, row in filtered_rules.iterrows():
        for antecedent in row['antecedents']:
            for consequent in row['consequents']:
                G.add_edge(antecedent, consequent, weight=row['lift'])

    plt.figure(figsize=(10,8))
    pos = nx.spring_layout(G, k=1)
    nx.draw(G, pos, with_labels=True, node_size=1500, node_color='skyblue', font_size=12, arrowsize=20)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={k: f"{v:.2f}" for k,v in labels.items()})
    plt.title('Association Rules Network')
    plt.savefig('association_rules_network.png', dpi=300, bbox_inches='tight')
    plt.close()
