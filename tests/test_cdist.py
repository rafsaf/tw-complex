from tw_complex.cdist import CDistAndKNN
import tests.utils as utils


def test_CDistAndKNN():
    utils.run_all_tests(CDistAndKNN, "CDistAndKNN", _precision=0.8, draw=True)
