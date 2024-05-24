import Data.List
import Data.Maybe
import Data.Set 

-- toList :: Set a -> [a] -- O(N)
-- fromList :: Ord a => [a] -> Set a -- O(logN)
makeListUnique :: Ord a => [a] -> [a]
makeListUnique = toList . fromList

pairsWithSumUniqueList :: Int -> [Int] -> [(Int, Int)]
pairsWithSumUniqueList total xs = [(x1, total-x1) | x1 <- xs, isJust (find (== (total-x1)) xs)]

pairsWithSum :: Int -> [Int] -> [(Int, Int)]
pairsWithSum total xs = pairsWithSumUniqueList total (makeListUnique xs)

main = do putStrLn (show (pairsWithSum 8 [0,8,0,0,0,0]))
          putStrLn (show (pairsWithSum 8 [1,2,3,4,5,6]))
          putStrLn (show (pairsWithSum 8 [-8,9,9,9,9,9]))
          putStrLn (show (pairsWithSum 8 [1,3,5,7,9,11]))
          putStrLn (show (pairsWithSum 8 [-8,16,-16,8]))
          putStrLn (show (pairsWithSum 8 []))