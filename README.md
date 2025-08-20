# Math Quiz

Welcome to the **Math Quiz**! This is a simple Python console program that helps you practice and test your multiplication skills with random problems. Challenge yourself, track your score, and have fun improving your math!

---

## Table of Contents

- [Math Quiz](#math-quiz)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [How It Works](#how-it-works)
  - [Rules](#rules)
  - [Features](#features)
  - [How to Use](#how-to-use)
  - [Scoring \& Feedback](#scoring--feedback)
  - [Example Session](#example-session)
  - [Customization](#customization)
  - [License](#license)

---

## Overview

Math Quiz is an interactive command-line game where you select a multiplication table (the "multiple") and then answer 10 randomly generated questions. It's an excellent tool for students and anyone wanting to sharpen their mental math skills.

---

## How It Works

- You choose which multiplication table (e.g., 2, 5, 7, 12) you want to practice.
- The program generates 10 random multiplication questions based on your choice.
- For each question, you input your answer.
- If you're unsure, you can type `00000` (five zeros) to reveal the correct answer.
- After 10 questions, you receive your score and feedback.
- You can choose to play again or exit.

---

## Rules

1. **Choose a Multiple:**  
   When prompted, enter the number you want to test (e.g., 7 for the 7 times table).

2. **Answer Questions:**  
   For each question (e.g., `6 x 7`), type your answer and press Enter.

3. **Reveal the Answer:**  
   If you don't know the answer, type `00000` (exactly five zeros) to see the correct answer.

4. **Scoring:**  
   - One point for each correct answer.
   - No penalty for skipping (using `00000`), but you don't get a point.

5. **Feedback:**  
   After 10 questions, your score and feedback message are displayed.

6. **Play Again:**  
   Type `yes` to play again, or `no` to quit.

---

## Features

- Random multiplication problems for the chosen table
- Score tracking
- Immediate feedback (correct/wrong/answer reveal)
- Motivational messages based on your score
- Option to replay as many times as you like

---

## How to Use

1. **Prerequisites:**  
   - Python 3.x installed on your system

2. **Running the Quiz:**  
   - Save the code in a file named `MathQuiz.py`
   - Open a terminal or command prompt
   - Navigate to the folder containing `MathQuiz.py`
   - Run the program with:
     ```
     python MathQuiz.py
     ```

---

## Scoring & Feedback

| Score Range | Message                                         |
|-------------|-------------------------------------------------|
| 10/10       | You got all questions correct! 🏆🏆🥇🙌🙌           |
| 7-9         | Great job! 👍                                   |
| 5-6         | Not bad! 👌                                     |
| 3-4         | You can do better! 👎                           |
| 1-2         | You need to practice more! 👎👎                  |
| 0           | You got 0 out of 10 questions correct.          |

---

## Example Session

```
——————————Math Quiz——————————

Welcome to the Math Quiz!
You will be given a math problem to solve.
If you get it right, you get a point!
Type, 00000 if you don't know the answer. Remember. Type 0, 5 times.

First you choose what multiples you want to test yourself on. 7
4 x 7
> 28
Correct!
9 x 7
> 00000
63
3 x 7
> 21
Correct!
...

You got 7 out of 10 questions correct. Great job! 👍
Do you want to play again? (yes/no). no
```

---

## Customization

- Adjust the range of questions by modifying `random.randint(0, 12)` in the code.
- Change the number of questions by modifying the `for i in range(1, 11):` loop.
- Add support for other operations (addition, subtraction, division) for further practice.

---

## License

This project is provided for educational purposes and is open to modification and sharing.

---
