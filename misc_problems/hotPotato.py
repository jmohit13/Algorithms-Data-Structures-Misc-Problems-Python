# Hot Potato Simulation
import sys
sys.path.append('..')
from data_structures.queue import Queue


def hotPotato(nameList, num):
    """
    Return the name of the last person remaining after repetitive counting by num.
    
    In this game children line up in a circle and pass an item from neighbor to neighbor as fast as they can.
    At a certain point in the game, the action is stopped and the child who has the potato is removed from the circle.
    Play continues until only one child is left.
    
    INPUT
    ------
        namelist : Players name
        num : number of times item is passed
    
    RETURN
    ------
        player who is left after all iterations
    
    """
    
    q = Queue(); numCount = 0
    
    for i in range(len(nameList)):
        q.enqueue(nameList[i])
    
    while(q.size() > 1):
        for i in range(num):
            temp_removed_item = q.dequeue()
            q.enqueue(temp_removed_item)
        removed_item = q.dequeue()
        print("Players remaining : ",q.items)
        numCount += 1
    
    return q.items[0]

if __name__ == "__main__":
    print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
