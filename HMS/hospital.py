import DDL
import heap
import patient as p
class Hospital:
    id = int(1)
    # initialise a linked list for hospital 
    list1 = DDL.DDL() # database 
    heap1 = heap.MaxHeap()
    def registerPatient(self, name, age):
        ob = p.Patient(name, age, self.id)
        self.id = self.id+1
        # insert into linked list, call
        self.list1.enqueue(ob)
        self.heap1.insert(ob)
    
    def showPatients(self):
        # self.list1.display()
        self.heap1.showQueue()
    
    
    def showNext(self):
        name, id = self.heap1.getTop()
        print(name)
        # print("----")
        self.list1.dequeue(id)
    
    def showHeap(self):
        self.heap1.showHeap()
