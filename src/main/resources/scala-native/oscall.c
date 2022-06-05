#include <stdio.h>

#include <stdlib.h>	//to use system()

void exec(char * s) {
  system(s);
}

char * input() {
  char * line = NULL;
  size_t len = 0;
  ssize_t lineSize = 0;
  lineSize = getline( & line, & len, stdin);
  return line;
}