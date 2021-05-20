import time
import logging
from typing import Any, Literal
import matplotlib.pyplot as plt
import numpy as np
from tw_complex.brute import CDistBrute


def run_all_tests(Algorithm: Any, name: str, draw=True, _precision: float = 1):
    # ally
    points1 = np.random.rand(10000, 2) + [2, 0]

    points2 = np.random.rand(15000, 2)
    min_radius = 1.4
    max_radius = 2
    run_test(
        Algorithm,
        points1,
        points2,
        min_radius,
        max_radius,
        name,
        "easy",
        draw=draw,
        _precision=_precision,
    )

    # ally
    points1 = np.random.rand(500, 2) * 25 + [10, 0]

    points21 = np.random.rand(100, 2) * 25 - [0, 10]
    points22 = np.random.rand(1000, 2) * 25
    points2 = np.array([i for i in points21] + [i for i in points22])
    min_radius = 4
    max_radius = 10
    run_test(
        Algorithm,
        points1,
        points2,
        min_radius,
        max_radius,
        name,
        "easy",
        draw=draw,
        _precision=_precision,
    )

    # ally
    points1 = np.random.rand(2500, 2) * 33 + [10, 0]

    points21 = np.random.rand(1000, 2) * 33 - [0, 10]
    points22 = np.random.rand(5000, 2) * 33
    points2 = np.array([i for i in points21] + [i for i in points22])
    min_radius = 4
    max_radius = 10
    run_test(
        Algorithm,
        points1,
        points2,
        min_radius,
        max_radius,
        name,
        "easy",
        draw=draw,
        _precision=_precision,
    )

    # ally
    points11 = np.random.rand(10000, 2) * 100 + [90, 0]
    points12 = np.random.rand(10000, 2) * 100 - [80, 0]
    points1 = np.array([i for i in points11] + [i for i in points12])

    points2 = np.random.rand(20000, 2) * 100
    min_radius = 20
    max_radius = 60
    run_test(
        Algorithm,
        points1,
        points2,
        min_radius,
        max_radius,
        name,
        "hard",
        draw=draw,
        _precision=_precision,
    )

    # ally
    points1, points2 = points2, points1
    min_radius = 10
    max_radius = 120
    run_test(
        Algorithm,
        points1,
        points2,
        min_radius,
        max_radius,
        name,
        "hard",
        draw=draw,
        _precision=_precision,
    )


def run_test(
    Algorithm: Any,
    points1,
    points2,
    min_radius,
    max_radius,
    name: str,
    level: Literal["easy", "medium", "hard"],
    draw=True,
    _precision: float = 1,
):
    logger = logging.getLogger(name)

    precise_front, precise_back = CDistBrute(
        ally_villages=points1,
        enemy_villages=points2,
        min_radius=min_radius,
        max_radius=max_radius,
    ).result()
    precise_front = set(tuple(x) for x in precise_front)
    precise_back = set(tuple(x) for x in precise_back)

    logger.info(f"Starting new test... ")
    logger.info(
        f"Ally: {len(points1)}, Enemy: {len(points2)}, min_r: {min_radius}, max_r: {max_radius}, level: {level}"
    )
    tries = []
    front_accuracy = []
    back_accuracy = []
    for _ in range(5):
        x1 = time.time()
        front, back = Algorithm(
            ally_villages=points1,
            enemy_villages=points2,
            min_radius=min_radius,
            max_radius=max_radius,
            _precision=_precision,
        ).result()
        if draw and _ == 0:
            figure, axis = plt.subplots(1, 2)
            axis[0].plot(
                points1[:, 0],
                points1[:, 1],
                linestyle="None",
                color="blue",
                marker="o",
                markersize=5,
            )
            axis[0].plot(
                points2[:, 0],
                points2[:, 1],
                linestyle="None",
                color="red",
                marker="o",
                markersize=2,
            )
            axis[0].set_title("BEFORE: Blue - ally, red - enemy")

            axis[1].plot(
                points1[:, 0],
                points1[:, 1],
                linestyle="None",
                color="blue",
                marker="o",
                markersize=5,
            )
            axis[1].plot(
                points2[:, 0],
                points2[:, 1],
                linestyle="None",
                color="red",
                marker="o",
                markersize=2,
            )
            axis[1].plot(
                back[:, 0],
                back[:, 1],
                linestyle="None",
                color="gold",
                marker="o",
                markersize=5,
            )
            axis[1].plot(
                front[:, 0],
                front[:, 1],
                linestyle="None",
                color="lime",
                marker="o",
                markersize=5,
            )
            axis[1].set_title("AFTER: Lime - Front, Gold - Back")
            plt.show()
        x2 = time.time()
        tries.append(x2 - x1)
        front_max = len(front)
        if front_max == 0:
            front_max = 1
        front_hit = 0
        back_max = len(back)
        if back_max == 0:
            back_max = 1
        back_hit = 0

        for coord in [tuple(x) for x in front]:
            if (
                coord in precise_front
                and coord not in precise_back
                and coord not in back
            ):
                front_hit += 1

        front_accuracy.append(front_hit / front_max)
        for coord in [tuple(x) for x in back]:
            if (
                coord in precise_back
                and coord not in precise_front
                and coord not in front
            ):
                back_hit += 1

        if len(precise_front) == 0 and len(front) == 0:
            front_hit += 1
        if len(precise_back) == 0 and len(back) == 0:
            back_hit += 1
        back_accuracy.append(back_hit / back_max)

    logger.info(f"Average time is {round(np.mean(tries),3)}s")
    logger.info(
        f"Front accuracy: {round(np.mean(front_accuracy)* 100,1)}%, Back accuracy: {round(np.mean(back_accuracy)* 100,1)}%"
    )
    logger.info(f"Finished...")
    logger.info("")
