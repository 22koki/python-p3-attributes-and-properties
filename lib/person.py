#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

# lib/person.py

class Person:
    approved_jobs = ["Engineer", "Teacher", "Doctor", "Artist", "Manager"]

    def __init__(self, name, job="Unemployed"):
        self._name = None  # Internal attribute to store the name
        self.name = name  # Use the property setter for validation
        self._job = None  # Internal attribute to store the job
        self.job = job  # Use the property setter for validation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be a string under 25 characters.")
        else:
            self._name = value.title()  # Convert name to title case before saving

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value not in Person.approved_jobs:
            print("Job must be in the list of approved jobs.")
        else:
            self._job = value

