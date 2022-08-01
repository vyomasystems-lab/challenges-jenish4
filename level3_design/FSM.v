// Verilog module for Traffic Light Controller FSM
module FSM(l_a, l_b, inp_a, inp_b, reset, clk);

  output [1:0] l_a, l_b;
  input inp_a;
  input inp_b;
  input reset;
  input clk;

  parameter GR = 0,	// Green-Yellow signals respectively
            YR = 1, 
            RG = 2,
            RY = 3,

  reg [1:0] current_state, next_state;

  // state transition
  always @(posedge clk)
  begin
    if(reset)
    begin
      current_state <= GR;
    end
    else
    begin
      current_state <= next_state;
    end
  end

  // state transition based on the input and current state
  always @(inp_a or inp_b or current_state)
  begin
    next_state = GR;  // Default State
    case(current_state)
      GR:
      begin
        if(inp_a == 1)
          next_state = GR;
        else
          next_state = YR;
      end
      YR:
      begin
        next_state = RG;
      end
      RG:
      begin
        if(inp_b == 1)
          next_state = RG;
        else
          next_state = RY;
      end
      RY:
      begin
        next_state = GR;
      end      
    endcase
  end
  
  // Output Logic
  
  // 0 - Green
  // 1 Yellow
  // 2 - Red
  
  assign l_a = {current_state == GR} ? 0 : 2;
  assign l_a = {current_state == YR} ? 1 : 2;
  
  assign l_b = {current_state == RG} ? 0 : 2;
  assign l_b = {current_state == RY} ? 1 : 2;
  
endmodule
