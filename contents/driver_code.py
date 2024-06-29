driver_code = {
    'ex1': {
        '''
        main :: IO()
        main = do
          raw_input_str <- readFile("in.txt")
          let str_list = words raw_input_str
          let input_list = list_str_to_int str_list
          let str_result = show (separateSigns input_list)
          writeFile "out.txt" str_result
        '''
    },
    'ex2': {
        '''
        main :: IO()
        main = do
          raw_input_str <- readFile("in.txt")
          let str_list = words raw_input_str
          let input_list = list_str_to_int str_list
          let str_result = (show (daysInMonth (input_list !! 0) (input_list !! 1)))
          writeFile "out.txt" str_result
        '''
    }
}
def get_driver_haskell_code(exercise_keys):
    try:
        driver_haskell_code = {}
        for key in exercise_keys:
            with open(f'main-{key}.hs') as driver_code_file:
                driver_haskell_code[key] = f.read()

        return driver_haskell_code
    except:
        raise Exception('Cannot prepared driver code for all source files')

if __name__ == '__main__':
    print(get_driver_haskell_code(2))