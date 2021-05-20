from tw_complex.brute import CDistBrute
import tests.utils as utils


def test_CDistBrute():
    utils.run_all_tests(CDistBrute, "CDistBrute", _precision=1, draw=True)
