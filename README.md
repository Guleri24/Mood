# Mood - WIP
 Minimalistic user mood generator and executor

## Build Mood locally
### Install Scala
```
    curl -fLo cs https://git.io/coursier-cli-"$(uname | tr LD ld)"
    chmod +x cs
    ./cs install
    rm ./cs
    cs setup
```
### Install LLVM and CLang
OpenSUSE
```
sudo zypper install clang llvm 
```

### Mood 
```
git clone https://github.com/Guleri24/Mood
cd Mood
sbt run
```
The native Mood file(`mood-out`) is generated in the `target/scala-*.*.*/` directory.
