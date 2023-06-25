## teslang-compiler
Teslang-compiler is a Python-based compiler that can generate intermediate code from input files, perform semantic analysis, and optimize code through register allocation.      

<br> 

## Installation     
clone project ```git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git```                    
install ply ```pip install ply``` s.th like this    
for Phase 2 add your test in test.txt file      
for Phase 3 add your test in IRtest.txt file remember to clear it every time you want to test     
run ```python3 main.py```      


<br> 
     

## Features   

- **Lexical Analysis**: Tokenizes input files
- **Parsing**: Parses tokenized files into an Abstract Syntax Tree (AST)
- **Semantic Analysis**: Checks the AST for semantic errors
- **Code Generation**: Generates intermediate code from the AST
- **Optimization**: Planned for future implementation
- **Scopes**: Tracks variable and function scopes
- **Error Correction**: Provides suggestions for fixing syntax errors
- **Forward Referencing**: Resolves references to functions and variables before they are defined
- **Solid Principles**: Follows SOLID design principles
- **Comments**: Planned for Phase 3 implementation
- **Built-in Functions**: Includes several built-in functions
- **Interpreter Support**: Supports debugging and potentially making an entire interpreter in the future

<br>    

## Phase 1,2
Phases 1 and 2 implement lexical analysis and parsing. These phases are well-organized and maintainable but are implemented as a two-pass compiler, meaning small tricks are taken instead of parsing and performing semantic operations.      

<br>    

## Phase 3        

Code Generation implemented based on my teacher doc and TSVM           
you can find out about TSVM [here](https://github.com/aligrudi/tsvm/tree/master)     
 
Please note that due to limited time, Phase 3 was not implemented in an efficient way, and optimization was not considered. However, ideas for implementation are provided in the TODOs and comments in the code.



<br> 


## Design patterns           
### **Singelton**  : with just one instance of CodeGenerator()              
### **Composite**: Create a tree-like structure with Ast                     
### **Visitor**: AstVisitor class explores an Object without changing it            
### **Iterator**: Acess symbol table class objects one by one           
### **Decorator**: Add new feature to existing symbol-table Object in symbol-table class              

<br>   


## Special thanks     
[my dear teacher](https://github.com/aligrudi)    
[Younes Nikbin](https://github.com/younes-nb)     
[AmirAli Fallahi](https://github.com/amoorali)     
[Alireza Zahiri](https://github.com/alirezazahiri)    
[Sajjad Seifi](https://github.com/sajjadseifihttps://github.com/sajjadseifi)     

<br> 






