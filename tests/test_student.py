import pytest
from school_schedule.student import Student

def test_new_valid_student():
    #Arrange
    name = "Felipe"
    grade = "Junior"
    classes = ["Art", "Underwater Basket Weaving", "Algebra", "Computer Science"]

    #Act
    felipe = Student(name, grade, classes)

    #Assert
    assert felipe.name == name
    assert felipe.grade == grade
    assert felipe.classes == classes
    assert felipe.get_num_classes() == 4

def test_valid_add_class():
    #Arrange
    name = "Felipe"
    grade = "Junior"
    classes = ["Art", "Underwater Basket Weaving", "Algebra", "Computer Science"]

    #Act
    Felipe = Student(name, grade, classes)
    Felipe.add_class("French")

    #Assert 
    assert Felipe.get_num_classes() == 5
    assert "French" in Felipe.classes

def test_get_num_classes():
    #Arrange
    name = "Felipe"
    grade = "Junior"
    classes = ["Art", "Underwater Basket Weaving", "Algebra", "Computer Science"]

    #Act
    Felipe = Student(name, grade, classes)
    Felipe.get_num_classes()

    #Assert
    assert Felipe.get_num_classes() == 4

def test_remove_class_from_classes():
    #Arrange
    name = "Felipe"
    grade = "Junior"
    classes = ["Art", "Underwater Basket Weaving", "Algebra", "Computer Science"]

    #Act
    Felipe = Student(name, grade, classes)
    Felipe.remove_class("Art")

    #Assert
    Felipe.get_num_classes == 3


