int evalRPN(char ** tokens, int tokensSize){
    int64_t* values = malloc(tokensSize * sizeof(int64_t));
    int64_t v_c = 0;
    for (int i = 0; i < tokensSize; i++) {
        switch (tokens[i][0]) {
            case '+':
                values[v_c - 1] += values[--v_c];
                break;
            case '*':
                values[v_c - 1] *= values[--v_c];
                break;
            case '/':
                values[v_c - 1] /= values[--v_c];
                break;
            case '-':
                if (tokens[i][1] == '\0') {
                    values[v_c - 1] -= values[--v_c];
                    break;
                }
            default: {
                int64_t n = 0;
                int power = 1;
                for (int c = strlen(tokens[i]) - 1; c >= 0; c--) {
                    if (tokens[i][c] == '-') {
                        n *= -1;
                        break;
                    }
                    n += power * (tokens[i][c] - '0');
                    power *= 10;
                }
                values[v_c++] = n;
            }
        }
    }
    v_c = values[0];
    free(values);
    return v_c;
}