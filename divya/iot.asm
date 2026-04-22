ORG 0000H        
    MOV R1, #35H;
    MOV R2, #26H; 
    MOV A, R1;
    ADD A, R2; 
HERE: 
    SJMP HERE;
END 
