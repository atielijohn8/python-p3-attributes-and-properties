#!/usr/bin/env python3

class Person:
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

    def __init__(self, name="John Kennedy", job="Sales"):
        self.name = name
        self.job  = job

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, newname):
        if isinstance(newname, str) and 1 <= len(newname) <= 25:
            self._name = newname
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def job(self):
        return self._job
    
    @job.setter
    def job(self, newJob):
        if newJob.title() in Person.APPROVED_JOBS:
            self._job = newJob.title()
        else:
            print("Job must be in list of approved jobs.")


Person1 = Person ("john", "Legal")