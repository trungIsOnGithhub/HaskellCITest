utilities_code = '\nstr_to_int :: String -> Int\nstr_to_int str = read str\nlist_str_to_int :: [String] -> [Int]\nlist_str_to_int [] = []\nlist_str_to_int (x:xs) = str_to_int x : list_str_to_int xs'

if __name__ == '__main__':
    print(utilities_code)