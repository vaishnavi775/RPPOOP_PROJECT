import sqlite3


def insert_funding_brought(StudentName, funding_amount):
    c = sqlite3.connect('..\db\members.db')
    cursor = c.cursor()

    # Insert the funding amount into the "Funding_Brought" column of the specified project_id
    cursor.execute('''
        UPDATE members
        SET Funding_Brought = ?
        WHERE StudentName = ?
    ''', (funding_amount, StudentName))

    # Commit the changes and close the connection
    c.commit()
    c.close()

# Example usage:
insert_funding_brought("Gaurav Pande", 50000)  # Inserts funding_amount of 50000 into project with project_id 1

def delete_funding_brought(StudentName):
    conn = sqlite3.connect('members.db')
    cursor = conn.cursor()

    # Delete the data from the "Funding_Brought" column for the specified project_id
    cursor.execute('''
        UPDATE members
        SET Funding_Brought = NULL
        WHERE StudentName = ?
    ''', (StudentName,))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Example usage:
# delete_funding_brought("Gaurav Pande")


import sqlite3

import sqlite3

def insert_task_for_student(StudentName, task_description):
    conn = sqlite3.connect('members.db')
    cursor = conn.cursor()

    # Check if the "Task_to_complete" column is empty or NULL for the specific student
    cursor.execute('SELECT Task_to_complete FROM members WHERE StudentName = ?', (StudentName,))
    result = cursor.fetchone()
    current_task = result[0] if result else None

    if not current_task:
        # Update the "Task_to_complete" column only if it is empty or NULL
        cursor.execute('''
            UPDATE members
            SET Task_to_complete = ?
            WHERE StudentName = ?
        ''', (task_description, StudentName))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Example usage:
# insert_task_for_student(1, "Complete the report")  # Inserts "Complete the report" into the "Task_to_complete" column for student with ID 1, only if it is currently empty or NULL

# Example usage:
insert_task_for_student("Janhavi Raut", "Complete the report")  # Inserts "Complete the report" into the "Task_to_complete" column for student with ID 1
insert_task_for_student("Janhavi Raut", "Submit the Report")  # Inserts "Complete the report" into the "Task_to_complete" column for student with ID 1


