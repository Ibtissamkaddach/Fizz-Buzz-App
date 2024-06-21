# FizzBuzz App

This is a simple FizzBuzz application written in Python. The FizzBuzz game prints numbers from 1 to a specified number. For multiples of three, it prints a custom word defaulted as "Fizz" instead of the number and for multiples of five, it prints a custom word defaulted as "Buzz". For numbers that are multiples of both three and five, it prints both the words as a defaulted "FizzBuzz".
This App has a command line to Allow users to pass the number as a command-line argument and be more responsive by allowing users to specify custom words for multiples of 3 and 5 and by Logging the output to a file.

## Features

- Command-line argument support for specifying the number to play up to.
- Customizable words for multiples of 3 and 5.
- Logs the output to a file.

## How to Use

1. Clone the repository:
   ```sh
   git clone https://github.com/Ibtissamkaddach/Fizz-Buzz-App.git

   Navigate to the project directory:
   ```sh
   cd fizzbuzz-app 

   Run the script with the default words:
   ```sh
   python fizzbuzz.py 100

   Run the script with custom words and a custom log file:
   ```sh
   python fizzbuzz.py 100 --word1 Foo --word2 Bar --log custom_log.log
   
2. Initialize Git and commit the code
# Initialize Git repository
git init

# Add all files to the repository
git add .

# Commit the changes
git commit -m "Initial commit - Add FizzBuzz app"

# Add the remote repository
git remote add origin https://github.com/Ibtissamkaddach/Fizz-Buzz-App.git

# Push the changes to the remote repository
git push -u origin main

## Contributing

Your contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit them (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License. See the file for details.

## Contact

If you have any questions or suggestions, feel free to contact me.
