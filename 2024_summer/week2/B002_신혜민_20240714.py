class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

def getImportance(employees: List['Employee'], id: int) -> int:
    emp_map = {emp.id: emp for emp in employees}
    
    def dfs(emp_id):
        employee = emp_map[emp_id]
        return employee.importance + sum(dfs(sub_id) for sub_id in employee.subordinates)
    
    return dfs(id)
