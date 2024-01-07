module TestExercises where

import Test.HUnit
import HaskellExercise

testExercise1 :: Test
testExercise1 =
    TestCase $ assertEqual
        "Testing case 1" 2 (addNum 1 1)

testExercise2 :: Test
testExercise2 =
    TestCase $ assertEqual
        "Testing case 2" 10 (sumList [1, 2, 3, 4])

main :: IO Counts
main = runTestTT $ TestList [testExercise1, testExercise2]