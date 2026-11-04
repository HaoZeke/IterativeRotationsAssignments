#include "iralib_interf.h"
#include <string.h>

int main(void) {
  char version[6] = {0};
  long date = 0;
  libira_get_version(version, &date);
  if (strcmp(version, "2.2.0") != 0) return 1;
  if (date != 20250911) return 2;
  if (libira_get_nmax() != 400) return 3;
  return 0;
}
