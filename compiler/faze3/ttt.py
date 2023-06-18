
    #z = 100;
    z = hello(x, y);

    sum_three_for_test(x, y, z);

    return x + y + z;
# proc main:
#         mov r0, 0
#         mov r1, 110
#         add r3, 110, r1
#         mov r2, r3
#         mov r0, 50
#         cmp< r4, r0, r1
#         jz r4, L1
#         mov r0, 20
#         jmp L0
# L1:
#         mov r1, 30
# L0:
#         call hello, r0, r1
#         mov r2, r0
#         call sum_three_for_test, r0, r1, r2
#         add r6, r0, r1
#         add r5, r6, r2
#         mov r0, r5
#         ret
# proc sum_three_for_test:
#         add r4, r0, r1
#         add r3, r4, r2
#         mov r0, r3
#         ret
# proc hello:
#         mov r2, 0
#         call iput, r2
#         call iget, r4
#         mov r3, r4
# L2:
#         cmp> r5, r3, 5
#         jz r5, L3
#         add r6, r2, 1
#         mov r2, r6
#         sub r7, r3, 1
#         mov r3, r7
#         call iput, r2
#         jmp L2
# L3:
#         mov r0, 1000
#         add r8, r0, 1
#         mov r0, r8
#         mov r1, r0
#         mov r9, 0
#         mov r9, 5
# L4:
#         cmp< r10, r9, 10
#         jz r10, L5
#         add r11, r2, 1
#         mov r2, r11
#         call iput, r2
#         add r9, r9, 1
#         jmp L4
# L5:
#         mov r0, r2
#         ret


def int main() {
    var int x; # r0
    var int y = 110; # r1
    var int z = 110 + y; # r2

    x = 50;

    if (x < y) {
        x = 20;
    }
    else {
        y = 30;
    }

    #z = 100;
    z = hello(x, y);

    #another_func(x, y, z);

    sum_three_for_test(x, y, z);

    return x + y + z;
}

def int sum_three_for_test(int x, int y, int z) {
    return x + y + z;
}

def int hello(int xxx, int y) {
    var int x = 0;

    printInt(x);
    var int user_inp = scan();

    while (user_inp > 5) {
        x = x + 1;
        user_inp = user_inp - 1;
        printInt(x);
    }

    xxx = 1000;
    xxx = xxx + 1;
    y = xxx;

    var int i;
    for (i = 5 to 10) {
        x = x + 1;
        printInt(x);
    }

    return x;
}

def null another_func(int x, int y, int z) {
   var int lskfd = sum3(x, y, z);
   printInt(lskfd);
   var int fds = sum2(x, y);
   printInt(fds);
   returnzero();
}

def int sum2(int x1, int x2) {
   return x1 + x2;
}

def int returnzero() {
   return 0;
}

def int sum3(int x1, int x2, int x3) {
   return x1 + x2 + x3;
}