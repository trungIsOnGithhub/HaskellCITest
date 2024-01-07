module HaskellExercise
(
    addNum,
    sumList
) where

addNum :: Int -> Int -> Int
addNum num1 num2 = num1 + num2

sumList :: Num a => [a] -> a
sumList [] = 0
sumList (x:xs) = x + sumList xs