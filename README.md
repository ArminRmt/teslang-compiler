 ## teslang-compiler
### Compiler Frontend  +  IR  (ply)

## Design patterns           
### **Singelton**  : with just one instance of CodeGenerator()              
### **Composite**: Create a tree-like structure with Ast                     
### **Visitor**: AstVisitor class explores an Object without changing it            
### **Iterator**: Acess symbol table class objects one by one           
### **Decorator**: Add new feature to existing symbol-table Object in symbol-table class              

<br>        

## What implemented    

- Lexical Analysis     
- Parsing    
- Semantic Analysis    
- Code Generation    
- Optimization   (register)
- scopes     
- error correction    
- forward referencing     
- solid principles notice carefully    
- comments (faze3)     
- built-in functions     
- interpreter support for debugging or making an entire interpreter in future     

<br>    

## faze 1,2
Lexical Analysis and Parsing implemented    
this faze implemented well organized and maintainable but it is two pass compiler means small tricks for the different parts  taken instead of parsing in and Performing semantic operations    

<br>    

## faze 3        

Code Generation implemented based on my teacher doc and TSVM           
you can find out about TSVM [here](https://github.com/aligrudi/tsvm/tree/master)     
 
notice: based on my limited time this faze was not implemented in an efficient way also optimization was not considered done but I entirely gave ideas to follow in TODO and comments in code for implementation of your own.      

<br> 

## Special thanks     
[my dear teacher](https://github.com/aligrudi)    
[Younes Nikbin](https://github.com/younes-nb)     
[AmirAli Fallahi](https://github.com/amoorali)     
[Alireza Zahiri](https://github.com/alirezazahiri)    
[Sajjad Seifi](https://github.com/sajjadseifihttps://github.com/sajjadseifi)     

<br> 






