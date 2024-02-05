int firstUniqChar(char* s) {
    int chars[26] = {0};
    int i = 0;
    while (s[i] != '\0')
        chars[s[i++] - 'a']++;
    i = 0;
    while (s[i] != '\0')
        if (chars[s[i++] - 'a'] == 1)
            return i - 1;
    return -1;
}
