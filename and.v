module and(
    input [8:0] a,
    input [8:0] b,
    output [8:0] c
);
    assign c = a & b;
endmodule