import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """

    ### YOUR CODE HERE ###
    pi_estimate = 0

    a = 1
    b = 1 / pow(2, 0.5)
    t = 0.25
    p = 1

    # perform 10 iterations of this loop
    for i in range(1, 10):
        a_1 = (a + b) / 2
        b = pow(a * b, 0.5)
        t = t - p * pow((a_1 - a), 2)
        p = 2 * p
        a = a_1

        # print out the current loop iteration. This is present to have something in the loop.
        #print("Loop Iteration: ", i)

    # modify this line below to estimate PI
    pi_estimate = pow(a + b, 2) / (4 * t)

    # change this so an actual value is returned
    return abs(target_error - pi_estimate)

desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
