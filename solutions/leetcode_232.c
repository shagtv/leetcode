typedef struct {
    int8_t* s1;
    int8_t* s2;
    int c;
    int n1;
    int n2;
} MyQueue;

MyQueue* myQueueCreate() {
    MyQueue* q = malloc(sizeof(MyQueue));
    q->c = 5;
    q->s1 = malloc(5);
    q->s2 = malloc(5);
    q->n1 = 0;
    q->n2 = 0;
    return q;
}

void myQueuePush(MyQueue* obj, int x) {
    if (obj->n1 >= obj->c) {
        obj->c *= 2;
        obj->s1 = realloc(obj->s1, obj->c);
        obj->s2 = realloc(obj->s2, obj->c);
    }
    obj->s1[obj->n1] = x;
    obj->n1 += 1;
}

int myQueuePop(MyQueue* obj) {
    while (obj->n1 > 0) {
        obj->n1 -= 1;
        obj->s2[obj->n2] = obj->s1[obj->n1];
        obj->n2 += 1;
    }
    obj->n2 -= 1;
    int item = obj->s2[obj->n2];
    while (obj->n2 > 0) {
        obj->n2 -= 1;
        obj->s1[obj->n1] = obj->s2[obj->n2];
        obj->n1 += 1;
    }
    return item;
}

int myQueuePeek(MyQueue* obj) {
    return obj->s1[0];
}

bool myQueueEmpty(MyQueue* obj) {
  return obj->n1 == 0;
}

void myQueueFree(MyQueue* obj) {
    free(obj->s1);
    free(obj->s2);
    free(obj);
}
