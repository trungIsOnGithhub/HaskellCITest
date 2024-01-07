module HaskellExercise where

addNum :: Int -> Int -> Int
addNum num1 num2 = num1 + num2

sumList :: Num a => [a] -> a
sumList [] = 0
sumList (x:xs) = x + sumList xs

-- main :: IO()
-- main =  do
--    putStr "Sum of 2 numbers = "
--    print(addNum 10 25)