import argparse
import logging

def fizzbuzz(n, word1, word2, log_file):
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(message)s')

    for i in range(1, n + 1):
        result = ''
        if i % 3 == 0:
            result += word1
        if i % 5 == 0:
            result += word2
        if not result:
            result = str(i)
        print(result)
        logging.info(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FizzBuzz Game")
    parser.add_argument('number', type=int, help="The number to play FizzBuzz up to")
    parser.add_argument('--word1', type=str, default="Fizz", help="Word for multiples of 3")
    parser.add_argument('--word2', type=str, default="Buzz", help="Word for multiples of 5")
    parser.add_argument('--log', type=str, default="fizzbuzz.log", help="Log file name")

    args = parser.parse_args()

    fizzbuzz(args.number, args.word1, args.word2, args.log)