# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_priority_encoder(dut):
    """Test the priority encoder functionality."""

    dut._log.info("Starting priority encoder test")

    # Define test cases: (ui_in, expected uo_out)
    test_cases = [
        # Test case 1: First logic 1 at bit 13
        (0b0010101011110001, 0b00001101),  # 13 in decimal
        # Test case 2: First logic 1 at bit 0
        (0b0000000000000001, 0b00000000),  # 0 in decimal
        # Test case 3: All bits are 0 (special case)
        (0b0000000000000000, 0b11110000),  # Special case output
        # Test case 4: First logic 1 at bit 7
        (0b0000000010000000, 0b00000111),  # 7 in decimal
        # Test case 5: First logic 1 at bit 15
        (0b1000000000000000, 0b00001111),  # 15 in decimal
    ]

    for ui_in, expected in test_cases:
        # Set input
        dut.ui_in.value = ui_in

        # Wait for 10 time units to ensure values settle
        await Timer(10, units="ns")

        # Check expected output
        assert dut.uo_out.value == expected, f"Priority encoder failed: ui_in = {ui_in:016b}, uo_out = {dut.uo_out.value:08b}, expected {expected:08b}"

    dut._log.info("Priority encoder test completed successfully")
