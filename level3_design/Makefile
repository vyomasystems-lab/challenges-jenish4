# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/FSM.v               # provide your design path

TOPLEVEL := FSM          # design file
MODULE   := test_FSM    # test file

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
