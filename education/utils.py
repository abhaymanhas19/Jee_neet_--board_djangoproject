from enum import Enum


class CourseChoices(Enum):
    OneYearIntegrated = "OneYearIntegrated"
    TwoYearIntegrated = "TwoYearIntegrated"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class UserType(Enum):
    student = "student"
    parent = "parent"
    guardian = "guardian"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
