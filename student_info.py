"""Simple program to display student information.

This script defines a `Student` data class with fields for name, batch,
course, and learning goal. The `main` function creates an instance with
sample data and prints the details in a readable format.
"""

from dataclasses import dataclass

@dataclass
class Student:
    """Data class representing a student's basic information."""
    name: str
    batch: str
    course: str
    learning_goal: str


def main() -> None:
    """Create a sample student and print its information."""
    # Sample data – you can modify these values as needed.
    student = Student(
        name="Shaikh Ashfaque",
        batch="2026",
        course="Forward Deployed Engineer",
        learning_goal="Master machine learning algorithms",
    )

    # Print the information in a structured way.
    print("Student Information:")
    print(f"Name          : {student.name}")
    print(f"Batch         : {student.batch}")
    print(f"Course        : {student.course}")
    print(f"Learning Goal : {student.learning_goal}")


if __name__ == "__main__":
    main()
