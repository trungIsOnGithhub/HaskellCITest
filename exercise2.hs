isLeapYear :: Int -> Bool
isLeapYear year = (year `mod` 4 == 0) && (year `mod` 100 /= 0 || year `mod` 400 == 0)

daysInMonth :: Int -> Int -> Int
daysInMonth month year | month <= 0 || month > 12 || year < 0 = -1
                    | (isLeapYear year) && (month == 2) = 29
                    | (month == 2) = 28
                    | (month < 8) && (month `mod` 2 == 0) = 30
                    | (month >= 8) && (month `mod` 2 /= 0) = 30
                    | otherwise = 31
main = do putStrLn (show (daysInMonth 2 2022)) -- February of 2022 first time i learned Lap Trinh Nang Cao
          putStrLn (show (daysInMonth 0 0))
          putStrLn (show (daysInMonth 1 2024))
          putStrLn (show (daysInMonth 2 2024))
          putStrLn (show (daysInMonth 3 2024))
          putStrLn (show (daysInMonth 4 2024))