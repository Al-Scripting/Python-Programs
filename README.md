# Python Programs Repository

## Overview
This repository contains a collection of Python programs covering various topics such as algorithms, data processing, automation, and error handling. Each program serves a specific purpose and helps in understanding different Python concepts.

## List of Programs & Explanations

### 1️⃣ ATM_Muqshith_100862739.py
**Description**: Simulates an Automated Teller Machine (ATM) where users can deposit, withdraw, and check their account balance.

**Key Functions:**
```python
def deposit(self, amount):
    """Adds the specified amount to the balance."""
    self.balance += amount
    return f"Deposited {amount}. New balance: {self.balance}"

def withdraw(self, amount):
    """Withdraws the amount if sufficient balance is available."""
    if amount > self.balance:
        return "Insufficient funds!"
    self.balance -= amount
    return f"Withdrew {amount}. New balance: {self.balance}"
```

### 2️⃣ Assignment1_100862739_Muqshith_Shifan.txt
**Description**: A text file containing solutions and explanations to assignment problems related to Python programming.

### 3️⃣ Bonus 1 L9.py
**Description**: A bonus program from Lecture 9, implementing advanced data structures.

**Key Functions:**
```python
def add_edge(self, node, neighbor):
    """Adds an edge between two nodes in a graph."""
    if node not in self.graph:
        self.graph[node] = []
    self.graph[node].append(neighbor)
```

### 4️⃣ Bonus [Lecture 6].py
**Description**: A bonus program focusing on **file handling and regular expressions**.

**Key Functions:**
```python
def extract_emails(text):
    """Extracts email addresses from the given text using regex."""
    return re.findall(r'[\w\.-]+@[\w\.-]+', text)
```

### 5️⃣ ErrorHandling.py
**Description**: Demonstrates **Python's exception handling** to manage runtime errors gracefully.

**Key Functions:**
```python
def check_positive(number):
    """Raises an exception if the number is negative."""
    if number < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    return f"Number {number} is positive."
```

### 6️⃣ LetterCounter.py
**Description**: Counts occurrences of each letter in a given text input.

**Key Functions:**
```python
def letter_count(text):
    """Counts occurrences of each letter in the text, ignoring spaces."""
    text = text.lower().replace(" ", "")
    return Counter(text)
```

### 7️⃣ Payroll.py
**Description**: Simulates a payroll system that calculates employee salaries based on their hours worked and hourly rate.

**Key Functions:**
```python
def calculate_salary(hours, rate):
    """Calculates the salary based on hours worked and hourly rate."""
    return hours * rate
```

### 8️⃣ Project3_Group3_ReCoders_2.py
**Description**: A **team project** implementing an application using Python.

### 9️⃣ Quiz_Muqshith_Shifan_100862739.py
**Description**: A simple **quiz game** that asks multiple-choice questions and evaluates user responses.

**Key Functions:**
```python
def ask_question(self, question, answer):
    """Prompts the user with a question and validates their response."""
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        self.score += 1
    return self.score
```

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/Al-Scripting/Python-Programs
   ```
2. Navigate to the directory:
   ```bash
   cd Python-Programs
   ```
3. Run the desired Python script:
   ```bash
   python script_name.py
   ```

## Contributions
- Contributions are welcome! Feel free to **fork** the repository and submit a **pull request**.
- If you encounter any issues, report them in the **Issues** section.

## License
This repository is available under the **MIT License**.
