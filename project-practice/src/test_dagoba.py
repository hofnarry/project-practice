from dagoba import Graph

def main():
    g = Graph()

    # Добавляем вершины
    g.add_vertex('Alice', {'type': 'person', 'name': 'Alice'})
    g.add_vertex('Bob', {'type': 'person', 'name': 'Bob'})
    g.add_vertex('Charlie', {'type': 'person', 'name': 'Charlie'})

    # Добавляем двунаправленную связь между Alice и Bob
    g.add_edge('Alice', 'Bob', 'knows', reverse=True)

    # Однонаправленная связь между Bob и Charlie
    g.add_edge('Bob', 'Charlie', 'knows')

    # Проверка: кого знает Alice
    print("Who does Alice know?")
    print(g.v('Alice').out('knows').run())

    # Проверка: кого знает Bob
    print("Who does Bob know?")
    print(g.v('Bob').out('knows').run())

    # Проверка: кого знает Charlie
    print("Who does Charlie know?")
    print(g.v('Charlie').out('knows').run())  # → []

if __name__ == "__main__":
    main()
