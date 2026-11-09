"""Assemble all sheets (and later the HTML page)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import s_ga, s_ga2, s_d1, s_d1b, s_d2, s_d3, s_d2b, s_d3b


def all_sheets():
    return [s_ga.sheet_ga1(), s_ga2.sheet_ga2(), s_d1b.sheet_fan(), s_d1b.sheet_diffuser(), s_d1b.sheet_chamber(), s_d1.sheet_contraction(), s_d2b.sheet_test_section(), s_d2b.sheet_balance(), s_d3b.sheet_airspeed(), s_d3b.sheet_joints()]


if __name__ == '__main__':
    print([s.code for s in all_sheets()])
