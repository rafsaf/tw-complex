from tw_complex.cdist_brute import CDistBrute
import tests.utils as utils
import logging


def test_CDistBrute():
    utils.run_all_tests(CDistBrute, "CDistBrute", _precision=1, draw=False)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    utils.run_all_tests(CDistBrute, "CDistBrute", _precision=1, draw=True)
