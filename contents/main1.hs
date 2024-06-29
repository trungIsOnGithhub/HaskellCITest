main :: IO()
main = do
    raw_input_str <- readFile("in.txt")
    let str_list = words raw_input_str
    let input_list = list_str_to_int str_list
    let str_result = show (separateSigns input_list)
    writeFile "out.txt" str_result