
```C
int count_num_states(char *input_file) {
  FILE *fp = fopen(input_file, "r");
  if (fp == NULL) return 0;
  
  int result = 0; 
  
  char temp; // just so that fscanf can write into it
  while (fscanf(fp, "%c", &temp) != EOF) {
    if (temp == '\n') {
      result++;
    }
  }
  
  fclose(fp);
  
  return result;
}

int generate_report(char *input_file) {
  
  if (input_file == NULL) return 0;
  int num_states = count_num_states(input_file);
  
  FILE *fp = fopen(input_file, "r"); // check
  if (fp == NULL) return 1;
  
  print_header();
  
  // skip csv header
  char temp; 
  while (fscanf(fp, "%c", &temp) != EOF) {
    if (temp == '\n') break;
  }
  
  int counter = 0; 

  for (int i = 1; i <= num_states; i++) {
    // mostly placeholder memory locations for fscanf
    char c1[STRSIZE], c2[STRSIZE], c3[STRSIZE], c4[STRSIZE], c5[STRSIZE], c6[STRSIZE];
    int returns, exempts, agi;
    
    // last 3 values are ints, rest are strings
    // arrays are automatically the memory address, ints need &name to get to the address
    
    // it skips all white characters until it gets to the next string (int later), if f.ex. comma was the separator, do fscanf(fp, "%[^,],%[^,],%d", origin, name, &agi);
    
    int items = fscanf(fp, "%s %s %s %s %s %s %d %d %d", c1, c2, c3, c4, c5, c6, &returns, &exempts, &agi);
    
    // to compare 2 strings, use strcmp
    
    if (strcmp(c1, "\"25\"") == 0) {
      print_state(c6, agi); 
      counter += agi;
    }
    
  }
  
  print_footer(counter);
  fclose(fp);
  return 0;
}
```