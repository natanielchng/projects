from N2G import drawio_diagram
import csv

# Initialize the Draw.io module
diagram = drawio_diagram()

# Helper funtion to process csv
def load_csv(filename):
    with open(filename, mode='r', encoding='utf-8-sig') as f:
        # list comprehension to strip whitespace from every value
        return [{k: v.strip() for k, v in row.items()} for row in csv.DictReader(f)]

# network_data = {
#     "nodes": load_csv('1-nodes.csv'),
#     "links": load_csv('1-links.csv')
# }

network_data = {
    "nodes": load_csv('2-nodes.csv'),
    "links": load_csv('2-links.csv')
}

# network_data = {
#     "nodes": load_csv('3-nodes.csv'),
#     "links": load_csv('3-links.csv')
# }


diagram.from_dict(network_data, diagram_name="Page-1")
diagram.layout(algo="fr")
diagram.dump_file(filename="Sample_graph_1.drawio", folder="./Output/")