from tw_complex.cdist_knn import CDistAndKNN
import tests.utils as utils
import logging


def test_CDistAndKNN():
    utils.run_all_tests(CDistAndKNN, "CDistAndKNN", _precision=0.8, draw=False)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    utils.run_all_tests(CDistAndKNN, "CDistAndKNN", _precision=0.8, draw=True)
