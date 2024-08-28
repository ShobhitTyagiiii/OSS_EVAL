{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e6d6b6cd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Student Rohit Sharma added successfully.\n",
      "Student Virat Kohli added successfully.\n",
      "Student Hardik Pandya added successfully.\n",
      "Grades updated for student ID {student_id}.\n",
      "Grades updated for student ID {student_id}.\n",
      "Grades updated for student ID {student_id}.\n"
     ]
    }
   ],
   "source": [
    "students = {}\n",
    "\n",
    "def add_student(student_id, name, student_class):\n",
    "   \n",
    "    if student_id in students:\n",
    "        print(f\"Student ID {student_id} already exists.\")\n",
    "    else:\n",
    "        students[student_id] = {\n",
    "            'name': name,\n",
    "            'class': student_class,\n",
    "            'grades': []\n",
    "        }\n",
    "        print(f\"Student {name} added successfully.\")\n",
    "\n",
    "add_student('001', 'Rohit Sharma', 'IV')\n",
    "add_student('002', 'Virat Kohli', 'V')\n",
    "add_student('003', 'Hardik Pandya', 'VI')\n",
    "def update_grades(student_id, new_grades):\n",
    "\n",
    "    if student_id in students:\n",
    "        students[student_id]['grades'] = new_grades\n",
    "        print(\"Grades updated for student ID {student_id}.\")\n",
    "    else:\n",
    "        print(\"Student ID {student_id} does not exist.\")\n",
    "\n",
    "update_grades('001', [99, 75, 68, 41])\n",
    "update_grades('002', [79, 83, 94, 78])\n",
    "update_grades('003', [97, 82, 88, 67])\n",
    "\n",
    "\n",
    "def calculate_average(student_id):\n",
    "  \n",
    "    if student_id in students:\n",
    "        grades = students[student_id]['grades']\n",
    "        if grades:\n",
    "            average = sum(grades) / len(grades)\n",
    "            return average\n",
    "        else:\n",
    "            print(f\"No grades available for student ID {student_id}.\")\n",
    "            return 0\n",
    "   \n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f118fe4c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
