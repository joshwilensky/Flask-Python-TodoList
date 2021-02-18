class Tasks():

    count = 1

    def __init__(self, tasks, date):
        self.tasks = tasks
        self.date = date
        self.id = Tasks.count
        Tasks.count += 1
