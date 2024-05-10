import pandas as pd
from scipy.sparse import csr_matrix
from graphviz import Digraph

class SparseMatrix:
    def __init__(self, data=None, row=None, col=None):
        self.data = data
        self.row = row
        self.col = col

    def load_from_csv(self, filename):
        df = pd.read_csv(filename)
        self.data = df.values.flatten()
        self.row, self.col = zip(*[(i, j) for i in range(df.shape[0]) for j in range(df.shape[1])])
    
    def manual_input(self):
        data = []
        row = []
        col = []
        print("Ingrese los elementos de la matriz uno por uno. Cuando haya terminado, ingrese 'fin' para finalizar.")
        while True:
            try:
                value = input("Ingrese un valor: ")
                if value.lower() == 'fin':
                    break
                row_idx = int(input("Ingrese el índice de fila: "))
                col_idx = int(input("Ingrese el índice de columna: "))
                data.append(float(value))
                row.append(row_idx)
                col.append(col_idx)
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un valor numérico para el índice de fila y columna.")
        self.data = data
        self.row = row
        self.col = col
    
    def visualize(self):
        graph = Digraph()
        for i in range(len(self.data)):
            graph.node(f"{self.row[i]},{self.col[i]}", label=str(self.data[i]))
        graph.render('sparse_matrix', format='png', view=True)

    def display(self):
        matrix = csr_matrix((self.data, (self.row, self.col)))
        print(matrix.toarray())

def main():
    matrix = SparseMatrix()
    print("Seleccione una opción:")
    print("1. Cargar desde archivo CSV.")
    print("2. Ingresar manualmente.")
    choice = input("Ingrese el número de la opción deseada: ")
    if choice == '1':
        filename = input("Ingrese el nombre del archivo CSV: ")
        matrix.load_from_csv(filename)
    elif choice == '2':
        matrix.manual_input()
    else:
        print("Opción no válida.")
        return

    print("\nDatos de la matriz:")
    matrix.display()

    visualize_option = input("\n¿Desea visualizar la matriz dispersa? (s/n): ")
    if visualize_option.lower() == 's':
        matrix.visualize()
        print("Se ha generado el archivo 'sparse_matrix.png' con la representación visual de la matriz dispersa.")

if __name__ == "__main__":
    main()
