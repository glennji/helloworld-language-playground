module Paths_Haskell (
    version,
    getBinDir, getLibDir, getDataDir, getLibexecDir,
    getDataFileName, getSysconfDir
  ) where

import qualified Control.Exception as Exception
import Data.Version (Version(..))
import System.Environment (getEnv)
import Prelude

catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
catchIO = Exception.catch


version :: Version
version = Version {versionBranch = [1,0], versionTags = []}
bindir, libdir, datadir, libexecdir, sysconfdir :: FilePath

bindir     = "/Users/gmason/Library/Haskell/bin"
libdir     = "/Users/gmason/Library/Haskell/ghc-7.8.3-x86_64/lib/Haskell-1.0"
datadir    = "/Users/gmason/Library/Haskell/share/ghc-7.8.3-x86_64/Haskell-1.0"
libexecdir = "/Users/gmason/Library/Haskell/libexec"
sysconfdir = "/Users/gmason/Library/Haskell/etc"

getBinDir, getLibDir, getDataDir, getLibexecDir, getSysconfDir :: IO FilePath
getBinDir = catchIO (getEnv "Haskell_bindir") (\_ -> return bindir)
getLibDir = catchIO (getEnv "Haskell_libdir") (\_ -> return libdir)
getDataDir = catchIO (getEnv "Haskell_datadir") (\_ -> return datadir)
getLibexecDir = catchIO (getEnv "Haskell_libexecdir") (\_ -> return libexecdir)
getSysconfDir = catchIO (getEnv "Haskell_sysconfdir") (\_ -> return sysconfdir)

getDataFileName :: FilePath -> IO FilePath
getDataFileName name = do
  dir <- getDataDir
  return (dir ++ "/" ++ name)
