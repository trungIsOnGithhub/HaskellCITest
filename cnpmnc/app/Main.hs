module Main where

import System.Exit
import HaskellExercise

-- testExercise1 :: Test
-- testExercise1 =
--    TestCase (assertEqual "Testing case 1" 2 (addNum 1 1))

-- testExercise2 :: Test
-- testExercise2 =
--    TestCase (assertEqual "Testing case 2" 10 (sumList [1, 2, 3, 4]))

main :: IO ()
main = do
    if addNum 1 1 == 2 then print("Test 1 passed")
    else die("Test 1 failed")

    if sumList [1,2,0] == 4 then print("Test 2 passed")
    else die("Test 2 failed")

-- runTestTTAndExit (TestList [testExercise1, testExercise2])