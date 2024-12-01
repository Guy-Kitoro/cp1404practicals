"""
CP1404/CP5632 Practical
Program to manage projects.
"""

from project import Project
from datetime import datetime


def main():
    """Main function to manage projects."""
    projects = load_projects("projects.txt")

    print("Welcome to Project Management!")
    menu = """
    - (L)oad projects  
    - (S)ave projects  
    - (D)isplay projects  
    - (F)ilter projects by date
    - (A)dd new project  
    - (U)pdate project  
    - (Q)uit
    """
    print(menu)

    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_date = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, filter_date)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        else:
            print("Invalid choice")
        print(menu)
        choice = input(">>> ").lower()

    save = input("Would you like to save your changes? (y/n): ").lower()
    if save == "y":
        save_projects("projects.txt", projects)
    print("Goodbye!")


def load_projects(filename):
    """Load projects from a text file."""
    projects = []
    try:
        with open(filename, "r") as file:
            file.readline()  # Skip the header
            for line in file:
                parts = line.strip().split("\t")
                name, start_date, priority, cost, completion = parts
                projects.append(Project(name, start_date, int(priority), float(cost), int(completion)))
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty project list.")
    return projects


def save_projects(filename, projects):
    """Save projects to a text file."""
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t"
                       f"{project.cost_estimate:.2f}\t{project.completion_percentage}\n")


def display_projects(projects):
    """Display incomplete and completed projects sorted by priority."""
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]

    print("Incomplete projects:")
    for project in sorted(incomplete):
        print(project)

    print("\nCompleted projects:")
    for project in sorted(complete):
        print(project)


def filter_projects_by_date(projects, filter_date):
    """Display projects that start after the given date."""
    filter_date = datetime.strptime(filter_date, "%d/%m/%Y").date()
    filtered_projects = [p for p in projects if datetime.strptime(p.start_date, "%d/%m/%Y").date() > filter_date]

    for project in sorted(filtered_projects, key=lambda p: datetime.strptime(p.start_date, "%d/%m/%Y")):
        print(project)


def add_new_project(projects):
    """Add a new project."""
    print("Let's add a new project!")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion_percentage = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def update_project(projects):
    """Update an existing project."""
    print("Choose a project to update:")
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_index = int(input("Project choice: "))

    project = projects[project_index]
    print(f"Updating {project}")
    completion = input("New completion percentage (leave blank to keep current): ")
    priority = input("New priority (leave blank to keep current): ")

    if completion:
        project.completion_percentage = int(completion)
    if priority:
        project.priority = int(priority)


if __name__ == "__main__":
    main()
