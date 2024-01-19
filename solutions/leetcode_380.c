
#define N 10000
#define hash(index) index < 0 ? (-index + 100) % N : index % N

typedef struct {
    int data[N][2];
    int list[N];
    int count;
} RandomizedSet;

RandomizedSet* randomizedSetCreate() {
    srand(time(NULL));
    
    RandomizedSet* set = malloc(sizeof(RandomizedSet));
    set->count = 0;
    return set;
}

bool randomizedSetInsert(RandomizedSet* obj, int val) {
    int key = hash(val);
    
    if (obj->data[key][0] == val) {
        return false;
    }
    obj->list[obj->count] = val;
    obj->data[key][0] = val;
    obj->data[key][1] = obj->count;
    obj->count++;
    
    return true;
}

bool randomizedSetRemove(RandomizedSet* obj, int val) {
    int key = hash(val);    
    if (obj->data[key][0] != val) {
        return false;
    }
    
    int current_last_val = obj->list[obj->count - 1];
    int deleted_list_index = obj->data[key][1];
    obj->list[deleted_list_index] = current_last_val;
    obj->data[hash(current_last_val)][1] = deleted_list_index;

    obj->data[key][0] = INT_MAX;
    obj->count--;
    
    return true;
}

int randomizedSetGetRandom(RandomizedSet* obj) {
    return obj->list[rand() % obj->count];
}

void randomizedSetFree(RandomizedSet* obj) {
    free(obj);
}
