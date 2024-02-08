char * frequencySort(char * s){
    int chars[128] = {0};
    for (int i = 0; i < strlen(s); i++) {
        chars[s[i]] += 1;
    }

    for (int i = 0; i < 128; i++) {
        if (chars[i]) chars[i] = chars[i] * 1000 + i;
    }

    for (int i = 0; i < 127; i++) {
        int max = i;
        for (int j = i + 1; j < 128; j++) {
            if (chars[j] > chars[max]) max = j;
        }
        if (chars[max] == 0) break;
        if (i != max) {
            int tmp = chars[i];
            chars[i] = chars[max];
            chars[max] = tmp;
        }
    }

    char *result = malloc(strlen(s) + 1);
    int pos = 0;
    for (int i = 0; i < 128; i++) {
        if (!chars[i]) break;
        char c = chars[i] % 1000;
        int num = chars[i] / 1000;
        for (int j = 0; j < num; j++) {
            result[pos++] = c;
        }
    }
    result[pos] = '\0';
    return result;
}