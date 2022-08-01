# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer

@cocotb.test()
async def test_fsm(dut):
    """Test for Traffic Light Controller FSM """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')

    for i in range (50):
        
        A = random.randint(0,1)
        B = random.randint(0,1)           	    
        
        #input driving

        dut.inp_a.value = A
        dut.inp_b.value = B

        # The following formulas are calculated using K Maps.
        exp_l_a = 2*dut.current_state[1] + dut.current_state[0]*(1-dut.current_state[1])
        exp_l_b = 2*(1-dut.current_state[1]) + dut.current_state[0]*dut.current_state[1]

        await Timer(2, units='ns')

    #    dut._log.info(f'S={S:05} I0={I0:05} model={I[S]:05} DUT={int(dut.out.value):05}')
        assert dut.l_a.value == exp_l_a, "Randomised test failed with: expected l_a value={EXP}, output={OUTPUT}, inp_a={a}, inp_b={b}".format(EXP=exp_l_a, OUTPUT=dut.l_a.value, a=A, b=B)
        assert dut.l_b.value == exp_l_b, "Randomised test failed with: expected l_b value={EXP}, output={OUTPUT}, inp_a={a}, inp_b={b}".format(EXP=exp_l_b, OUTPUT=dut.l_b.value, a=A, b=B)
