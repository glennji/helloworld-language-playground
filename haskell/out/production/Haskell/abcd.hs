import System.Console.ANSI

main :: IO()
main = do
    setSGR [ SetColor Foreground Vivid Green ]
    putStrLn "Hello, World"