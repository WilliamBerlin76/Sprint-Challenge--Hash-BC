#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length 

    for i in range(len(tickets)):
        # print(tickets[i].source, tickets[i].destination)
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
        if tickets[i].source == "NONE":
            
            route[0] = tickets[i].destination
        elif tickets[i].destination == "NONE":
            route[-1] = tickets[i].source

    for i in range(len(route)):
        if route[i] is not route[0] or route[i] is not route[-1]:
            route[i] = hash_table_retrieve(hashtable, route[i - 1])
    
    return route[1:]
