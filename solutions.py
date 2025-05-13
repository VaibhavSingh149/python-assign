#--------Functions---------------

#Write a function called calculate_average 
def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

print(calculate_average([5, 10, 15, 20]))  # Should return 12.5
print(calculate_average([]))  # Should return 0

#greet user function
def greet_user(name, greeting="Hello"):
    return f"{greeting}, {name}!"
print(greet_user("Alice"))  # Should return "Hello, Alice!"
print(greet_user("Bob", "Hi"))  # Should return "Hi, Bob!"



#-----------Medium----------
#calculate total function
def calculate_total(*prices, discount=0):
    total = sum(prices)
    if discount:
        total -= total * (discount/100)
    return total
# Example usage:
print(calculate_total(10, 20, 30))  # Should return 60
print(calculate_total(10, 20, 30, discount=10))  # Should return 54 (10% off)



#create multiplier
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier
# Example usage:
double = create_multiplier(2)
triple = create_multiplier(3)
print(double(5))  # Should return 10
print(triple(5))  # Should return 15



#---------List Questions--------------

#filter even numbers
def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]
# Example usage:
print(filter_even_numbers([1, 2, 3, 4, 5, 6]))  # Should return [2, 4, 6]
print(filter_even_numbers([1, 3, 5]))  # Should return []



#merge sorted lists
def merge_sorted_lists(list1, list2):
    return sorted(list1 + list2)
# Example usage:
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # Should return [1, 2, 3, 4, 5, 6]
print(merge_sorted_lists([1, 2, 3], [4, 5, 6]))  # Should return [1, 2, 3, 4, 5, 6]

#Medium questions
#generate matrix
def generate_matrix(n, m):
    return [[i * j for j in range(m)] for i in range(n)]
# Example usage:
print(generate_matrix(3, 3))
# Should return:
# [
#   [0, 0, 0],
#   [0, 1, 2],
#   [0, 2, 4]
# ]


#transpose matrix
def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]
# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose_matrix(matrix))
# Should return:
# [
#   [1, 4],
#   [2, 5],
#   [3, 6]
# ]



#----------Tuples------------
#swap pairs
def swap_pairs(tup):
    return tuple(
        (tup[i + 1], tup[i]) if i % 2 == 0 else tup[i]
        for i in range(len(tup) - 1)
    ) + (tup[-1],) if len(tup) % 2 else tuple(
        (tup[i + 1], tup[i]) if i % 2 == 0 else tup[i]
        for i in range(len(tup))
    )
# Example usage:
print(swap_pairs((1, 2, 3, 4)))  # Should return (2, 1, 4, 3)
print(swap_pairs((1, 2, 3)))  # Should return (2, 1, 3)


#get stats
def get_stats(numbers):
    if numbers:
        return (
            min(numbers),
            max(numbers),
            sum(numbers),
            sum(numbers) / len(numbers)
        )
    return (None, None, 0, 0)
# Example usage:
print(get_stats([1, 2, 3, 4, 5]))  # Should return (1, 5, 15, 3.0)


#named tuples
from collections import namedtuple

# Define the Student named tuple
Student = namedtuple('Student', ['name', 'age', 'grades'])
def top_student(students):
    # Calculate the average grade for each student
    averages = [(student, sum(student.grades) / len(student.grades)) for student in students]
    
    # Find the student with the highest average grade
    return max(averages, key=lambda x: x[1])[0]
# Example usage:
from collections import namedtuple

# You'll define the Student named tuple

alice = Student("Alice", 20, (85, 90, 95))
bob = Student("Bob", 19, (70, 80, 90))
charlie = Student("Charlie", 21, (90, 92, 93))

print(top_student([alice, bob, charlie]))  # Should return the charlie Student tuple


#count_cordinate
from collections import Counter

def count_coordinate_occurrences(coords):
    return dict(Counter(coords))
# Example usage:
coords = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (1, 2)]
print(count_coordinate_occurrences(coords))
# Should return {(1, 2): 3, (3, 4): 2, (5, 6): 1}


#-------------Dictionary-----------
#Easy

def invert_dictionary(d):
    return {v: k for k, v in d.items()}
# Example usage:
print(invert_dictionary({"a": 1, "b": 2, "c": 3}))  # Should return {1: "a", 2: "b", 3: "c"}

#merge dictionaries
def merge_dictionaries(d1, d2):
    return {**d1, **d2}
# Example usage:
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(merge_dictionaries(dict1, dict2))  # Should return {"a": 1, "b": 3, "c": 4}

#Medium
#word freq
def word_frequencies(text):
    return {word: text.split().count(word) for word in set(text.split())}
# Example usage:
text = "the quick brown fox jumps over the lazy dog"
print(word_frequencies(text))
# Should return {"the": 2, "quick": 1, "brown": 1, "fox": 1, "jumps": 1, "over": 1, "lazy": 1, "dog": 1}


#nested contact dictionary
def add_contact(contacts, name, **details):
    if name not in contacts:
        contacts[name] = {}
    contacts[name].update(details)
# Example usage:
contacts = {}
add_contact(contacts, "Alice", phone="123-456-7890", email="alice@example.com")
add_contact(contacts, "Bob", phone="987-654-3210")
add_contact(contacts, "Alice", address="123 Main St")  # Updates Alice's info

print(contacts)
# Should return:
# {
#   "Alice": {"phone": "123-456-7890", "email": "alice@example.com", "address": "123 Main St"},
#   "Bob": {"phone": "987-654-3210"}
# }
