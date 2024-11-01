def create_task_list():
    """
    Creates task list using closure. Its create one list of tasks with two properties (description, is_complete) and some functions for manipulate it.

    :return: Dictionary with closure functions
    """

    tasks = []

    def add_task(description : str):
        """
        Add new uncompleted task
        :param description: the task text
        """
        if len(description.strip()) < 0:
            raise Exception("Task must contains one char at least.")

        tasks.append({"description" : description, "is_complete" : False})

    def get_uncompleted():
        """
        Select uncompleted tasks amd return it
        :return: list of descriptions in str
        """
        uncompleted = []
        for t in tasks:
            if not t["is_complete"]:
                uncompleted.append(t["description"])
        return uncompleted


    def complete_task(description):
        """
        Mark task as complete
        """
        for t in tasks:
            if t["description"] == description:
                t["is_complete"] = True

    def get_complete():
        """
        Select completed tasks amd return it
        :return: list of descriptions in str
        """
        completed = []
        for t in tasks:
            if t["is_complete"]:
                completed.append(t["description"])
        return completed

    def get_all_tasks():
        

    return {"add_task" : add_task, "get_uncompeted": get_uncompleted , "complete_task" : complete_task, "get_complete" : get_complete}

peter_todo = create_task_list()
peter_todo["add_task"]("Vynest smeti")
peter_todo["add_task"]("Uklidit si pokojicek")
peter_todo["add_task"]("Task1")
peter_todo["add_task"]("Task2")
peter_todo["add_task"]("Task3")
peter_todo["add_task"]("Task4")



print(peter_todo["get_uncompeted"]())

peter_todo["complete_task"]("Vynest smeti")
peter_todo["complete_task"]("Task1")
peter_todo["complete_task"]("Task6")
print(peter_todo["get_uncompeted"]())
print("---------------------------------")
print(peter_todo["get_complete"]())