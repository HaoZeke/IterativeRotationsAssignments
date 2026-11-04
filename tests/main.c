#include "iralib_interf.h"
#include <stdio.h>

int main(){
  long i;
  char str[6];
  libira_get_version( str, &i );

  printf( "%li\n", i );
  printf( "%s\n", str );

  return 0;
}
