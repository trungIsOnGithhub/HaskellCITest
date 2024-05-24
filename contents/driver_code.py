driver_code = {
    'ex1': {
        'input': '\nmain :: IO()\nmain = do\n raw_input_str <- readFile("in.txt")\n let str_list = words raw_input_str',
        'solution': '\n let input_list = list_str_to_int str_list\n let str_result = (show (separateSigns input_list))',
        'output': '\n writeFile "out.txt" str_result',
    },
    'ex2': {
        'input': '\nmain :: IO()\nmain = do\n raw_input_str <- readFile("in.txt")\n let str_list = words raw_input_str',
        'solution': '\n let input_list = list_str_to_int str_list\n let str_result = (show (daysInMonth (input_list !! 0) (input_list !! 1)))',
        'output': '\n writeFile "out.txt" str_result',
    }
}

if __name__ == '__main__':
    print(driver_code)