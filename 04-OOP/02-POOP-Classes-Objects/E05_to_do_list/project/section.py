from project.task import Task


class Section:

    def __init__(self, name: str) -> None:
        self.name = name
        self.tasks: list = []

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str) -> str:
        if task_name not in self.tasks:
            return f"Could not find task with the name {task_name}"
        idx = self.tasks.index(task_name)
        self.tasks[idx].completed = True
        return f"Completed task {task_name}"

        # t: Task = next((t for t in self.tasks if t.name == task_name), None)
        # if t:
        #     t.completed = True
        #     return f"Completed task {task_name}"
        # return f"Could not find task with the name {task_name}"

    def clean_section(self) -> str:
        count = 0
        for t in self.tasks:
            if t.completed:
                self.tasks.remove(t)
                count += 1
        return f"Cleared {count} tasks."

        # current_tasks_len = len(section.tasks)
        # self.tasks = [t for t in self.tasks if not t.completed]
        # return f"Cleared {current_tasks_len - len(self.tasks)} tasks."

    def view_section(self) -> str:
        task_details = '\n'.join(t.details() for t in self.tasks)
        return f"Section {self.name}:\n{task_details}"
