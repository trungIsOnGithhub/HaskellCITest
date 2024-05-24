transform :: [Int] -> [Int]
transform xs = [x*3 | x <- xs, x `mod` 2 == 0]

main = do putStrLn (show (transform [0,0,0,0,0,0]))
          putStrLn (show (transform [1,2,3,4,5,6]))
          putStrLn (show (transform [-8,9,9,9,9,9]))
          putStrLn (show (transform [1,3,5,7,9,11]))
          putStrLn (show (transform [-8,-6,-6,-8]))
          putStrLn (show (transform []))