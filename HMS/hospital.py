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
        print(self.heap1.showHeap())
    
    def showPatientsDDL(self):
        self.list1.display()
    
    
    def showNext(self):
        name, id = self.heap1.getTop()
        print("ID No.",id,name,"is the next patient for consultation")
        # print("----")
        self.heap1.showHeap()
        self.list1.dequeue(id)
    
    def showHeap(self):
        self.heap1.showHeap()
