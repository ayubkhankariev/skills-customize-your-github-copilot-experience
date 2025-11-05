
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Создать классическую игру «Виселица» на Python, где игроки угадывают слово по буквам. В задании практикуются работа со строками, циклы, условные операторы и ввод пользователя.

## 📝 Tasks

### 🛠️	Build the Hangman Game

#### Description
Реализуйте игру «Виселица», которая случайно выбирает слово из предопределённого списка и даёт игроку ограниченное число попыток угадывать буквы. После каждой попытки программа должна показывать текущее состояние отгаданного слова и количество оставшихся неверных попыток.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list (in-code list or external file)
- Accept single-letter guesses (case-insensitive) and reveal correct letters in a _ _ _ format
- Track and display incorrect guesses remaining
- Prevent repeated penalties for repeated guesses of the same letter
- End when the word is fully guessed or attempts are exhausted
- Display a clear win or lose message and reveal the target word on loss

##### Example session
```
Welcome to Hangman!
_ _ _ _ _
Guess a letter: a
_ a _ _ _   | Incorrect guesses left: 6
Guess a letter: e
_ a _ _ e   | Incorrect guesses left: 6
...
You won! The word was: 'magic'
```

### 🛠️	Optional Enhancements

#### Description
Добавьте дополнительные возможности для улучшения игры и практики (необязательно, но рекомендуется для бонуса).

#### Requirements
Completed enhancements may include one or more of the following:

- Difficulty levels (e.g., easy/medium/hard) that adjust allowed attempts or word length
- ASCII-art representation of the hangman that updates on each wrong guess
- Load word list from an external text/CSV file instead of an in-code list
- Save high scores (e.g., fewest incorrect guesses) to a local file

Примечание: Основная задача — реализовать функционал из секции Requirements; улучшения — опциональны и дают дополнительные баллы.
