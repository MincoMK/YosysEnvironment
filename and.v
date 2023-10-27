module andv(a, b, c);
    input [7:0] a;
    input [7:0] b;
    output [7:0] c;
    assign c = a & b;
endmodule