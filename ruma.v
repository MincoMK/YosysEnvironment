module ruma(clk, rst, out);
    parameter WIDTH = 32;
    input clk, rst;
    output reg [WIDTH-1:0] out;

    always @(posedge clk) begin
        if (rst) begin
            out <= WIDTH-1'b0;
        end else begin
            out <= out + 1;
        end
    end
endmodule