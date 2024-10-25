import tkinter as tk
from tkinter import simpledialog, messagebox
import networkx as nx
import matplotlib.pyplot as plt

class GrafoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Proyecto Grafos")
        self.grafo = nx.DiGraph()  # Grafo dirigido
        self.vertices = set()  # Conjunto para almacenar los vértices
        self.aristas = []  # Lista para almacenar las aristas
        self.inicializar_interfaz()

#CREAMOS LA INTERFAZ GRAFICA:
    def inicializar_interfaz(self):
        self.label_instrucciones = tk.Label(self.root, text="Ingrese vértices y aristas en el formato A -> B")
        self.label_instrucciones.pack()

        # Ingreso de aristas y vertices
        self.input_vertice = tk.Entry(self.root)
        self.input_vertice.pack()

        self.boton_agregar_arista = tk.Button(self.root, text="Agregar Arista", command=self.agregar_arista)
        self.boton_agregar_arista.pack()

        # Tabla de Vértices
        self.label_vertices = tk.Label(self.root, text="Vértices ingresados:")
        self.label_vertices.pack()
        self.lista_vertices = tk.Listbox(self.root, height=6)
        self.lista_vertices.pack()

        # Tabla de Aristas
        self.label_aristas = tk.Label(self.root, text="Aristas ingresadas:")
        self.label_aristas.pack()
        self.lista_aristas = tk.Listbox(self.root, height=6)
        self.lista_aristas.pack()

        # Botones para mostrar las graficas
        self.boton_mostrar_grafo = tk.Button(self.root, text="Mostrar Grafo", command=self.mostrar_grafo)
        self.boton_mostrar_grafo.pack()

        self.boton_bfs = tk.Button(self.root, text="Aplicar Búsqueda en Anchura", command=self.aplicar_bfs)
        self.boton_bfs.pack()

        self.boton_dfs = tk.Button(self.root, text="Aplicar Búsqueda en Profundidad", command=self.aplicar_dfs)
        self.boton_dfs.pack()
        
        
#FUNCION PARA AGREGAR UNA ARISTA
    def agregar_arista(self):
        arista = self.input_vertice.get()
        if "->" not in arista:
            messagebox.showerror("Error", "Formato incorrecto. Use A -> B")
            return
        vertice_a, vertice_b = arista.split("->")
        vertice_a, vertice_b = vertice_a.strip(), vertice_b.strip()
        
        # Agregamos los vértices al conjunto
        self.vertices.add(vertice_a)
        self.vertices.add(vertice_b)
        
        # Agregamos la arista a la lista
        self.aristas.append((vertice_a, vertice_b))
        
        # Añadir al grafo
        self.grafo.add_edge(vertice_a, vertice_b)
        
        # Actualizar la lista de vértices y aristas en la tabla
        self.actualizar_tabla()

#ACTUALIZAMOS LA TABLA
    def actualizar_tabla(self):
        # Limpiar las listas
        self.lista_vertices.delete(0, tk.END)
        self.lista_aristas.delete(0, tk.END)

        # Agregar vértices a la tabla
        for vertice in self.vertices:
            self.lista_vertices.insert(tk.END, vertice)
        
        # Agregar aristas a la tabla
        for arista in self.aristas:
            self.lista_aristas.insert(tk.END, f"{arista[0]} -> {arista[1]}")

#FUNCION PARA AGREGAR UN GRAFO
    def mostrar_grafo(self):
        plt.figure()
        nx.draw(self.grafo, with_labels=True, node_color="lightblue", font_weight="bold")
        plt.show()

#FUNCION PARA VERTICE DE ANCHURA
    def aplicar_bfs(self):
        vertice_inicial = simpledialog.askstring("BFS", "Ingrese el vértice inicial:")
        if vertice_inicial not in self.grafo.nodes:
            messagebox.showerror("Error", "El vértice no existe en el grafo")
            return
        bfs_edges = list(nx.bfs_edges(self.grafo, source=vertice_inicial))
        bfs_grafo = nx.DiGraph(bfs_edges)
        self.mostrar_grafo_modificado(bfs_grafo, "Búsqueda en Anchura")

#FUNCION VERTICE A LO LARGO
    def aplicar_dfs(self):
        vertice_inicial = simpledialog.askstring("DFS", "Ingrese el vértice inicial:")
        if vertice_inicial not in self.grafo.nodes:
            messagebox.showerror("Error", "El vértice no existe en el grafo")
            return
        dfs_edges = list(nx.dfs_edges(self.grafo, source=vertice_inicial))
        dfs_grafo = nx.DiGraph(dfs_edges)
        self.mostrar_grafo_modificado(dfs_grafo, "Búsqueda en Profundidad")

#MOSTRAMOS EL GRAFO MODIFICADO
    def mostrar_grafo_modificado(self, grafo_modificado, titulo):
        plt.figure()
        nx.draw(grafo_modificado, with_labels=True, node_color="lightgreen", font_weight="bold")
        plt.title(titulo)
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = GrafoApp(root)
    root.mainloop()