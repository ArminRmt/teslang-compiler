# teslang-compiler
Compiler Frontend  +  IR  Built  in Pythone




def int find(vector A, int n) {
    var int k;
    var int j;

    for (i = 0 to 5) {
        if (n == k) {
            return j;
        }
        j = j + 1;
    }   

    return -1;
}


def int main() {
    var int A;
    var int a;

    A = list(3);
    A[0] = 1;
    A[1] = 2;
    A[2] = 3;

    print(find(A));
    print(find(A, a));
    print(find(a, A));

    return A;
}






while loop

def int res(int c) {
    int x = 2
    while(x) print("salam ")
}


logical operator

def int res(int a) {
    b = 2 > 1;
    c = 4 > 1 && 1 < 2;
    d = b == c;
}




nested for loop

def int main() {
    var vector a = [1, 2, 3, 4, 5];
    var int result = 0;
    
    for(i = 0 to length(a)) {
      for(i = 0 to length(a)) {
        result = result + a[i];
        }
    }
}





built in length

def int main() {
    var vector a = [1, 2, 3, 4, 5];

    print(length(a));
}


Scope

def int main() {

    var int a = 1;

    def int res() {
          var int a = 2;
          print(a);
    }

   print(a);
}





it shouldnt run what is inside the function

def int res() {
    var int a = 1;
    print(a);
}
def int res() {
      var int b = 2;
      print(b);
}



func argumans

def int res(int b, int c) {
    var int a = 1;
    print(a);
}


return type

def str main(int b, int c) {
    var int a = 1;
    print(a);

    return a;
}



For loop

def int main(int b, int c) {
    var int a = 1;
    
    for (i = 0 to 2) {
      a = a + 1;
    }

    print(a);

}



assign varible

def int main(int b, int c) {
    var int a;
    a = 5;
    print(a);
    
}



list 

def int main(int b, int c) {
    var vector a = [1,2,3];
    print(a);
    a[1] = 5;
    print(a);
    print(a[1]);
}




functoin call

def int res(int b, int c) {
      var int a = 5;
      return a;
}
def int main() {
      var int b = res(1,2);
      print(b);
}



UnaryNot

def int main() {
    b = !1;
    print(!0);
}



unarry operation

def int main() {
      var int a = 8;
      var int b = 4;
      var int c = a + b;
      print(c);
}



 

