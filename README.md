# teslang-compiler
Compiler Frontend  +  IR  Built  in Pythone



test:
    1 + 2*3  => tree generation
    (-1 + 4)*5
    2^3
    =  => show invalid syntaxt that means it pass lexer and problem is in parser otherwise it should trow illigal charecter error
    VAR a = 5   => return 5
    a   => return 5
    a + 2   => return 7
    null    =>  0
    VAR a = VAR b = VAR c = 10    
    5 + (VAR x = 6)   =>  res == 11 , x == 6
    VAR + LET a = 4   => EXPECTED 'VAR','+' , ....
    5 + LET a = 4   => EXPECTED '+' , ....
    VAR a = 0 , 10 / a  => divition by zero and pointing to where diviron by zero acured not variable assignment to zero     

    logical operators
        5 == 5   => 1
        2 + 2 == 1 + 3  => 1
        1 == 1 AND 5 == 5   => 1
        5 < 6   => 1
        NULL, TRUE , FALSE, => 0,1,0
        not 0 => 1
        
    if statemenmt:
        IF 5==5 THEN 123    => 123
        IF 5==5 THEN 123 ELSE 234    => 234
        VAR age = 19 ,   VAR price = IF age >= 19 THEN 40 ElSE 20   => 40     
        
    for and while statement:
        VAR res = 1 ,   FOR i = 1 TO 6 THEN VAR res = res * i, res   => 120
        VAR res = 1 ,   FOR i = 5 TO 0 STEP -1 THEN VAR res = res * i, res   => 120
        WHILE TRUE THEN 123  => stay in infinite loop
        VAR i = 0 ,   WHILE i <10000 THEN VAR i = i + 1, res   => close after seconds
         
    functions:
        FUN add (a, b) -> a + b  =>  <functin add>
        add(5,6)  => 11
        add() or add(5,3,74,8,6)     => throw error
        VAR some_function = add, some_function => <functin add> , some_function(1,2) => 3
        VAR some_function = FUN (a) -> a + 2  =>  <functin <anonymous>>, some_function(1) => 3
        traceback error:
            FUN test(a) -> a / 0, test(1651) => ....

    Strings:
        "this is a string" => "this is a string"
        "this is" +  "a string" => "this is a string"
        "salam " * 3  => "salam salam salam"

    lists:
        [],
        [1,2,3] + 4  => [1,2,3,4]
        [1,2,3] * [4,5,6]  => [1,2,3,4,5,6]
        [1,2,3] - 1  => [1,3]  remove element in that position
        [1,2,3] - -1  => [1,2]
        [1,2,3] / 1  => 2   get element in that position
        [1,2,3] / -1  => 3 


    Built in functions:
        MATH_PI => 3.14
        PRINT("priting s.th")  => priting s.th
        VAR name = INPUT() , s.th => s.th  also name => s.th
        CLS() => clear screen
        IS_NUM(123) , IS_SRE("dferw") , IS_LIST([]) , IS_FUN(PRINT) => 1
        appened to list:
            VAR list = [1,2,3] , APPEND(list,4) => [1,2,3,4]
        pop from list:
            APPEND(list,3) => 4, [1,2,3]
        extend list:
            EXTEND(list,[4,5,6]) => 0, [1,2,3,4,5,6]

    Multi-line statements:
        1+2;2+3;3+3;  => [3,5,6]
        ;;;;;;; 1+2;2+3 ;;;;;;;  => [3,5]
        IF 5==5 THEN;PRINT('eerg');PRINT('eergds'); ELSE PRINT('rtg')


    Break Continue Return:
        FUN tset(); VAR foo = 5; RETURN foo; END => <function test>,  test() => 5

        VAR a = [] , FOR i = 0 TO 10 TEHN; IF i == 4 THEN CONTINUE ELIF i == 8 THEN BREAK; VAR a = a + i; END
        a => [0,1,2,3,5,6,7] 

        VAR a = [] , VAR i = 0 , WHILE i < 10 TEHN; VAR i = i + 1; IF i == 4 THEN CONTINUE; IF i == 8 THEN BREAK; VAR a = a + i; END  , a => [0,1,2,3,5,6,7]
            

    Running program:
        python3 shell.py
        RUN("example.myopl")
        RUN("test.txt")


    

improvemnet:
    1 + man  => semantic error 
 

