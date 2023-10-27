module ruma(clk, rst, out);
    input clk, rst;
    output reg [7:0] out;

    always @(posedge clk) begin
        if (rst) begin
            out <= 8'b0;
        end else begin
            out <= out + 1;
        end
    end
endmodule