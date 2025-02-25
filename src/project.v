/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_priority_16_8_encode(
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered, so you can ignore it
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);


    always @(*) begin
        // Default output for all inputs 0
        uo_out = 8'b11110000;

        // Priority encoding logic
        if (ui_in[15]) uo_out = 8'd15;
        else if (ui_in[14]) uo_out = 8'd14;
        else if (ui_in[13]) uo_out = 8'd13;
        else if (ui_in[12]) uo_out = 8'd12;
        else if (ui_in[11]) uo_out = 8'd11;
        else if (ui_in[10]) uo_out = 8'd10;
        else if (ui_in[9]) uo_out = 8'd9;
        else if (ui_in[8]) uo_out = 8'd8;
        else if (ui_in[7]) uo_out = 8'd7;
        else if (ui_in[6]) uo_out = 8'd6;
        else if (ui_in[5]) uo_out = 8'd5;
        else if (ui_in[4]) uo_out = 8'd4;
        else if (ui_in[3]) uo_out = 8'd3;
        else if (ui_in[2]) uo_out = 8'd2;
        else if (ui_in[1]) uo_out = 8'd1;
        else if (ui_in[0]) uo_out = 8'd0;
    end

  // All output pins must be assigned. If not used, assign to 0.
  //assign uo_out  = ui_in + uio_in;  // Example: ou_out is the sum of ui_in and uio_in
  assign uio_out = 0;
  assign uio_oe  = 0;

  // List all unused inputs to prevent warnings
  wire _unused = &{ena, clk, rst_n, 1'b0};

endmodule
