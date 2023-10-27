module ruma(rst, up, out);
    input rst;
    input [7:0] up;
    output [7:0] out;

    reg [7:0] num;

    always @(posedge rst)
        if (rst) num <= 0;

    always @(posedge up)
        if (up) num <= num + 1;
endmodule