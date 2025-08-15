import networkx as nx
import matplotlib.pyplot as plt

class ConnectionsManager:
    def __init__(self):
        self.graph = nx.Graph()
    
    def addUser(self, user):
        if user not in self.graph:
            self.graph.add_node(user)
            print(f"'{user}' added successfully.")
        
       
    def addConnection(self, user1, user2):
        if user1 in self.graph and user2 in self.graph:
            self.graph.add_edge(user1, user2)
            print(f"Connection established between '{user1}' and '{user2}'")
       
    def viewUsers(self):
        print(" Users in the network:")
        for user in self.graph.nodes:
            print(user)
    
    def viewConnections(self):
        print("The currecnt connections are :")
        for user1, user2 in self.graph.edges:
            print(f"{user1} and {user2}")
    
    def showgraph(self):

        plt.title("My graph")
        mypos=nx.spring_layout(self.graph)
        nx.draw(self.graph,mypos, with_labels=True, node_color='red', font_size=10)
        plt.show()
        
        


class SocialNetworkApp:
    def __init__(self):
        self.manager = ConnectionsManager()

    def display_menu(self):
        print("\nSocial Media Connections Manager")
        print("1. Add User")
        print("2. Add Connection")
        print("3. View All Users")
        print("4. View All Connections")
        print("5. Display Graph")
        print("6. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter option : ")
            if choice == '1':
                user = input("Enter username to add: ")
                self.manager.addUser(user)
            elif choice == '2':
                user1 = input("Enter the name of user 1: ")
                user2 = input("Enter the name of user 2: ")
                self.manager.addConnection(user1, user2)
            elif choice == '3':
                self.manager.viewUsers()
            elif choice == '4':
                self.manager.viewConnections()
            elif choice == '5':
                self.manager.showgraph()
            elif choice == '6':
                print("Exiting....")
                break
            else:
                print("Enter a number from 1-6")


if __name__ == "__main__":
    app = SocialNetworkApp()
    app.run()
