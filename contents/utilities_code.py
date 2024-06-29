utilities_haskell_code = '''
    str_to_int :: String -> Int
    str_to_int str = read str
    list_str_to_int :: [String] -> [Int]
    list_str_to_int [] = []
    list_str_to_int (x:xs) = str_to_int x : list_str_to_int xs
'''

if __name__ == '__main__':
    print(utilities_haskell_code)