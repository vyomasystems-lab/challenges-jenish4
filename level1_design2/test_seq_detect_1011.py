# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')

    I = []
    for i in range (50):

        I.append(random.randint(0,1))           	    
        
        #input driving

        dut.inp_bit.value = I[-1]
        exp_out=0
        if (I[-4:]==[1,0,1,1]):
            exp_out = 1

        await Timer(2, units='ns')

    #    dut._log.info(f'S={S:05} I0={I0:05} model={I[S]:05} DUT={int(dut.out.value):05}')
        assert dut.seq_seen.value == exp_out, "Randomised test failed with: expected value={EXP}, output={OUTPUT}, last 6 inputs={I6}".format(EXP=exp_out, OUTPUT=dut.seq_seen.value, I6=I[-6:])
